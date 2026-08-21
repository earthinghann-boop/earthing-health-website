var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
var ids = ['fittedCarousel','quiltCarousel','kitCordCarousel','blanketCarousel','shawlCarousel','kidsCarousel','puSheetCarousel'];
ids.forEach(function(id) {
    var cidx = h.indexOf('<div class="carousel" id="' + id + '"');
    if (cidx === -1) { console.log(id + ': carousel NOT FOUND'); return; }
    var nearA = h.lastIndexOf('<a href="', cidx);
    var href = h.slice(nearA + 9, h.indexOf('"', nearA + 9));
    console.log(id + ': href=' + href);
});