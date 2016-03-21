$(document).ready(function () {

    var readability = document.getElementById('readability');
    noUiSlider.create(readability, {

        start: [0, 100],
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
        start: [-1, 1],
        connect: true,
        range: {
            'min': -1,
            'max': 1
        }
    });
    var polSnapValues = [
	document.getElementById('pol-slider-snap-value-lower'),
	document.getElementById('pol-slider-snap-value-upper')];

    polarity.noUiSlider.on('update', function( values, handle ) {
	polSnapValues[handle].innerHTML = values[handle];});

    var subjectivity = document.getElementById('subjectivity');
    noUiSlider.create(subjectivity, {
        start: [0, 1],
        connect: true,
        range: {
            'min': 0,
            'max': 1
        }
    });

     var subSnapValues = [
	document.getElementById('sub-slider-snap-value-lower'),
	document.getElementById('sub-slider-snap-value-upper')];

    subjectivity.noUiSlider.on('update', function( values, handle ) {
	subSnapValues[handle].innerHTML = values[handle];});
});