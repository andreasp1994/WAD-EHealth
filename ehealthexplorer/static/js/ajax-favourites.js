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

    $('.delete-icon').click(function(e){

        var cat_id = $(e.target).closest('label').attr('for');
        $.post("",
            {
                task:"AJAX_DELETE_CATEGORY",
                id:cat_id
            },
            function () {
                $.get('/explorer/sidebar/favourites/'  , function(data) {
                temp = data;
                $('#sidebar').html(temp);
                });
            })
            .fail(function(xhr){
                console.log("Error: " + xhr.statusText);
                alert("Error: " + xhr.statusText);
            });

        e.preventDefault();
        return false;
    });

    $('.share-icon').click(function(e){

        var cat_id = $(e.target).closest('label').attr('for');
        $.post("",
            {
                task:"AJAX_SHARE_CATEGORY",
                id:cat_id
            },
            function () {
                $.get('/explorer/sidebar/favourites/'  , function(data) {
                temp = data;
                $('#sidebar').html(temp);
                });
            })
            .fail(function(xhr){
                console.log("Error: " + xhr.statusText);
                alert("Error: " + xhr.statusText);
            });

        e.preventDefault();
        return false;
    });

    $('.rename-icon').click(function(e) {
        var element = $(e.target).parent().find("span")
        var editableText = $("<input type='text' />");
        editableText.addClass('my-editable');
        editableText.val(element.html().trim());
        element.replaceWith(editableText);
        editableText.focus();

        editableText.keypress(function (e) {
            if (e.which == 13) { //Enter pressed
                var cat_id = $(e.target).closest('label').attr('for');
                var name = editableText.val();
                $.post("",
                    {
                        task:"AJAX_RENAME_CATEGORY",
                        id:cat_id,
                        new_name:name
                    },
                    function () {
                        $.get('/explorer/sidebar/favourites/'  , function(data) {
                        temp = data;
                        $('#sidebar').html(temp);
                        });
                    })
                    .fail(function(xhr){
                        console.log("Error: " + xhr.statusText);
                        alert("Error: " + xhr.statusText);
                    });
            }
        });
    });

    $('.fav-delete-icon').click(function(e) {

        var topic_id = $(e.target).data('id');
        $.post("",
            {
                task:"AJAX_DELETE_FAVOURITE",
                id:topic_id
            },
            function () {
                $.get('/explorer/sidebar/favourites/'  , function(data) {
                temp = data;
                $('#sidebar').html(temp);
                });
            })
            .fail(function(xhr){
                console.log("Error: " + xhr.statusText);
                alert("Error: " + xhr.statusText);
            });

        e.preventDefault();
        return false;
    });



});