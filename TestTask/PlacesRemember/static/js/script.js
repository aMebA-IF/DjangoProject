function updateCoordinates(lat, lng) {
    document.getElementById('id_latitude').value = lat;
    document.getElementById('id_longitude').value = lng;
  }
  
  function initMap() {
    var map, marker;
    var myLatlng = {
      lat: 56.00435778741845,
      lng: 92.76696590524162
    };

    if (String(document.getElementById('id_latitude').value).length == 0){
      document.getElementById('id_latitude').value = myLatlng.lat;
      document.getElementById('id_longitude').value = myLatlng.lng;
    }

    else{
      myLatlng.lat = parseFloat(String(document.getElementById('id_latitude').value).replace(',','.'));
      myLatlng.lng = parseFloat(String(document.getElementById('id_longitude').value).replace(',','.'));
    }

    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: myLatlng
    });
    
    marker = new google.maps.Marker({
      position: myLatlng,
      map: map,
      draggable: true
    });
  
    marker.addListener('dragend', function(e) {
      var position = marker.getPosition();
      updateCoordinates(position.lat(), position.lng())
    });
  
    map.addListener('click', function(e) {
      marker.setPosition(e.latLng);
      updateCoordinates(e.latLng.lat(), e.latLng.lng())
    });
  
    map.panTo(myLatlng);
  }