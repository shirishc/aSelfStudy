var numCats = 3;
var countCat = [];

for (var i = 0; i < numCats; i++) {
	countCat.push(0);
	var $div = $("<div>", {id : "cat-img"+(i+1), 
							class: "center-content",
							text: "Cat No " + (i+1)});
	$div.append("<img src='http://placekitten.com/" + 
				(305+i) + "/" + (305+i) + "'>");
	// Using IIFE  - Immediately invoked function expression
	// Outer function is returning the inner function which
	// will be given out to click event but at the same time 
	// calling itself with the index to remember the index for
	// this event listener - closure
	// Without this it doesn't work as i keeps changing in the 
	// loop
	$div.click((function(index) {
		// console.log("itr - " + i + ", count - " + countCat[i]);
		return function() {
			countCat[index]++;
			var strCnt = "";
		
			for (var j = 0; j < numCats; j++) {
				strCnt += "<p>Cat Image " + (j+1) + 
			 				"- No of clicks - " + countCat[j] + 
			 				"</p>";
			}
			$("#counter").html(strCnt);	
		}		
	})(i));
	// Trying this with just a normal cliosure without IIFE

	$("#cat-images").append($div);
};

