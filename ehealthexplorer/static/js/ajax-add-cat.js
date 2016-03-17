/**
 * Created by Andreas on 15/03/2016.
 */
$(document).ready(function () {
    $('.add-cat').click(function(e){

        $.post("",
            {
                name:"New Category ",
                task:"AJAX_ADD_CATEGORY",
                csrfmiddlewaretoken:'{{ csrf_token }}'
             },
            function(){

                $.get('/explorer/sidebar/favourites/'  , function(data) {
                temp = data;
                $('#sidebar').html(temp);
                });
            })
            .fail(function(xhr) {
                console.log("Error: " + xhr.statusText);
                alert("Error: " + xhr.statusText);
            });

        e.preventDefault();
        return false;
    });

});