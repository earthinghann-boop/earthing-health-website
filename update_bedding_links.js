var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Update bedding links to use anchors
var updates = [
    ['fittedCarousel', 'groundingbedding.html#fitted-sheet'],
    ['flatCarousel', 'groundingbedding.html#flat-sheet'],
    ['pillowCarousel', 'grounding-pillow-cases.html'], // pillow has its own page
    ['duvetCarousel', 'groundingbedding.html#duvet-cover'],
    ['kidsCarousel', 'groundingbedding.html#kids-bedding']
];

updates.forEach(function(u) {
    var cid = u[0], href = u[1];
    var re = new RegExp('<a href="[^"]*"><div class="carousel" id="' + cid + '"', 'g');
    var matches = h.match(re);
    if (matches) {
        h = h.replace(re, '<a href="' + href + '"><div class="carousel" id="' + cid + '"');
        console.log(cid + ' -> ' + href + ' (' + matches.length + ' replaced)');
    } else {
        console.log(cid + ': no match');
    }
});

fs.writeFileSync('index.html', h, 'utf8');
console.log('Done');