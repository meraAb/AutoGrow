
var app = {
	
	
	online: null,
	
    // Application Constructor
    initialize: function() {
	
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
		document.addEventListener('online', this.onDeviceOnline.bind(this), false);
		document.addEventListener('offline', this.onDeviceOffline.bind(this), false);
        document.addEventListener('resize', this.onDeviceResize.bind(this), false);
		document.addEventListener("volumeupbutton", callbackFunction, false);  
        function callbackFunction() { 
        alert('Volume Up Button is pressed!');
        }

    },

    // deviceready Event Handler
    //
    // Bind any cordova events here. Common events are:
    // 'pause', 'resume', etc.
    
	onDeviceOnline: function() {
        this.receivedEvent('online');
    },
	onDeviceOffline: function() {
        this.receivedEvent('offline');
    },
	onDeviceResize: function() {
        this.receivedEvent('resize');
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
		if (id == "online"){
			this.online= True;
			App_Dialogs.ShowAlert("this device is online",null,"network status","ok");
			}
		else if (id == "offline"){
			this.online=False;
						App_Dialogs.ShowAlert("this device is offline",null,"network status","ok");

			
				}
				else if (id == "deviceready"){
				App_Controller.initialize();						
			
				}
		else if (id == "resize"){
			
			}	 
       
    }
};
app.initialize();

var App_Model={
	 initialize: function() {
		 
		 
		 }
	
	};
	var App_View={
	 initialize: function() {
		 
		 
		StatusBar.overlaysWebView(false);
		 StatusBar.styleBlackTranslucent();
		 StatusBar.backgroundColorByName("black");
		 }
	
	};
	var App_Controller={
	 initialize: function() {
		 
		 App_View.initialize();
		 App_Model.initialize();
		 navigator.notification.alert("startup complete", null, "test","ok")

		 }
	
	};