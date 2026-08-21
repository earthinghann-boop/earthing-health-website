var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');

// Find all section class=gb-category-section in order (using indexOf sequentially)
var markers = [
    'id="fitted-sheet"',
    'id="available-colors"',
    'id="flat-sheet"',
    'id="pillow-case"',
    'id="duvet-cover"',
    'id="kids-bedding"'
];

console.log('Section order:');
markers.forEach(function(m) {
    var idx = h.indexOf('<section class="gb-category-section" ' + m);
    console.log('  ' + m + ' starts at:', idx);
});

// Find where fitted-sheet ends: after its own </section> before id="flat-sheet"
var fittedStart = h.indexOf('<section class="gb-category-section" id="fitted-sheet"');
var flatStart = h.indexOf('<section class="gb-category-section" id="flat-sheet"');
// The fitted section ends somewhere between fittedStart and flatStart
// Find the last </section> before flatStart
var slice = h.slice(fittedStart, flatStart);
var lastSec = slice.lastIndexOf('</section>');
var fittedEnd = fittedStart + lastSec + '</section>'.length;
console.log('\nfitted-sheet end (relative offset):', lastSec, '  absolute:', fittedEnd);
console.log('flat-sheet start:', flatStart);
console.log('gap:', flatStart - fittedEnd, 'chars');
// That gap should be > 0 (means colors section is BETWEEN fittedEnd and flatStart? or not?)
var colorsStart = h.indexOf('<section class="gb-category-section" id="available-colors"');
console.log('\navailable-colors start:', colorsStart);
console.log('Is colors between fitted-end and flat-start?', fittedEnd < colorsStart && colorsStart < flatStart);