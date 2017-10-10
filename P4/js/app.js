var map;

// Array of Location Objects for the Map
var locationList = [{
        name: 'Boxpark Shoreditch',
        lat: 51.523704,
        lng: -0.076474
    },
    {
        name: 'Queen of Hoxton',
        lat: 51.523704,
        lng: -0.081235
    },
    {
        name: 'Junkyard Golf Club',
        lat: 51.521133,
        lng: -0.072511
    },
    {
        name: 'Bounce, Old Street',
        lat: 51.526797,
        lng: -0.084208
    },
    {
        name: 'Flight Club Shoreditch',
        lat: 51.522172,
        lng: -0.086588
    },
    {
        name: 'Old Truman Brewery',
        lat: 51.521887,
        lng: -0.072257
    },
    {
        name: 'The Breakfast Club',
        lat: 51.527037,
        lng: -0.081236
    },
    {
        name: 'Hoxton Grill',
        lat: 51.525594,
        lng: -0.082995
    },
    {
        name: 'The Magic Roundabout',
        lat: 51.525673,
        lng: -0.087435
    }
]

// Map styling via Snazzy Maps 
var styles = [{
        "featureType": "all",
        "elementType": "labels.text.fill",
        "stylers": [{
            "color": "#ffffff"
        }]
    },
    {
        "featureType": "all",
        "elementType": "labels.text.stroke",
        "stylers": [{
                "color": "#000000"
            },
            {
                "lightness": 13
            }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.fill",
        "stylers": [{
            "color": "#000000"
        }]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.stroke",
        "stylers": [{
                "color": "#144b53"
            },
            {
                "lightness": 14
            },
            {
                "weight": 1.4
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "all",
        "stylers": [{
            "color": "#08304b"
        }]
    },
    {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [{
                "color": "#0c4152"
            },
            {
                "lightness": 5
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [{
            "color": "#000000"
        }]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [{
                "color": "#0b434f"
            },
            {
                "lightness": 25
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "geometry.fill",
        "stylers": [{
            "color": "#000000"
        }]
    },
    {
        "featureType": "road.arterial",
        "elementType": "geometry.stroke",
        "stylers": [{
                "color": "#0b3d51"
            },
            {
                "lightness": 16
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "geometry",
        "stylers": [{
            "color": "#000000"
        }]
    },
    {
        "featureType": "transit",
        "elementType": "all",
        "stylers": [{
            "color": "#146474"
        }]
    },
    {
        "featureType": "water",
        "elementType": "all",
        "stylers": [{
            "color": "#021019"
        }]
    }
]

var ViewModel = function() {

    var self = this;
    this.bounds = new google.maps.LatLngBounds();

    // Function to provide info when a marker is clicked
    this.populateInfoWindow = function(marker, infowindow) {
        if (infowindow.marker != marker) {
            infowindow.marker = marker;
            // Log lat & lng to the console for checking
            console.log(marker.lat);
            console.log(marker.lng);
            // Flickr API Key
            var api_key = '521e1447c9a835d529381db9e38d4dcb';
            // Build api url using multiple data sources
            var api = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=' + api_key + '&has_geo=1&lat=' + marker.lat + '&lon=' + marker.lng + '&radius=0.01&per_page=4&format=json&nojsoncallback=1';
            // Log the url to the console for checking
            console.log(api);
            // Build the initial content for the InfoWindow
            this.content = '<div class="marker-content"><h3 class="marker-title">' + marker.title + '</h3>';
            this.content += '<p>Recent images from Flickr for this area</p>';
            // Request JSON via API call to Flickr
            $.getJSON(api, function(data) {
                var images = data.photos.photo;
                // Return a url path for each individual image
                for (var i = 0; i < images.length; i++) {
                    var url = 'https://farm' + images[i].farm + '.staticflickr.com/' + images[i].server + '/' + images[i].id + '_' + images[i].secret + '_q.jpg';
                    // Log all Image url to the console for checking
                    console.log(url);
                    // Create an image path for each image returned from the initial api call
                    self.content += '<img class="img-thumb" src="' + url + '">';
                }
                self.content += '</div>';
                infowindow.setContent(self.content);
            }).error(function() {
                self.content += '<p class="error">Data from Flickr can not be loaded at this time</p></div>';
                infowindow.setContent(self.content);
            });
            // Open the InfoWindow
            infowindow.open(map, marker);
            // On click close the InfoWindow
            infowindow.addListener('closeclick', function() {
                infowindow.marker = null;
            });
        }
    };

    // Click Event and Marker Animation function to open the InfoWindow
    this.clickEvent = function() {
        this.setAnimation(google.maps.Animation.BOUNCE);
        setTimeout((function() {
            this.setAnimation(null);
        }).bind(this), 1200);
        self.populateInfoWindow(this, self.largeInfoWindow);
    };


    this.markers = [];
    // Map Initialisation
    this.initMap = function() {

        // New Map parameter set up
        map = new google.maps.Map(document.getElementById('map'), {
            center: {
                lat: 51.525378,
                lng: -0.081725
            },
            zoom: 15,
            styles: styles,
            mapTypeControl: false
        });

        this.largeInfoWindow = new google.maps.InfoWindow();

        // Customize Marker Icons
        var defaultIcon = makeMarkerIcon('ffe600');

        function makeMarkerIcon(markerColor) {
            var markerImage = new google.maps.MarkerImage(
                'http://chart.googleapis.com/chart?chst=d_map_spin&chld=1.15|0|' + markerColor +
                '|40|_|%E2%80%A2',
                new google.maps.Size(21, 34),
                new google.maps.Point(0, 0),
                new google.maps.Point(10, 34),
                new google.maps.Size(21, 34));
            return markerImage;
        }

        // Loop through Location List to create a Marker for each place
        for (var i = 0; i < locationList.length; i++) {
            this.lat = locationList[i].lat;
            this.lng = locationList[i].lng;
            this.title = locationList[i].name;
            this.marker = new google.maps.Marker({
                lat: this.lat,
                lng: this.lng,
                position: {
                    lat: this.lat,
                    lng: this.lng
                },
                title: this.title,
                animation: google.maps.Animation.DROP,
                icon: defaultIcon,
                id: i
            });
            // Check for Marker Object
            console.log(this.marker);
            // Display each Marker on the Map
            this.marker.setMap(map);
            this.markers.push(this.marker);
            // Trigger for opening the InfoWindow
            this.marker.addListener('click', self.clickEvent);
        }

        for (var i = 0; i < this.markers.length; i++) {
            this.markers[i].setMap(map);
            self.bounds.extend(this.markers[i].position);
        }

        // Ensures map view stays within the bounds of every Marker
        window.onresize = function() {
            map.fitBounds(self.bounds);
        };
    }
    // Call to initialize the Map
    this.initMap();

    // Filter the List of Locations and Markers
    this.filter = ko.observable("");
    this.locationFilter = ko.computed(function() {
        var filteredArray = [];
        for (var i = 0; i < this.markers.length; i++) {
            var selectedLocation = this.markers[i];
            // Compare if the filter value is included in the Location title
            if (selectedLocation.title.toLowerCase().includes(this.filter().toLowerCase())) {
                filteredArray.push(selectedLocation);
                this.markers[i].setVisible(true);
            } else {
                // Hide the marker from the Location list and Map
                this.markers[i].setVisible(false);
            }
        }
        return filteredArray;
    }, this);
}

// Error function in case Map does not Load
mapLoadError = function() {
    var mapError = "<span class='map-load-error'>Failed to Load Map. Please try again!</span>";
    document.getElementById('side-nav').innerHTML = mapError;
}

function appLoad() {
    ko.applyBindings(new ViewModel());
}
