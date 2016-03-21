/**
 * Created by Andreas on 15/03/2016.
 */
$(document).ready(function () {

    var baseurl = '/explorer/sidebar/favourites/?task=';

    $('.add-cat').click(function(e){

        var url = baseurl.concat("AJAX_ADD_CATEGORY");

        $.get(url, function (data) {
            temp = data;
            $('#sidebar').html(temp);
        });

        e.preventDefault();
        return false;
    });

    $('.delete-icon').click(function(e){

        var cat_id = $(e.target).closest('label').attr('for');
        var url = baseurl.concat("AJAX_DELETE_CATEGORY","&id=",cat_id);

        $.get(url, function (data) {
            temp = data;
            $('#sidebar').html(temp);
        });

        e.preventDefault();
        return false;
    });

    $('.share-icon').click(function(e){

        var cat_id = $(e.target).closest('label').attr('for');
        var url = baseurl.concat("AJAX_SHARE_CATEGORY","&id=",cat_id);
        $.get(url, function (data) {
            temp = data;
            $('#sidebar').html(temp);
        });

        e.preventDefault();
        return false;
    });

    $('.rename-icon').click(function(e) {
        var element = $(e.target).parent().find("span");
        var editableText = $("<input type='text' />");
        editableText.addClass('my-editable');
        editableText.val(element.html().trim());
        element.replaceWith(editableText);
        editableText.focus();

        editableText.keypress(function (e) {
            if (e.which == 13) { //Enter pressed
                var cat_id = $(e.target).closest('label').attr('for');
                var name = editableText.val();
                var url = baseurl.concat("AJAX_RENAME_CATEGORY","&id=",cat_id,"&name=",name);
                $.get(url, function (data) {
                    temp = data;
                    $('#sidebar').html(temp);
                });
            }
        });
    });

    $('.fav-delete-icon').click(function(e) {

        var topic_id = $(e.target).data('id');
        var url = baseurl.concat("AJAX_DELETE_FAVOURITE","&id=",topic_id);
        $.get(url, function (data) {
            temp = data;
            $('#sidebar').html(temp);
        });

        e.preventDefault();
        return false;
    });



});