/**
 * Created by pitsillos on 20/03/16.
 */
$(document).ready(function(){
    var page_url, summary, r, s, p,title;
    $('#save-to').click(function(){
        var parent = $(this).parent();
        title = parent.find('a#title').html();
        page_url = parent.find('a#title').attr('href');
        summary = parent.find('h5#summary').html();
        r = parent.find('span#read').html();
        p = parent.find('span#pola').html();
        s = parent.find('span#subj').html();

        $('.dropdown-toggle').dropdown();
    });

    $('.cat-li').click(function(){

            var cat_id = $(this).data('cat-id');
            var baseurl = '/explorer/sidebar/favourites/?task=';
            var url = baseurl.concat("AJAX_SAVE_TO","&title=",title,"&url=",page_url,
                "&summary=",summary,"&id=",cat_id,"&read=",r,"&pola=",p,"&subj=",s);
            
            $.get(url,function(data){
                temp = data;
                $('#sidebar').html(temp);
            });
        });

});