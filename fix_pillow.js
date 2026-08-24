var fs = require('fs');

// 1. Add anchor to grounding-pillow-cases.html section 2
var h = fs.readFileSync('grounding-pillow-cases.html', 'utf8');

// Find the second <section> (the one with "Designed for Daily Grounding Comfort")
var firstSec = h.indexOf('<section');
var secondSec = h.indexOf('<section', firstSec + 8);
if (secondSec === -1) {
    console.log('Second section not found');
    process.exit(1);
}

// Check if already has id
var tagEnd = h.indexOf('>', secondSec);
var openTag = h.slice(secondSec, tagEnd + 1);
if (openTag.indexOf('id=') !== -1) {
    console.log('Second section already has id:', openTag.match(/id="([^"]+)"/)[1]);
} else {
    // Add id="pillow-case"
    var newOpenTag = openTag.replace('<section', '<section id="pillow-case"');
    h = h.slice(0, secondSec) + newOpenTag + h.slice(tagEnd + 1);
    fs.writeFileSync('grounding-pillow-cases.html', h, 'utf8');
    console.log('Added id="pillow-case" to second section');
}

// 2. Update index.html pillowCarousel link
var idx = fs.readFileSync('index.html', 'utf8');
var re = /<a href="[^"]*"><div class="carousel" id="pillowCarousel"/g;
var matches = idx.match(re);
if (matches) {
    idx = idx.replace(re, '<a href="grounding-pillow-cases.html#pillow-case"><div class="carousel" id="pillowCarousel"');
    fs.writeFileSync('index.html', idx, 'utf8');
    console.log('Updated pillowCarousel href to grounding-pillow-cases.html#pillow-case');
} else {
    console.log('pillowCarousel link not found or already updated');
}

// Verify
var verify = fs.readFileSync('index.html', 'utf8');
var cidx = verify.indexOf('id="pillowCarousel"');
var nearA = verify.lastIndexOf('<a href="', cidx);
var finalHref = verify.slice(nearA + 9, verify.indexOf('"', nearA + 9));
console.log('\nFinal pillowCarousel href:', finalHref);