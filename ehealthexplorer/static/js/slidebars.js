$(document).ready(function () {

    var readability = document.getElementById('readability');
    noUiSlider.create(readability, {

        start: [rl, ru],
        connect: true,
        range: {
            'min': 0,
            'max': 100
        }
    });

    var readSnapValues = [
	document.getElementById('read-slider-snap-value-lower'),
	document.getElementById('read-slider-snap-value-upper')];

    readability.noUiSlider.on('update', function( values, handle ) {
	readSnapValues[handle].innerHTML = values[handle];});

    var polarity = document.getElementById('polarity');
    noUiSlider.create(polarity, {
        start: [pl, pu],
        connect: true,
        range: {
            'min': 0,
            'max': 100
        }
    });
    var polSnapValues = [
	document.getElementById('pol-slider-snap-value-lower'),
	document.getElementById('pol-slider-snap-value-upper')];

    polarity.noUiSlider.on('update', function( values, handle ) {
	polSnapValues[handle].innerHTML = values[handle];});

    var subjectivity = document.getElementById('subjectivity');
    noUiSlider.create(subjectivity, {
        start: [sl, su],
        connect: true,
        range: {
            'min': 0,
            'max': 100
        }
    });

     var subSnapValues = [
	document.getElementById('sub-slider-snap-value-lower'),
	document.getElementById('sub-slider-snap-value-upper')];

    subjectivity.noUiSlider.on('update', function( values, handle ) {
	subSnapValues[handle].innerHTML = values[handle];});



    $('.apply-filters').click(function(){
        var query = $('#search_box').val();

        var readability_values = readability.noUiSlider.get();
        var subjectivity_values = subjectivity.noUiSlider.get();
        var polarity_values = polarity.noUiSlider.get();

        var baseurl = "/explorer/results/?";

        window.location = baseurl.concat("rl=",readability_values[0],
                                "&ru=",readability_values[1],
                                "&sl=",subjectivity_values[0],
                                "&su=",subjectivity_values[1],
                                "&pl=",polarity_values[0],
                                "&pu=",polarity_values[1],
                                "&q=",query)
    });


});