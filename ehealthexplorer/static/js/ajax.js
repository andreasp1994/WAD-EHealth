$(document).ready(function () {
    $('.main-menu li a').click(function(e){
        $.get($(e.target).data('link')  , function(data) {
            temp = data;
            $('#sidebar').html(temp);
        });
    });
});