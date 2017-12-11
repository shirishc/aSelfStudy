$(function(){
	
	var model = {
        init: function() {
            if (!localStorage.cats) {
                localStorage.cats = JSON.stringify([
                	{name:"Emma", clicks:0, 
                		url:"images/Cat-images/emma.jpeg"},
                	{name:"Lizzy", clicks:0, 
                		url:"images/Cat-images/lizzy.jpeg"},
                	{name:"George", clicks:0, 
                		url:"images/Cat-images/george.jpeg"},
					{name:"Stuart", clicks:0, 
						url:"images/Cat-images/stuart.jpeg"},
					{name:"Kevin", clicks:0, 
						url:"images/Cat-images/kevin.jpeg"},
					{name:"Sara", clicks:0, 
						url:"images/Cat-images/sara.jpeg"}
				]);
            }
        },
        add: function(obj) {
            var data = JSON.parse(localStorage.cats);
            data.push(obj);
            localStorage.cats = JSON.stringify(data);
        },
        update: function(currCatIdx, name, url, clicks) {
        	var data = JSON.parse(localStorage.cats);
            data[currCatIdx].name = name;
            data[currCatIdx].url = url;
            data[currCatIdx].clicks = clicks;
        	localStorage.cats = JSON.stringify(data);
        },
        incrementClick: function(idx) {
        	var data = JSON.parse(localStorage.cats);
            data[idx].clicks++;
            localStorage.cats = JSON.stringify(data);	
        },
        getAllCats: function() {
            return JSON.parse(localStorage.cats);
        }
    };

    var octopus = {
    	currCatIdx: 0,
    	adminMode: 0,

        init: function() {
            model.init();
            view.init();
        },

        getAllCats: function() {
            return model.getAllCats();
        },

        getCurrentCat: function() {
        	return model.getAllCats()[this.currCatIdx];
        },

		updateCat: function(name, url, clicks) {
        	model.update(this.currCatIdx, name, url, clicks);
        	view.render();
        },

        updateAdminMode: function(mode) {
        	this.adminMode = mode;
        	view.render();
        },

        changeCatSel: function(catIdx) {
            this.currCatIdx = catIdx;
            view.render();
        },

        imageClicked: function() {
        	model.incrementClick(this.currCatIdx);
        	view.render();
        }
    };

    var view = {
        init: function() {
            console.log("View Init called");
        	$("#Cat-List").change(function() {
				var idx = $('#Cat-List option:selected').val();
				octopus.changeCatSel(idx);
			});
			$("#Cat-Image").click(function() {
				octopus.imageClicked();
			});
			$("#AdminBtn").click(function() {
				octopus.updateAdminMode(1);
			});
			$("#CancelBtn").click(function() {
				octopus.updateAdminMode(0);
			});
			$("#UpdateBtn").click(function() {
				octopus.updateCat(
					$("#nameEditBox").val(),
            		$("#urlEditBox").val(),
            		$("#numClkEditBox").val());	
			});
			view.renderCatList();
            view.render();
        },
        renderCatList: function() {
        	var catList = octopus.getAllCats();
			for (var i = 0; i < catList.length; i++) {
				$("#Cat-List").append("<option value=" + i + ">" 
						+ catList[i].name + "</option>");
			}
        },
        render: function() {
            view.renderCat();
            view.renderAdmin();
        },
        renderCat: function() {
        	var currCat = octopus.getCurrentCat();
            $("#Cat-Image").attr("src", currCat.url);
            $("#Cat-Name").text(currCat.name);
			$("#Cat-Click").text("Num of Clicks for " 
						+ currCat.name + " - " + currCat.clicks);
        },
        renderAdmin: function() {
        	if (octopus.adminMode == 1) {
        		var currCat = octopus.getCurrentCat();
        		$("#AdminForm").show();
        		$("#nameEditBox").val(currCat.name);
            	$("#urlEditBox").val(currCat.url);
            	$("#numClkEditBox").val(currCat.clicks);
        	}
        	else {
	        	$("#AdminForm").hide();
	    	}
        }
    };

    $(document).ready(function() {
        console.log("Document Ready");
    });
    octopus.init();
});
