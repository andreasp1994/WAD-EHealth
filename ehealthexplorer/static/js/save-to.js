/**
 * Created by pitsillos on 20/03/16.
 */
$(document).ready(function(){

    // Element to get
    var element = $('#save-to');
    var parent = element.parent();
    var h6 = parent.find('h6');
    var spans = h6.children();
    var scores = [];
    for (var i=0;i<spans.length;i++){
        scores[i] = spans[i].html;
    }

    // Data
    var result_title = parent.find('a').html();
    var result_url = parent.find('a').attr('href');
    var result_summary = parent.find('h5').html();

    var span = element.children();
    span.click(function(){
        $('dropdown-toggle').dropdown();
    });

});