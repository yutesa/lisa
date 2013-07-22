$(function(){
	$('#frmUbicacion').submit(function(e){
		e.preventDefault();

		$.post('/sistema/ubicacion/add', $(this).serialize(), function(data){
			if (data.codigo == 1)
			{
				alert(data.msg);
				document.location = '/sistema/mis_ubicaciones/';
			} else if (data.codigo == 2) {
				alert(data.msg);
			}
		}, 'json');
	});
});