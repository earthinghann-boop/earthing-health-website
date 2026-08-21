var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

var tests = [
    ['capCarousel', 'emf-wearing.html#baseball_cap'],
    ['shawlCarousel', 'emf-wearing.html#shawl'],
    ['kitCordCarousel', 'grounding-kit.html#cord'],
    ['fittedCarousel', 'groundingbedding.html#fitted-sheet'],
    ['puSheetCarousel', 'pu-earthing-mat.html#pu-sheet'],
    ['quiltCarousel', 'grounding-mat.html#quilt-mat'],
    ['blanketCarousel', 'grounding-blanket.html#blanket']
];

var allPass = true;
tests.forEach(function(t) {
    var cid = t[0], expected = t[1];
    var cidx = h.indexOf('id="' + cid + '"');
    var nearA = h.lastIndexOf('<a href="', cidx);
    var actual = h.slice(nearA + 9, h.indexOf('"', nearA + 9));
    var pass = actual === expected;
    console.log((pass ? '✓' : '✗') + ' ' + cid + ': ' + actual);
    if (!pass) allPass = false;
});

console.log('\n' + (allPass ? 'All tests passed!' : 'Some tests failed'));

// Count total hrefs with #
var hashLinks = (h.match(/href="[^"]*#/g) || []).length;
console.log('Total links with anchors:', hashLinks);