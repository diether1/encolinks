$(document).ready(function(){
    var makeShrink = function() {
        var txtToShrink = $('input[name="url"]')
        $.post('/api/shrink/',
            {url: txtToShrink.val()},
            function(data) {
                txtToShrink.val("");
                $('#result').html(
					"<input class='form-control' type='text' value='" + data.url + "'>"
				);
            }
        );
        return false;
    };
    $('#shrink').bind('click', makeShrink);
    
    var getLinkInfo = function() {
        var txtToInfo = $('input[name="url"]')
        $.getJSON('/api/info/?url=' + txtToInfo.val(),
            {},
            function(data) {
                txtToInfo.val("");
                $('#result').html(
                    "<table class='table table-striped'><tr><td>Link:</td><td>" + data.url + "</td></tr>" +
                    "<tr><td>Código:</td><td>" + data.cod + "</td></tr>" +
                    "<tr><td>Acessos:</td><td>" + data.qtd + "</td></tr>" +
                    "<tr><td>Último acesso:</td><td>" + data.last_access + "</td></tr></table>"
                );
            }
        );
    };
    $('#info').bind('click', getLinkInfo);
})
