
$(document).ready(function (e) {
    const basic_cords = [39.6487498, 66.9646865];

    var map = L.map('map').setView(basic_cords, 15);

    // Dark Layer
    var CartoDB_DarkMatter = L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        minZoom: 13
    });

    // add dark layer to map
    CartoDB_DarkMatter.addTo(map);

    for (i of DATA) {
        L.geoJSON(i, {
            style: e => { return { fillColor: colorize(i), color: 'none', fillOpacity: 1 } },
            onEachFeature: onEachFeature
        }).addTo(map);
    }

    function onEachFeature(feature, layer) {
        //bind click
        layer.on({
            click: whenClicked
        });
    }


    function colorize(e) {
        let year = parseInt(e.properties.year);
        if (year > 1000 && year <= 1878) return "#f5fe95";
        else if (year > 1878 && year <= 1917) return "#ffb301";
        else if (year > 1917 && year <= 1958) return "#ff7801";
        else if (year > 1958 && year <= 1966) return "#ff0109";
        else if (year > 1966 && year <= 1984) return "#ff017c";
        else if (year > 1984 && year <= 1991) return "#0066fe";
        else if (year > 1991 && year <= 2000) return "#0066fe";
        else if (year > 2000 && year <= 2008) return "#0066fe";
        else if (year > 1984 && year <= 2016) return "#0066fe";
        else if (year > 2016 && year <= 2022) return "#0066fe";
        else return "#7d7d7d";
    };

    

    function whenClicked(e) {
        showPopUp(e);
    }
    




});