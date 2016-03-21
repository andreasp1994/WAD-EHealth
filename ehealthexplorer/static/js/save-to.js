/**
 * Created by pitsillos on 20/03/16.
 */
$(document).ready(function(){
    $('#save-to').click(function(){

        var upper_div = $(this).parent().find('div');
        var title = upper_div.find('a').html();
        var page_url = upper_div.find('a').attr('href');
        var spans = upper_div.find('h6').children();
        var summary = upper_div.find('h5').html();
        $('.dropdown-toggle').dropdown();
        $('#cat-li').click(function(){
            alert('adding cat');
            var cat_name = $(this).find('a').html();
            var baseurl = '/explorer/sidebar/favourites/?task=';
            var url = baseurl.concat("AJAX_SAVE_TO","&title=",title,"&url=",page_url,
                "&summary=",summary,"&name=",cat_name,"&read=",spans[0].innerHTML,
                "&pola=",spans[1].innerHTML,"&subj=",spans[2].innerHTML);
            $.get(url,function(data){
                temp = data;
                $('#sidebar').html(temp);
            });
        });
    });

});