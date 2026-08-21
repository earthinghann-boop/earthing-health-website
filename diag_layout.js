var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
// Find kids-bedding end and what comes after
var kidsStart = h.indexOf('<section class="gb-category-section" id="kids-bedding"');
var slice = h.slice(kidsStart, kidsStart + 3500);
// Print structure with line numbers
var lines = slice.split('\n');
for (var i = 0; i < Math.min(lines.length, 80); i++) {
    console.log((i+1).toString().padStart(3) + ': ' + lines[i].slice(0, 100));
}