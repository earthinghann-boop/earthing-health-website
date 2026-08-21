var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
console.log('Total size:', h.length);

// Find "Our Products" section
var re = /our.products/gi;
var m;
while ((m = re.exec(h)) !== null) {
    console.log('"our products" at byte', m.index);
}

// Find <section ...products...> blocks
var secRe = /<section[^>]*class="[^"]*products?[^"]*"[^>]*>/gi;
while ((m = secRe.exec(h)) !== null) {
    console.log('Section class containing "product": at byte', m.index, 'tag:', m[0]);
}

// Find h2/h3 with "Products"
var re2 = /<(h1|h2|h3)[^>]*>([^<]*[Pp]roducts?[^<]*)</g;
while ((m = re2.exec(h)) !== null) {
    console.log('Header tag <' + m[1] + '>:', JSON.stringify(m[2]));
}

// Find Products dropdown from nav
var navPos = h.indexOf('<nav class="navbar"');
var footerPos = h.indexOf('<footer');
var slice = h.slice(navPos, footerPos);
var dropPos = slice.indexOf('Products');
console.log('\nNav "Products" first occurrence in nav:', dropPos);