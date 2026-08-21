var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Update kit links to use anchors
var updates = [
    ['kitCordCarousel', 'grounding-kit.html#cord'],
    ['kitPlugCarousel', 'grounding-kit.html#plug'],
    ['kitTesterCarousel', 'grounding-kit.html#tester']
];

updates.forEach(function(u) {
    var cid = u[0], href = u[1];
    var re = new RegExp('<a href="[^"]*"><div class="carousel" id="' + cid + '"', 'g');
    var matches = h.match(re);
    if (matches) {
        h = h.replace(re, '<a href="' + href + '"><div class="carousel" id="' + cid + '"');
        console.log(cid + ' -> ' + href + ' (' + matches.length + ' replaced)');
    } else {
        console.log(cid + ': no match found (already updated?)');
    }
});

fs.writeFileSync('index.html', h, 'utf8');
console.log('Done');