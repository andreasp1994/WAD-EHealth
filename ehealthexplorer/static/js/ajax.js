$(document).ready(function () {
    /*
    Dynamic content switch
     */
    $('.main-menu li a').click(function(e){
        $.get($(e.target).data('link')  , function(data) {
            temp = data;
            $('#sidebar').html(temp);

        });
    });

    $('.top-navigation-link').click(function(e){
        $.get($(e.target).data('link')  , function(data) {
            temp = data;
            $('#sidebar').html(temp);
        });
    });

});


