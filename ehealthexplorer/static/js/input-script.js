$(document).ready(function () {
    $('.tab-pane li').click(function(e){
            var search_box =  $("#search_box");
            search_box.val(search_box.val() + $(e.target).text() + " ");
            search_box.focus();
        });
});
