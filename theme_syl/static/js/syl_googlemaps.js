$('.gmap').each(function(){
	var mapID = $(this).attr('id');
	var mapData = eval(mapID);
	if (GBrowserIsCompatible()) {
		var map = new GMap2(document.getElementById(mapID));
		map.addControl(new GLargeMapControl());
		map.addControl(new GMapTypeControl());
		var point = new GLatLng(mapData.latitude, mapData.longitude);
		map.setCenter(point, 11, G_SATELLITE_MAP);
		function createMarker(point, icon) {
			var icon = new GIcon();
			icon.image = "/theme/images/pointer.png";
			//icon.shadow = "../img/shadow.png";
			icon.iconSize = new GSize(22, 22);
			//icon.shadowSize = new GSize(36,20);
			icon.iconAnchor = new GPoint(11, 6);
			icon.infoWindowAnchor = new GPoint(10, 6);
			var marker = new GMarker(point, icon);
			return marker;
		}
		mm = createMarker(point);
		map.addOverlay(mm);
		mm.openInfoWindowHtml('<div class="gmap-text"><div class="gmap-text-date">'+mapData.date+'</div>'+mapData.message+'<div class="gmap-sponsor"><img src="/theme/images/logo-suunto.png" height="37" width="119"/></div></div>');
	//	var ovSize=new GSize(150, 110)
	//	var ovMap=new GOverviewMapControl(ovSize);
	//	map.addControl(ovMap);
	//	var mini=ovMap.getOverviewMap();
	//	GEvent.addListener(mini,"load",function(){
	//		ovMap.hide(true);
	//	});
	//	setTimeout("ovMap.setMapType(G_SATELLITE_MAP);",100);
	}
});
