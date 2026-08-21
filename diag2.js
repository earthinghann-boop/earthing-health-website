var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Issue 1: Check zoom CSS
var styleEnd = h.indexOf('</style>');
var styleBlock = h.slice(0, styleEnd);
var zoomIdx = styleBlock.lastIndexOf('.product-image:hover');
if (zoomIdx !== -1) {
    console.log('Zoom CSS found at byte', zoomIdx, ':');
    console.log(styleBlock.slice(Math.max(0, zoomIdx - 10), zoomIdx + 200));
} else {
    console.log('Zoom CSS NOT FOUND in style block');
    var allZoom = h.indexOf('.product-image:hover');
    console.log('In whole file at:', allZoom);
}

// Issue 2: Check structure
var firstA = h.indexOf('<a href="');
console.log('\nFirst <a href> context:');
console.log(h.slice(Math.max(0, firstA - 30), firstA + 200));

// Check a few carousels - find their nearest href
var ids = ['fittedCarousel','shawlCarousel','kitCordCarousel','quiltCarousel'];
ids.forEach(function(id) {
    var cidx = h.indexOf('<div class="carousel" id="' + id + '"');
    if (cidx === -1) { console.log(id + ': NOT FOUND'); return; }
    var nearbyA = h.lastIndexOf('<a href="', cidx);
    if (nearbyA === -1) { console.log(id + ': no <a href> before carousel'); return; }
    var href = h.slice(nearbyA + 9, h.indexOf('"', nearbyA + 9));
    console.log(id + ': href=' + href + ' | carousel at byte ' + cidx);
});

// Check carousel nesting - find first product-image
var pi = h.indexOf('<div class="product-image">');
console.log('\nproduct-image start:');
console.log(h.slice(pi, pi + 300));