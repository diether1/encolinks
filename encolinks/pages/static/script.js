$(document).ready(function(){

    $('#result').hide();

    var makeShrink = function() {

        var validateInput = true;
        if($('.url-input').val() == ""){
            $('.url-input').parent().removeClass("has-success");
            $('.url-input').parent().addClass('has-feedback has-error');
            $('.url-input').parent().find('span').addClass('glyphicon-remove');
            return;
        }else{
            $('.url-input').parent().removeClass("has-error");
            $('.url-input').parent().find('span').removeClass('glyphicon-remove');
            $('.url-input').parent().addClass('has-feedback has-success');
            $('.url-input').parent().find('span').addClass('glyphicon-ok');
        }

        var txtToShrink = $('input[name="url"]')
        $.post('/api/shrink/',
            {url: txtToShrink.val()},
            function(data) {
                txtToShrink.val("");
                $('#result').html(
					"<input class='form-control' type='text' value='" + data.url + "'>"
				);
                $('#result').fadeIn();
            }
        );
        return false;
    };
    $('#shrink').on('click', makeShrink);
    
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
