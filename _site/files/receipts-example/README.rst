A sample app for demonstrating receipts and their libraries. Not intended for
anything serious. Other than remembering where your scotch is.

This doesn't really use any frameworks (apart from bootstrap) and is really
just a way to demonstrate what receipts are and how they work.

It does it in three ways:

- a very naive implementation that cracks the receipt open and verifies it
  against the server. This is so you can see how the receipt is accessed and
  how the verifying server works https://wiki.mozilla.org/Apps/WebApplicationReceipt.
  This approach is *not recommended*.

- using a proxy to send the receipt too, which then forwards on to the
  verifying server. This uses http://django-receipts.herokuapp.com/.

- the *recommended* approach of using the mozmarket.js receipt verifier library
  here: https://github.com/mozilla/receiptverifier

This app can be found on the test mozilla marketplace: https://marketplace-dev.allizom.org/app/myscotch/
where you can buy it for play money and check the receipts.
