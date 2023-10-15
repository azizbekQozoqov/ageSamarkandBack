
$(document).ready(function (e) {
    const basic_cords = [39.6487498, 66.9646865];
    const endpoint = 'http://agesamarkand.uz';

    var map = L.map('map').setView(basic_cords, 15);

    // Dark Layer
    var CartoDB_DarkMatter = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        minZoom: 13
    });

    var buildingsLayer = L.tileLayer(`${endpoint}/api/{z}/{x}/{y}.png/${start_year}/${end_year}`, {
        minZoom: 13
    });

    // add dark layer to map
    CartoDB_DarkMatter.addTo(map);
    buildingsLayer.addTo(map);

    // function onEachFeature(feature, layer) {
    //     //bind click
    //     layer.on({
    //         click: whenClicked
    //     });
    // }


   

    // function whenClicked(e) {
    //     showPopUp(e);
    // }
    




});