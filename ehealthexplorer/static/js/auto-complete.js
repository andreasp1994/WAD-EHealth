/**
 * Created by pitsillos on 20/03/16.
 */

$(function(){
    var availableTags = ['Lipitor','Nexium','Plavix',
        'Advair','Abilify','Seroquel',
        'Singulair','Crestor','Actos',
        'Excessive Thirst', 'Increased Urinations',
        'Blurred Vision', 'Runny Nose', 'Stuffy Nose',
        'Cough', 'Sneezing', 'Unexplained Bleeding',
        'Unexplained Weightloss', 'Lump', 'Unexplained Pain',
        ];

    $("#search_box").autocomplete({
        source: availableTags
    });
});
