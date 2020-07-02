function createMarker(point, element) {
  var marker = new GMarker(point);
  GEvent.addListener(marker, "click", function() {
    marker.openInfoWindowHtml(element.innerHTML);
  });
  return marker;
}

function loadTrip() {
  var mapnode = $("map");
  if (!mapnode) {
      return;
  }
  if (GBrowserIsCompatible()) {
    var map = new GMap2(mapnode);
    // set center
    var longitude = document.getElementById("long").innerHTML;
    var latitude = document.getElementById("lat").innerHTML;
    map.addControl(new GSmallMapControl());
    //map.addControl(new GMapTypeControl());
    map.setCenter(new GLatLng(latitude, longitude), 7);
    var location = document.getElementById("locations");
    var elements = location.getElementsByTagName("li");
    var k = 0;
    for (k = 0; k < elements.length; k++) {
        latitude = elements[k].getAttribute("latitude");
        longitude = elements[k].getAttribute("longitude");
        var point = new GLatLng(latitude, longitude);
        map.addOverlay(createMarker(point, elements[k]));
    }
  }
}
addLoadEvent(loadTrip);
