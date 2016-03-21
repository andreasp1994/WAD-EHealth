/**
 * Created by pitsillos on 20/03/16.
 */
$(document).ready(function(){
    $('#save-to').click(function(){
        var parent = $(this).parent();
        var title = parent.find('a#title').html();
        var page_url = parent.find('a#title').attr('href');
        var summary = parent.find('h5#summary').html();
        var r = parent.find('span#read').html();
        var p = parent.find('span#pola').html();
        var s = parent.find('span#subj').html();
        $('.dropdown-toggle').dropdown();
        $('#cat-li').click(function(){
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

});