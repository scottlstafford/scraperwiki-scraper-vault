<?php
scraperwiki::attach("blaskjell");           

$data = scraperwiki::select(           
    "* from `skjell`,`location_data` where `location_data`.`Malested`=`skjell`.`Malested`"
);

foreach ($data as $data) {
if (strlen($data['data_lat']) > 0) {
$markers[] = "['<h3>". addslashes(trim($data['Sted'])) ."</h3><p>Målested: ". $data['Malested'] ."</p><p>". $data['Melding'] ."</p>',". $data['data_lat'] .",". $data['data_lng'] ."]";
}
}

$markers = implode(",", $markers);
?>
<html>
<head>
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js" type="text/javascript"></script>
<script type="text/javascript">
jQuery.noConflict();

jQuery(document).ready(function($){

var map = new google.maps.Map(document.getElementById('map_canvas'), {
  zoom: 13,
  center: new google.maps.LatLng(60.2733674, 5.7220194),
  mapTypeId: google.maps.MapTypeId.ROADMAP
});

var infowindow = new google.maps.InfoWindow();

var homemarker, marker, i;

var bounds = new google.maps.LatLngBounds();

var locations = [<?php echo $markers; ?>];

for (i = 0; i < locations.length; i++) {  

latLng = new google.maps.LatLng(locations[i][1], locations[i][2]);

var image = new google.maps.MarkerImage("http://mapicons.nicolasmollet.com/wp-content/uploads/mapicons/shape-default/color-8c4eb8/shapecolor-color/shadow-1/border-dark/symbolstyle-white/symbolshadowstyle-dark/gradient-no/restaurant.png", new google.maps.Size(32, 37), new google.maps.Point(0,0), new google.maps.Point(0, 32));

  marker = new google.maps.Marker({
    position: latLng,
    icon: image,
    map: map
  });
  
  bounds.extend(latLng);
  
  google.maps.event.addListener(marker, 'click', (function(marker, i) {
    return function() {
      infowindow.setContent(locations[i][0]);
      infowindow.open(map, marker);
    }
  })(marker, i));
}

map.fitBounds(bounds);


}); 
</script>

<style type="text/css">
body {
    margin: 0;
    padding: 0;
    font:0.8em/1.5em "Lucida Grande", "Lucida Sans Unicode", Helvetica, Arial, sans-serif;
    }
</style>

</head>
<body>
<div id="map_canvas" style="width: 100%; height: 100%;"></div>
</body>
</html>
<?php
scraperwiki::attach("blaskjell");           

$data = scraperwiki::select(           
    "* from `skjell`,`location_data` where `location_data`.`Malested`=`skjell`.`Malested`"
);

foreach ($data as $data) {
if (strlen($data['data_lat']) > 0) {
$markers[] = "['<h3>". addslashes(trim($data['Sted'])) ."</h3><p>Målested: ". $data['Malested'] ."</p><p>". $data['Melding'] ."</p>',". $data['data_lat'] .",". $data['data_lng'] ."]";
}
}

$markers = implode(",", $markers);
?>
<html>
<head>
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js" type="text/javascript"></script>
<script type="text/javascript">
jQuery.noConflict();

jQuery(document).ready(function($){

var map = new google.maps.Map(document.getElementById('map_canvas'), {
  zoom: 13,
  center: new google.maps.LatLng(60.2733674, 5.7220194),
  mapTypeId: google.maps.MapTypeId.ROADMAP
});

var infowindow = new google.maps.InfoWindow();

var homemarker, marker, i;

var bounds = new google.maps.LatLngBounds();

var locations = [<?php echo $markers; ?>];

for (i = 0; i < locations.length; i++) {  

latLng = new google.maps.LatLng(locations[i][1], locations[i][2]);

var image = new google.maps.MarkerImage("http://mapicons.nicolasmollet.com/wp-content/uploads/mapicons/shape-default/color-8c4eb8/shapecolor-color/shadow-1/border-dark/symbolstyle-white/symbolshadowstyle-dark/gradient-no/restaurant.png", new google.maps.Size(32, 37), new google.maps.Point(0,0), new google.maps.Point(0, 32));

  marker = new google.maps.Marker({
    position: latLng,
    icon: image,
    map: map
  });
  
  bounds.extend(latLng);
  
  google.maps.event.addListener(marker, 'click', (function(marker, i) {
    return function() {
      infowindow.setContent(locations[i][0]);
      infowindow.open(map, marker);
    }
  })(marker, i));
}

map.fitBounds(bounds);


}); 
</script>

<style type="text/css">
body {
    margin: 0;
    padding: 0;
    font:0.8em/1.5em "Lucida Grande", "Lucida Sans Unicode", Helvetica, Arial, sans-serif;
    }
</style>

</head>
<body>
<div id="map_canvas" style="width: 100%; height: 100%;"></div>
</body>
</html>
