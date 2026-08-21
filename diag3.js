var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
var css = fs.readFileSync('css/style.css', 'utf8');

// 1. Check where </style> is vs zoom CSS
var styleClose = h.indexOf('</style>');
var zoomByte = h.indexOf('.product-image:hover');
console.log('</style> at byte:', styleClose);
console.log('Zoom CSS at byte:', zoomByte);
console.log('Zoom INSIDE style tag?', zoomByte < styleClose);

// 2. Check css/style.css for .carousel-img
var ciIdx = css.indexOf('.carousel-img');
if (ciIdx !== -1) {
    console.log('\n.carousel-img in css/style.css:');
    console.log(css.slice(ciIdx, ciIdx + 300));
} else {
    console.log('\nNo .carousel-img in css/style.css');
}

// 3. Check index.html <style> for .carousel-img
var hStyleEnd = h.indexOf('</style>');
var hStyle = h.slice(0, hStyleEnd);
var ciIdxH = hStyle.indexOf('.carousel-img');
if (ciIdxH !== -1) {
    console.log('\n.carousel-img in HTML <style>:');
    console.log(hStyle.slice(Math.max(0, ciIdxH - 20), ciIdxH + 200));
}

// 4. Check where the zoom CSS was injected - before or after existing carousel rules
var zoomIdxInStyle = hStyle.lastIndexOf('.product-image:hover');
if (zoomIdxInStyle !== -1) {
    console.log('\nZoom CSS position in HTML style (last):', zoomIdxInStyle);
    console.log('Style block size:', hStyleEnd);
    console.log('Zoom is at END of style block?', hStyleEnd - zoomIdxInStyle < 300);
}

// 5. The key issue: is overflow:hidden on .product-image blocking zoom?
// Look for overflow in .product-image rules in css/style.css
var piIdx = css.indexOf('.product-image');
if (piIdx !== -1) {
    console.log('\n.product-image in css/style.css:');
    console.log(css.slice(piIdx, piIdx + 300));
}

// 6. Check what hover-related CSS exists for .product-image
var productImageRules = css.match(/\.product-image[^}]*/g) || [];
console.log('\nAll .product-image rules in css/style.css:', productImageRules.length);
productImageRules.slice(0,3).forEach(function(r) { console.log(r.slice(0,150)); });