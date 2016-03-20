/**
 * Created by pitsillos on 20/03/16.
 */

$(function(){
    var availableTags = ['Lipitor','Nexium','Plavix','Advair','Abilify','Seroquel',
                    'Singulair','Crestor','Actos'];

    $("#search_box").autocomplete({
        source: availableTags
    });
});
