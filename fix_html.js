var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// ── Remove wrongly placed CSS (after </style> tag that doesn't exist) ───────────
var zoomStart = h.indexOf('\n\n/* Homepage product image zoom on hover */');
var zoomEnd = h.indexOf('\n</style>');
if (zoomEnd === -1) zoomEnd = h.length;
if (zoomStart !== -1) {
    console.log('Removing misplaced zoom CSS bytes', zoomStart, '-', zoomEnd);
    h = h.slice(0, zoomStart) + h.slice(zoomEnd);
    console.log('Zoom CSS text removed. New size:', h.length);
}

// ── CID → href map ─────────────────────────────────────────────────────────────
var hrefMap = {
    'fittedCarousel':'earthing-fitted-sheet.html',
    'flatCarousel':'groundingbedding.html',
    'pillowCarousel':'grounding-pillow-cases.html',
    'duvetCarousel':'groundingbedding.html',
    'kidsCarousel':'groundingbedding.html',
    'puSheetCarousel':'pu-earthing-mat.html',
    'puDeskCarousel':'pu-earthing-mat.html',
    'quiltCarousel':'grounding-mat.html',
    'blanketCarousel':'grounding-blanket.html',
    'shawlCarousel':'emf-wearing.html',
    'fishmanCarousel':'emf-wearing.html',
    'beanieCarousel':'emf-wearing.html',
    'hoodCarousel':'emf-wearing.html',
    'capCarousel':'emf-wearing.html',
    'curtainCarousel':'emf-wearing.html',
    'socksCarousel':'emf-wearing.html',
    'eyeMaskCarousel':'emf-wearing.html',
    'sleeveCarousel':'emf-wearing.html',
    'loungeCarousel':'emf-wearing.html',
    'boxerCarousel':'emf-wearing.html',
    'kitCordCarousel':'grounding-kit.html',
    'kitPlugCarousel':'grounding-kit.html',
    'kitTesterCarousel':'grounding-kit.html'
};

// ── Depth-aware div closer ─────────────────────────────────────────────────────
function findClosingDiv(html, start) {
    var depth = 0, pos = start;
    while (pos < html.length) {
        var o = html.indexOf('<div', pos);
        var c = html.indexOf('</div>', pos);
        if (c === -1) break;
        if (o !== -1 && o < c) { depth++; pos = o + 4; }
        else { depth--; if (depth === 0) return c + 6; pos = c + 6; }
    }
    return -1;
}

// ── Rewrite product-image sections ─────────────────────────────────────────────
// Strategy: find each product-image div, extract carousel, wrap in <a>
// Pattern: <div class="product-image">\n<div class="carousel" id="XXX">...<div class="carousel">...</div>...</div>\n</div>
//         <div class="product-info">...
// Need to:  <div class="product-image">\n<a href="XXX">\n<div class="carousel" id="XXX">...</div>\n</a></div>
//         <div class="product-info">...

var result = '';
var pos = 0;
var count = 0;

while (true) {
    var imgDivStart = h.indexOf('<div class="product-image">', pos);
    if (imgDivStart === -1) { result += h.slice(pos); break; }
    
    result += h.slice(pos, imgDivStart);
    
    // Find carousel div inside this product-image
    var carouselDivStart = h.indexOf('<div class="carousel"', imgDivStart);
    if (carouselDivStart === -1 || carouselDivStart > imgDivStart + 200) {
        // No carousel, copy as-is
        var fallClose = findClosingDiv(h, imgDivStart);
        result += h.slice(imgDivStart, fallClose);
        pos = fallClose;
        continue;
    }
    
    // Get carousel ID
    var cidMatch = h.slice(carouselDivStart).match(/<div class="carousel" id="([^"]+)"/);
    var cid = cidMatch ? cidMatch[1] : '';
    var href = hrefMap[cid] || '#';
    
    // Find carousel div boundaries
    var carDivStart = h.indexOf('<div class="carousel"', carouselDivStart);
    var carDivEnd = findClosingDiv(h, carDivStart);
    
    // Find product-image div boundaries
    var prodImgEnd = findClosingDiv(h, imgDivStart);
    
    // Extract pieces
    var openDiv = h.slice(imgDivStart, carouselDivStart);  // <div class="product-image"> + whitespace
    var carousel = h.slice(carDivStart, carDivEnd);        // <div class="carousel">...</div>
    var afterCarousel = h.slice(carDivEnd, prodImgEnd);    // whatever between carousel close and product-image close
    
    // Rebuild: wrap carousel in <a href>
    result += openDiv + '<a href="' + href + '">' + carousel + '</a>' + afterCarousel;
    
    pos = prodImgEnd;
    count++;
}

fs.writeFileSync('index.html', result, 'utf8');
console.log('Done. Cards processed:', count, '| Size:', result.length);

// Verify
var zoomText = result.indexOf('\n\n/* Homepage product image zoom on hover */');
console.log('Zoom text in file:', zoomText !== -1 ? 'YES (still present, wrong place)' : 'NO (removed - good)');
var aWrapped = (result.match(/<a href="[^"]+"><div class="carousel"/g) || []).length;
console.log('Carousels wrapped in <a>:', aWrapped, '(expect 23)');
var hrefs = (result.match(/<a href=""><div/g) || []).length;
console.log('Empty href carousels:', hrefs, '(expect 0)');
var viewalls = (result.match(/View All/g) || []).length;
console.log('View All remaining:', viewalls, '(expect 0)');