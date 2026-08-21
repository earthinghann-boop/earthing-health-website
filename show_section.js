var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Show the products section (6967 onwards)
var start = h.indexOf('<section class="products" id="products">');
var slice = h.slice(start, start + 6000);
var lines = slice.split('\n');
console.log('First 100 lines of section:');
for (var i = 0; i < Math.min(lines.length, 100); i++) {
    console.log((i + 1).toString().padStart(3) + ': ' + lines[i].slice(0, 120));
}