var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Find inline style blocks
var pos = 0; var count = 0;
while (true) {
    var o = h.indexOf('<style', pos);
    if (o === -1) break;
    var c = h.indexOf('</style>', o);
    count++;
    console.log('style block #' + count + ': byte ' + o + '-' + c + ', ' + (c - o) + ' chars');
    pos = c + 8;
}
console.log('Total:', count, 'style blocks');
// Find key carousel CSS
var styleSlice = h.slice(0, h.indexOf('<script>'));
var carouselCSS = styleSlice.slice(Math.max(0, styleSlice.indexOf('.carousel')));
carouselCSS = carouselCSS.slice(0, 3000);
console.log('\nFirst 200 chars of carousel CSS:');
console.log(carouselCSS.slice(0, 200));
// Find .product-card CSS
var prodCardIdx = styleSlice.indexOf('.product-card');
if (prodCardIdx !== -1) {
    var prodCSS = styleSlice.slice(prodCardIdx, prodCardIdx + 500);
    console.log('\n.product-card CSS (first 400):');
    console.log(prodCSS.slice(0, 400));
}
// Find .products-grid CSS
var gridIdx = styleSlice.indexOf('.products-grid');
if (gridIdx !== -1) {
    var gridCSS = styleSlice.slice(gridIdx, gridIdx + 300);
    console.log('\n.products-grid CSS:');
    console.log(gridCSS.slice(0, 300));
}
// Check if goGB is referenced
console.log('\ngoGB referenced:', h.indexOf('goGB') !== -1);
console.log('goProductSlide referenced:', h.indexOf('goProductSlide') !== -1);
console.log('moveProductSlide referenced:', h.indexOf('moveProductSlide') !== -1);