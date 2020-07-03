var install = function install(ev) {
  ev.preventDefault();
  var manifest_url = "https://mckay.pub.ca/files/receipts-example/manifest.webapp";
  navigator.mozApps.install(manifest_url);
}

var add = function add(ev) {
  ev.preventDefault();
  var req = window.navigator.mozApps.getSelf();
  req.onsuccess = function(o) {
    console.log('on success');
    req.addReceipt('test-bad-receipt');
  }
}

document.onreadystatechange = function() {
  if (document.readyState === 'complete') {
    document.getElementById('install').addEventListener('click', install, false);
    document.getElementById('add').addEventListener('click', add, false);
  }
};
