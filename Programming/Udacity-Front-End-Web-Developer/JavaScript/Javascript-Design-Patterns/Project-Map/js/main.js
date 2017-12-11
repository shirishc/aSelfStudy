$(function(){
	
	var model = {
        init: function() {
        },
    };

    var octopus = {
        init: function() {
            model.init();
            view.init();
        },
    };

    var view = {
        viewMap: 0,
        infoWindow: 0,
        allMarkers: 0,

        init: function() {
            allMarkers = [];
            $("#srchForm").submit(function(e) {
                var loc = $("#location").val();
                geocoder = new google.maps.Geocoder();
                geocoder.geocode( {"address": loc}, function(results, status) {
                    if(status === google.maps.GeocoderStatus.OK) {
                        viewMap.setCenter(results[0].geometry.location);
                        view.createMarker(results[0]);
                    }
                });
                e.preventDefault();
            });
            
            $("#restaurants").on("click", function(e) {
                if (!$(this).prop('checked')) {
                    view.clearAllMarkers();
                }
                else {
                    view.showService("restaurant");
                }
            });

            $("#hotels").on("click", function(e) {
                if (!$(this).prop('checked')) {
                    view.clearAllMarkers();
                }
                else {
                    view.showService("room");
                }
            });

            $("#barsnPubs").on("click", function(e) {
                if (!$(this).prop('checked')) {
                    view.clearAllMarkers();
                }
                else {
                    view.showService("bar");
                }
            });

            view.render();
        },
        render: function() {
            var mapDiv = document.getElementById('mapContainer');
            viewMap = new google.maps.Map(mapDiv, {
                center: {lat: 35.615185, lng: 139.750064},
                zoom: 15});
            infoWindow = new google.maps.InfoWindow();
        },
        createMarker: function(place) {
            var currMarker = new google.maps.Marker({
                                map: viewMap,
                                position: place.geometry.location
            });
            allMarkers.push(currMarker);
            google.maps.event.addListener(currMarker, "click", function() {
                infoWindow.setContent(place.name);
                infoWindow.open(viewMap, this);
            });
        },
        clearAllMarkers: function() {
            allMarkers.forEach(function(currMarker) {
                currMarker.setMap(null);
            });
            allMarkers = [];
        },
        showService: function(serviceType) {          
            var service = new google.maps.places.PlacesService(viewMap);
            // Other functions like radarSearch, textSearch are all there which are better
            service.nearbySearch({
                    location: viewMap.getCenter(),
                    radius: 500,
                    types: Array(serviceType)
                }, 
                function(results, status) {
                    if (status === google.maps.places.PlacesServiceStatus.OK) {
                        results.forEach(view.createMarker);
                    }
                }
            );
        }
    };

    octopus.init();
});
