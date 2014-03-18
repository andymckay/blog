The Firefox Marketplace currently accepts payments for apps and in-app payments. This allows developers to earn some money from their apps.

Currently we've got just one payment provider who is integrated into the Firefox Marketplace, the great team at <a href="http://bango.com/">Bango</a> have been integrating credit card and carrier billing. But we don't want to stop there, we'd like to have lots of options for different payment providers that meet the different consumers and developers needs.

Implementing payments for the Firefox Marketplace is a little different from any other site because, unlike most implementations, Mozilla does not look after holding money and paying developers, the payment providers do. This creates issues for payment providers who don't normally operate this way.

To explain how we do things at Mozilla, we wanted to write a specification of how to integrate with the backend. But writing specifications is no fun, writing code is more fun. So we wrote a sample backend for payment providers, its called <a href="http://zippypayments.readthedocs.org/en/latest/">Zippy</a>.

As it turns out writing Zippy gives us a bunch of other advantages:

* Tests can now be run on the entire payment flow from start to end without having to spend real money.
* We <a href="http://zippy.paas.allizom.org/styleguide">have real HTML, JS and CSS</a> for the payment pages so payment providers don't need to implement it, just integrate our code.
* We can use the Mozilla localisation teams to <a href="https://localize.mozilla.org/projects/zippy">provide localisations</a>.
* Payment providers now have a working implementation they can poke and prod and examine.

Here's an example of a payment using the Zippy backend, in French:

<video src="http://people.mozilla.org/~amckay/presentation/movs/purchase.ogg" controls>

So if you are payment provider and wanted to integrate payments with the Marketplace, all you have to do is implement Zippy on your end in what ever language or platform you like. As long as it implements the same REST APIs. We'll need to enable you as a payment provider in the Marketplace, so you'll want to speak to us before you start doing work on it.

The code is available under the <a href="http://www.mozilla.org/MPL/2.0/">MPL</a>, is written in <a href="http://nodejs.org/">Node.js</a> and is the hard work of <a href="http://github.com/davidbgk/">David Larlet</a>, <a href="http://github.com/muffinresearch/">Stuart Colville</a> and <a href="http://github.com/kumar303/">Kumar McMillan</a>. It's in the early days right now, being at version 0.1 and I'm sure there are lots of new features to come.
