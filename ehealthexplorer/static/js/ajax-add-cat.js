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
            function(data,status){
              alert("Data: " + data + "\nStatus: " + status);
            })
            .fail(function(xhr) {
                console.log("Error: " + xhr.statusText);
                alert("Error: " + xhr.statusText);
            });

        e.preventDefault();
        return false;
    });

});