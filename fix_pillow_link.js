var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Update pillowCarousel to use groundingbedding.html#pillow-case
var re = /<a href="[^"]*"><div class="carousel" id="pillowCarousel"/g;
var matches = h.match(re);
if (matches) {
    h = h.replace(re, '<a href="groundingbedding.html#pillow-case"><div class="carousel" id="pillowCarousel"');
    fs.writeFileSync('index.html', h, 'utf8');
    console.log('Updated pillowCarousel to groundingbedding.html#pillow-case');
} else {
    console.log('pillowCarousel not found or already updated');
}

// Verify
var verify = fs.readFileSync('index.html', 'utf8');
var cidx = verify.indexOf('id="pillowCarousel"');
var nearA = verify.lastIndexOf('<a href="', cidx);
var finalHref = verify.slice(nearA + 9, verify.indexOf('"', nearA + 9));
console.log('Final href:', finalHref);