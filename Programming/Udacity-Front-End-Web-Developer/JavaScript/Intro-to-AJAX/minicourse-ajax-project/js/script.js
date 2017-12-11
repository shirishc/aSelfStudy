
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    var streetStr = $('#street').val();
    var cityStr = $('#city').val();
    var addressStr = streetStr + ", " + cityStr; 
    var googURL = 'https://maps.googleapis.com/maps/api/streetview?size=600x400&location=' + addressStr;
    
    $greeting.text("So, you want to live at " + addressStr + "?");
    $body.append("<img class='bgimg' src=" + googURL +">");

    var NYTimesKey = "1484431dc1a334efcf7aee2a17e2ef75:4:74082345";
    var NYTurlHead = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=";
    var NYTurl = NYTurlHead + addressStr + "&sort=newest&api-key=" + NYTimesKey;

    $.getJSON(NYTurl, function(data) {
        $nytElem.text("New York Times articles about " + cityStr);

        var items = [];
        // console.log(data);
        $.each(data.response.docs, function(idx, doc) {
            $nytElem.append("<li class='article'>" + 
                            "<a href='" + doc.web_url + "'>" + doc.headline.main + "</a>" + 
                            "<p>" + doc.snippet + "</p></li>");
        });
    })
    .error(function(e) {
        $nytElem.text("New York Times articles FAILED");
    });
    
    var wikiURL = "http://en.wikipedia.org/w/api.php?action=opensearch&search="
                    + cityStr + "&format=json&callback=wikiCallback";
    
    // $wgCrossSiteAJAXdomains = Array("*.wikipedia.org");

    // No error handling in this case and so we set a timeout of 8 secs
    var wikiRequestTimeOut = setTimeout(function() {
        $wikiElem.text("failed to get wikipedia resources");
    }, 8000);

    $.ajax({
        url: wikiURL, 
        dataType: "jsonp", 
        success: function (wikiData) {
            
            var articleList = wikiData[1];
            var urlList = wikiData[3];
            
            for (var i = 0; i < articleList.length; i++) {
                $wikiElem.append("<li>" + 
                            "<a href='" + urlList[i] + "'>" + articleList[i] + "</a>" + 
                            "</li>");
            };

            // Clear the time out in case we have success in AJAX request
            clearTimeout(wikiRequestTimeOut);
        }
    });

    return false;
};

$('#form-container').submit(loadData);
