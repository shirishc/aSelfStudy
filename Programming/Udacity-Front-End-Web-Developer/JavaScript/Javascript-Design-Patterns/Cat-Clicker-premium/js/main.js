var file_path = "images/Cat-images/";

var catList = [ "Emma", "Lizzy", "George",
	"Stuart", "Kevin", "Sara"
];
var clickCount = [ 0, 0, 0, 0, 0, 0];

for (var i = 0; i < catList.length; i++) {
	$("#Cat-List").append("<option value=" + i + ">" 
						+ catList[i] + "</option>");
};

$("#Cat-List").change(function() {
	var idx = $('#Cat-List option:selected').val();
	var file_name = file_path + catList[idx] + ".jpeg";
	
	if(!$("#Cat-Image").has("img").length) {
		// console.log("Didn't get image");
		$("#Cat-Image").append("<img src='" + 
							file_name + "'>");	
	} else {
		// console.log("Got image");
		$("#Cat-Image").find("img").attr("src", file_name);	
	}

	$("#Cat-Name").text(catList[idx]);
	$("#Cat-Click").text("Num of Clicks for " 
						+ catList[idx] + " - "
						+ clickCount[idx]);
});

$("#Cat-Image").click(function() {
	var idx = $('#Cat-List option:selected').val();
	clickCount[idx]++;
	$("#Cat-Click").text("Num of Clicks for " 
						+ catList[idx] + " - "
						+ clickCount[idx]);
});
