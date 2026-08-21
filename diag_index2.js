var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
console.log('Size:', h.length);

// Find the products section and its end
var secStart = h.indexOf('<section class="products" id="products">');
console.log('Products section starts at:', secStart);
var pos = secStart;
var depth = 0;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { var secEnd = pos; break; } }
}
console.log('Products section ends at:', secEnd, '  length:', secEnd - secStart);

// What's right after it?
console.log('\nAfter products section:');
console.log(h.slice(secEnd, secEnd + 300));

// Find all product-category divs (these are the 6 categories)
var catRe = /<div class="product-category" id="([^"]+)">/g;
var m;
var cats = [];
while ((m = catRe.exec(h)) !== null) {
    cats.push({id: m[1], idx: m.index});
}
console.log('\nProduct categories:');
cats.forEach(function(c) { console.log('  -', c.id, 'at byte', c.idx); });