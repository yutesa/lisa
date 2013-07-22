$(function(){
	$('#frmLike').submit(function(e){
		e.preventDefault();

		$.post('/Products2/AddLike/', $(this).serialize(), function(data){
			if (data.codigo == 1)
			{
				alert(data.msg);
				document.location = '/Products/YaLike/';
			} else if (data.codigo == 2) {
				alert(data.msg);
			}
		}, 'json');
	});
});