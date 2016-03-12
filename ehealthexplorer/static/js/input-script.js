$(document).ready(function () {

    $('.tab-pane li').click(function(e){
        $("#search_box").val($("#search_box").val() + $(e.target).text() + " ");
    }
    );

});
