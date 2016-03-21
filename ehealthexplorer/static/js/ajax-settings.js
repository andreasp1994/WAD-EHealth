/**
 * Created by pitsillos on 18/03/16.
 */
    $(document).ready(function (){

        var CSRF = $('[name="csrfmiddlewaretoken"]').val();

        $('#edit').click(function (){

            if ($(this).html()=='Edit'){
                $.fn.editable.defaults.mode = 'inline';
                $('.to-edit').editable({
                    success: function(k,v){
                        $('input#'+$(this).attr('id')).val(v);
                }
                });
                $('#edit').html('Save');
            }
            else if ($(this).html()=='Save'){
                $('.to-edit').editable('destroy');
                $('#edit').html('Edit');

                var username = $('input#username').val();
                var email = $('input#email').val();

                $.post("/explorer/sidebar/profile",
                {
                    task:"AJAX_UPDATE",
                    username: username,
                    email: email,
                    csrfmiddlewaretoken: CSRF

                })
                    .done(function () {

                        //$.get(url, function (data) {
                        //    temp = data;
                        //    $('#sidebar').html(temp);
                        //});
                    })
                .fail(function(xhr) {
                    console.log("Error: " + xhr.statusText);
                    alert("Error: " + xhr.statusText);
                });

            }
        });
    });