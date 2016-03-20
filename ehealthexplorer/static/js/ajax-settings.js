/**
 * Created by pitsillos on 18/03/16.
 */
    $(document).ready(function (){
        $('#edit').click(function (){
            if ($(this).html()=='Edit'){
                $.fn.editable.defaults.mode = 'inline';
                $('.to-edit').editable();
                $('#edit').html('Save');
            }
            else if ($(this).html()=='Save'){
                $('.to-edit').editable('destroy');
                $('#edit').html('Edit');
                var spans = document.getElementsByTagName("span");
                var username = spans[0].html;
                var email = spans[1].html;
                $.post("",
                {
                    task:"AJAX_UPDATE",
                    username: username,
                    email: email
                })
                .fail(function(xhr) {
                    console.log("Error: " + xhr.statusText);
                    alert("Error: " + xhr.statusText);
                });

            }
        });
    });