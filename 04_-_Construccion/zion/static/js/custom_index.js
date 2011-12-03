$(document).ready(function() {
	//$("#sesion").css({
	//	'height': "25px",
	//	'overflow': "hidden"
	//});
	//$("#pre-sesion a").text("Iniciar Sesión");
	_sesion = {};
	_sesion.open = false;
	$("#pre-sesion a").click(function(){
		if ( !_sesion.open ){
			_sesion.open = true;
			$("#sesion").animate({
				height:'200px'
			});
			$(this).text("Cancelar");
		} else {
			_sesion.open = false;
			$("#sesion").animate({
				height:'25px'
			});
			$(this).text("Iniciar Sesión");
		}
	});
	
});
