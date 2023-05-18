---
layout: post
title: Service catalog - Using Actions
categories: general
blog: andy-mckay
---

As part of the [service catalog](https://github.com/clearwind-ca/service-catalog) (see [announcement](https://mckay.pub/2023-05-15-service-catalog/)) we want to be able to measure the "quality or readiness" of a service.

Quality or readiness of a service tends to be different from code quality, although they might be overlap. Ideas of readiness could include:

* Does the team specify a place for bugs or feedback?
* Does the team specify an on-call rotation?
* Is the team keeping on top of security issues?
* Is the service meeting legal obligations or compliance?
* Is the service vulnerable to urgent security problems?
* Does the team have appropriate metrics and dashboard?

These questions and more are defined by the organization and different for every organization. Trying to code all those situations and questions is not within the service catalog's goal.

So we need to find a way to allow customers to be able to create and code health checks, while avoiding running arbitrary code in the service catalog [^1]. For this, GitHub Actions came to the rescue.

So let's take an example, scanning all our services to ensure no one is vulnerable to the [Log4J vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2021-44228).

In the service catalog we create a health check for `Log4J`. The service catalog will send a [repository_dispatch](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#repository_dispatch) on a schedule defined in the catalog for this check.

In GitHub we'll write an Action to grab the repository, scan it and send the result back to the service catalog.

Here's how that Action would look:

```
  log4j:
    env:
      # We'll need this to write back to the catalog.
      SERVICE_CATALOG_TOKEN: $\{\{ secrets.SERVICE_CATALOG_TOKEN \}\}
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
      with:
        # Grab the repository for the service that the catalog has sent to us.
        repository: $\{\{ github.event.client_payload.repository \}\}
    - run: |
        # Grab a log4jscanner.
        wget https://github.com/google/log4jscanner/releases/download/v0.5.0/log4jscanner-v0.5.0-linux-amd64.tar.gz
        tar -zxf log4jscanner-v0.5.0-linux-amd64.tar.gz
        cd log4jscanner
        ./log4jscanner $GITHUB_WORKSPACE >> /tmp/log4j.results
        
        # Write some annotations in the Action log and a JSON file
        # ready to send back to the catalog.
        if test -s "/tmp/log4j.results"; then
          contents=$(cat /tmp/log4j.results)
          echo "::error::Vulnerable files found"
          printf '{"result": "fail", "message": "Vulnerable file(s) found: `%s`"}' $contents >> /tmp/service-catalog-result.json
        else
          echo "::notice::All good, no vulnerable files found"
          printf '{"result": "pass"}' >> /tmp/service-catalog-result.json
        fi
        echo `cat /tmp/service-catalog-result.json`

    # Send the result back
    - uses: clearwind-ca/send-result@main 
```

Most of this code is running the log4j scanner and finding the vulnerable files. At the end there's a simple Action [clearwind-ca/send-result](github.com/clearwind-ca/send-result) that sends the results to the service catalog.

Here's a little chart:

```

  ┌────────────────┐
  │ Service        │
  │                ◄──────────┐
  └────────────────┘          │
                              │
  ┌────────────────┐   ┌──────┴─────────┐            ┌───────────────────┐
  │ Health check   │   │ Health check   │ Dispatch   │ GitHub Action     │
  │                ◄───┤ Result         ├────────────►                   │
  └────────────────┘   └──────▲─────────┘            └──────┬────────────┘
                              │                             │
                              └─────────────────────────────┘
                                    Pass, fail response
```

The great parts about this approach are:

* Grabbing and running arbitrary code is now sandboxed with GitHub Actions.
* The code and information about the code is on GitHub anyway (issue, repositories etc) so doing the work on GitHub makes sense.
* GitHub Actions have great secret management, so you can store secrets for other services. That allows you to query other services like Slack, Pager Duty and so on.
* There are thousands of [re-usable Actions within the GitHub Marketplace](https://github.com/marketplace?category=&query=&type=actions&verification=) that we can use to do these checks.

Using Actions this way gives customers the chance to build these checks quickly and simply in Actions. Separation of concerns, allows us to focus on building the best thing in the catalog. And finally, don't want to use Actions? That's cool, there's an API for the Catalog that let's you go down a different path if you like.

--

[^1]: We could also do this by allowing custom code to be run in the catalog, however this has its own share of problems. Access to repositories, secret management, resource utilization, ease of upgrades and so on. Better to use an external service.
