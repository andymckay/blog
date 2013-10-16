So you've put your hard work into building a great app. If you want to get paid for your app then the Marketplace supports app receipts and verification of those receipts.

Receipt verification is how we ensure that your app has been paid for in the case of both hosted and packaged apps. It's important to point out that we don't limit the installation or distribution of apps from the Marketplace. They can be installed by anyone without limitation, they just won't have the receipt.

That means as developers, it is essential to check the receipt in your app. This is the only way to ensure that the payment has been processed.

Receipts are based on the [Web Application Receipt specification](https://wiki.mozilla.org/Apps/WebApplicationReceipt). A receipt is a JSON object that contains information about the purchase. That JSON is then signed using the [JSON Web Token](http://tools.ietf.org/html/draft-ietf-jose-json-web-key) specification.

When the App is installed after purchase, the [receipt is installed](https://developer.mozilla.org/en-US/docs/Web/Apps/JavaScript_API) along with the app. To check that a receipt is installed you can access the receipt through the `mozApps` API, for example `window.navigator.mozApps.getSelf()`.

Once you've expanded a receipt it would look something like the following:

<pre>
{
  "product": {
    "url": "http://example.com",
    "storedata": "id=111111"
  },
  "iss": "https://marketplace.firefox.com",
  "verify": "https://receiptcheck.marketplace.firefox.com/verify/111111", // The verify URL
  "detail": "https://marketplace.firefox.com/en-US/purchases/111111",
  "reissue": "https://marketplace.firefox.com/en-US/app/example/purchase/reissue",
  "user": {
    "type": "directed-identifier",
    "value": "1234-abcd99ef-a123-456b-bbbb-cccc11112222"
  },
  "exp": 1353028900,
  "iat": 1337304100,
  "typ": "purchase-receipt",
  "nbf": 1337304100
}</pre>

Just checking for the presence of the receipt is not enough, there are a few checks that should be performed as well: that the receipt is correctly signed and has not be tampered with, that the receipt is from a marketplace you approve of and that the receipt is for your app.

There are two optional steps you can perform: that the crypto signing on the receipt is correct, that the receipt is still valid with the store.

These last steps require the app to have internet access to be able to call servers.

An easy way to perform most of these checks is to use the [receipt verifier library](https://github.com/mozilla/receiptverifier). After including it:

<pre>
var verifier = new mozmarket.receipts.Verifier({
  // checks that the receipt is for your app.
  productURL: 'http://example.com',
  // only allow apps that came from the firefox marketplace.
  installs_allowed_from: ['https://marketplace.firefox.com']
})
verifier.verify(function (verifier) {
  if (verifier.state instanceof verifier.states.OK) {
    // everything is good.
  } else {
    // something went wrong.
  }
});
</pre>

See the docs for a full [list of the options](https://github.com/mozilla/receiptverifier#options).

The receipt verifier returns a [state object](https://github.com/mozilla/receiptverifier#states-and-errors) that tells you the exact error. We don't prescribe what the app should do under those circumstances, that is left completely to the developer. For example a ``NetworkError`` indicates that we couldn't connect to the verification server. That may, or may not be, a fatal condition for your app.

The receipt verifier library also includes a basic user interface for showing errors to the user. It is great for testing, but since the user interface in your app is going to be different, the chances are you'll want to display messages back to the user in your own style. If you include ``receiptverifier-ui.js``, then you can use the prompter like this:

<pre>
mozmarket.receipts.Prompter({
  storeURL: "https://marketplace.mozilla.org/app/myapp",
  supportHTML: '<a href="mailto:me@example.com">email me@example.com</a>',
  verify: true
});
</pre>

If you ran the app without the receipt installed you would see a message like this: http://cl.ly/image/3p2V3c022n1T

Finally one last thing that the receipt verifier library won't do is verify that a receipt has not been shared between users. That is left as something the app developer will need to implement an example might be using the [django-receipts library](https://github.com/andymckay/django-receipts).

