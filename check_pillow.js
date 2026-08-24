var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Find pillowCarousel href
var cidx = h.indexOf('id="pillowCarousel"');
var nearA = h.lastIndexOf('<a href="', cidx);
var href = h.slice(nearA + 9, h.indexOf('"', nearA + 9));
console.log('pillowCarousel href:', href);

// Check if grounding-pillow-cases.html has anchors
try {
    var ph = fs.readFileSync('grounding-pillow-cases.html', 'utf8');
    var ids = [];
    var re = /<section[^>]*id="([^"]+)"/g;
    var m;
    while ((m = re.exec(ph)) !== null) ids.push(m[1]);
    console.log('grounding-pillow-cases.html anchors:', ids.length ? ids.join(', ') : 'NO ANCHORS');
    
    // Check titles
    var titles = [];
    var tre = /<h[34][^>]*>([^<]+)<\/h[34]>/g;
    while ((m = tre.exec(ph)) !== null) titles.push(m[1].trim());
    console.log('First 5 titles:', titles.slice(0, 5).join(' | '));
} catch(e) {
    console.log('grounding-pillow-cases.html: FILE NOT FOUND');
}