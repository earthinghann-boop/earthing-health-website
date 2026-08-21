var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// CID → href#anchor map (for products with anchors on their detail pages)
var hrefMap = {
    // Grounding Bedding - all go to groundingbedding.html (no anchors yet)
    'fittedCarousel':'earthing-fitted-sheet.html',
    'flatCarousel':'groundingbedding.html',
    'pillowCarousel':'grounding-pillow-cases.html',
    'duvetCarousel':'groundingbedding.html',
    'kidsCarousel':'groundingbedding.html',
    // PU Leather
    'puSheetCarousel':'pu-earthing-mat.html',
    'puDeskCarousel':'pu-earthing-mat.html',
    // Quilt Mat
    'quiltCarousel':'grounding-mat.html',
    // RF Blanket
    'blanketCarousel':'grounding-blanket.html',
    // RF Wearing - all with anchors
    'shawlCarousel':'emf-wearing.html#shawl',
    'fishmanCarousel':'emf-wearing.html#fishman_cap',
    'beanieCarousel':'emf-wearing.html#beanie',
    'hoodCarousel':'emf-wearing.html#hood',
    'capCarousel':'emf-wearing.html#baseball_cap',
    'curtainCarousel':'emf-wearing.html#curtain',
    'socksCarousel':'emf-wearing.html#socks',
    'eyeMaskCarousel':'emf-wearing.html#eye_mask',
    'sleeveCarousel':'emf-wearing.html#sleeve_shirt',
    'loungeCarousel':'emf-wearing.html#loungewear',
    'boxerCarousel':'emf-wearing.html#boxer',
    // Accessories
    'kitCordCarousel':'grounding-kit.html',
    'kitPlugCarousel':'grounding-kit.html',
    'kitTesterCarousel':'grounding-kit.html'
};

// Replace each href in <a href="..."><div class="carousel"
var count = 0;
for (var cid in hrefMap) {
    var href = hrefMap[cid];
    // Pattern: <a href="OLD"><div class="carousel" id="CID"
    var re = new RegExp('<a href="[^"]*"><div class="carousel" id="' + cid + '"', 'g');
    var matches = h.match(re);
    if (matches) {
        h = h.replace(re, '<a href="' + href + '"><div class="carousel" id="' + cid + '"');
        count += matches.length;
        console.log(cid + ' -> ' + href + ' (' + matches.length + ' replaced)');
    }
}

fs.writeFileSync('index.html', h, 'utf8');
console.log('\nTotal replacements:', count);

// Verify
var verify = ['capCarousel','shawlCarousel','kitCordCarousel'];
verify.forEach(function(cid) {
    var idx = h.indexOf('id="' + cid + '"');
    var nearA = h.lastIndexOf('<a href="', idx);
    var href = h.slice(nearA + 9, h.indexOf('"', nearA + 9));
    console.log(cid + ' final href: ' + href);
});