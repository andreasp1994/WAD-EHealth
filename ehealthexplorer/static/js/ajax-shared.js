$(document).ready(function () {

    $('#search52').keypress(function (e) {
        if (e.which == 13) { //Enter pressed
            var query = $(e.target).val();

            var baseurl = '/explorer/sidebar/shared/?q=';
            var url = baseurl.concat(query);
            $.get(url, function (data) {
                temp = data;
                $('#sidebar').html(temp);
            });
        }

    });

});