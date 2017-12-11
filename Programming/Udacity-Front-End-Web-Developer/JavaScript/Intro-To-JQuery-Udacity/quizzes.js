/*
For this quiz, use a jQuery class selector and featuredArticle variable to toggle the 'featured' class!
*/

// don't change this variable!
var featuredArticle;

featuredArticle = $(".featured");

featuredArticle.toggleClass("featured");

/*
For this quiz, remove the class 'featured' from Article #2 and add it to Article #3!

You must use jQuery's toggleClass method!
*/

// don't change these variable!
var article2, article3;

// your code goes here!

var articleItems = $(".article-item");
article2 = $(".featured");
article3 = article2.next();

article2.toggleClass("featured");
article3.toggleClass("featured");

/*
For this quiz, set the href of the <a> in the first nav item to "#1".

You must use jQuery's attr() method!
*/

// Start with this variable!
var navList;

navList = $(".nav-item"); // your code goes here!
navList.first().find("a").attr("href", "#1");

/*
For this quiz, change the font-size of all the article-items to 20px!

You must use jQuery's css() method!
*/

// Start with this variable!
var articleItems;

// your code goes here!
articleItems = $(".article-item");
articleItems.css("font-size", "20px");

/*
For this quiz, use jQuery's val method to make live changes to the 'Cool Articles' <h1>!

The starter code below creates an event listener that will run any time the input changes.
For more on events, check the instructor notes.
*/


$('#input').on('change', function() {
    var val;
    val = $('#input').val();
    $(".articles").children("h1").text(val);
});

/*
For this quiz, remove the <ul> from the first article item!

You must use jQuery's remove() method.
*/

// Start with this variable!
var articleItems;

// your code goes here!
articleItems = $(".article-list").children();

articleItems.first().find("ul").remove();

/*
For this quiz, you'll need to add to the DOM tree that already exists.

'#family2' should be a sibling of and come after '#family1'. '#bruce' should be the only immediate child
of '#family2'. '#bruce' should have two <div>s as children, '#madison' and '#hunter'.
*/

// Your code goes here!
var family1 = ("#family1");

var family2 = $("<div>", {id: "family2"});
family2.append("<h1>Family2</h1>");

var bruce = $("<div>", {id: "bruce"});
bruce.append("<h2>Bruce</h2>");
// bruce = $('<div id ="bruce"><h2>Bruce</h2></div>')

var madison = $("<div>", {id: "madison"});
madison.append("<h3>Madison</h3>");

var hunter = $("<div>", {id: "hunter"});
hunter.append("<h3>Hunter</h3>");

bruce.append(madison);
bruce.append(hunter);
family2.append(bruce);

family2.insertAfter(family1);

/*
For this quiz, use jQuery's each() method to iterate through the <p>s,
calculate the length of each one, and add each length to the end of each <p>.

Also, make sure you don't change the text inside each <p>, otherwise your
lengths won't be correct!
*/

// Your code goes here!
$("p").each(function(idx) {
    newTxt = $(this).text() + " " + $(this).text().length;
    $(this).text(newTxt);
});

otherwise

function numAdder() {
	newTxt = $(this).text() + " " + $(this).text().length;
    $(this).text(newTxt);
}
$("p").each(numAdder);

// Shirish - monitorEvents in console - didn't work with logo for me....

/*
For this quiz, use jQuery to set up an event listener. Your event listener must:
    1. listen to the #my-button element
    2. listen for a `click` event
    3. perform the following actions when the button is clicked:
        a. remove the #my-button element from the DOM
        b. add the `success` class to the body
*/

$("#my-button").on("click", function() {
    $(this).remove();
    $("body").addClass("success");
});

// Events examples which might be useful

$( 'article' ).on( 'click', function( evt ) {
    $( evt.target ).css( 'background', 'red' );
});

$( '#myAnchor' ).on( 'click', function( evt ) {
    evt.preventDefault(); // Prevents the default action
    console.log( 'You clicked a link!' );
});

