var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
// Show what comes after kids-bedding end
var kidsStart = h.indexOf('<section class="gb-category-section" id="kids-bedding"');
var slice = h.slice(kidsStart, kidsStart + 2500);
var lines = slice.split('\n');
for (var i = 0; i < Math.min(lines.length, 60); i++) {
    console.log((i+1).toString().padStart(3) + ': ' + lines[i].slice(0, 120));
}