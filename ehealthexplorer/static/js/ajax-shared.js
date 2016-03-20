$(document).ready(function () {

    $('#search52').keypress(function (e) {
        if (e.which == 13) { //Enter pressed
            var query = $(e.target).val();
            if (query == ""){
                query = "default";
            }
            var baseurl = '/explorer/sidebar/shared/';
            var url = baseurl.concat(query,'/');
            $.get(url, function (data) {
                temp = data;
                $('#sidebar').html(temp);
            });
        }

    });

});