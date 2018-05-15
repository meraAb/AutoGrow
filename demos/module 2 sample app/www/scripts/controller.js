 /*
 	Controller.js

 	Ties all app dependencies together, including UI interaction, user management, and data storage.
 */
(function(ctrl){ 

	ctrl.init = function() {
		// initialize kendo mobile app - only line needed to get started
        new kendo.mobile.Application(document.body, { skin: "flat", 
        	layout: "drawer-layout" });
		
		// load images into carousel
		var imageArray = ["img/pg.jpeg", "img/buildbot-hero.png", "img/devices.png"];
		createImageCarousel(imageArray);
	}

	ctrl.getImage = function (img) {
		$("#curImage").attr("src", img.src);
	}

	// Create a basic image carousel. Clicking on an image thumbnail displays it as the main image selected
	function createImageCarousel(imageArray) {

		$.each(imageArray, function( index, value ) {
		  $("#imageCarousel").append($('<img>',{id:'anImage'+index,src:value,onclick:'controller.getImage(this)',
		  		style:"margin-left:20px; height:50px; width:50px"}));
		});
	}

	ctrl.takePicture = function() {
		alert("Will be implemented in course module 4 - plugins.");
	}

}(window.controller = window.controller || {}));