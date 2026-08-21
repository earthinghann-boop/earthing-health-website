var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// ── 1. Inject zoom CSS ────────────────────────────────────────────────────────
var styleEnd = h.indexOf('</style>');
var zoomCSS = '\n\n/* Homepage product image zoom on hover */\n' +
    '.product-image { overflow: hidden; cursor: pointer; }\n' +
    '.product-image .carousel-img { transition: transform 0.5s ease !important; }\n' +
    '.product-image:hover .carousel-img.active { transform: scale(1.05); }\n' +
    '.product-image a { display: block; overflow: hidden; }\n';
h = h.slice(0, styleEnd) + zoomCSS + h.slice(styleEnd);

// ── 2. Remove View All blocks ─────────────────────────────────────────────────
h = h.replace(/<div class="product-actions">\s*<a[^>]*>View All →<\/a>\s*<\/div>\s*/g, '');

// ── 3. Build CID → href map ────────────────────────────────────────────────────
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

// ── 4. Wrap each .carousel in <a href> using depth-count parsing ─────────────
function findClosingDiv(html, start) {
    var depth = 0;
    var pos = start;
    while (pos < html.length) {
        var o = html.indexOf('<div', pos);
        var c = html.indexOf('</div>', pos);
        if (c === -1) break;
        if (o !== -1 && o < c) { depth++; pos = o + 4; }
        else { depth--; if (depth === 0) return c + 6; pos = c + 6; }
    }
    return -1;
}

function findClosingAnchor(html, start) {
    var pos = start;
    while (pos < html.length) {
        var a = html.indexOf('<a ', pos);
        var c = html.indexOf('</a>', pos);
        if (c === -1) break;
        if (a !== -1 && a < c) { pos = a + 3; }
        else { return c + 4; }
    }
    return -1;
}

var newH = '';
var pos = 0;
while (true) {
    // Find next <div class="product-image">
    var imgDivStart = h.indexOf('<div class="product-image">', pos);
    if (imgDivStart === -1) { newH += h.slice(pos); break; }
    
    newH += h.slice(pos, imgDivStart);
    
    // Find the carousel div inside
    var carouselStart = h.indexOf('<div class="carousel" id="', imgDivStart);
    if (carouselStart === -1 || carouselStart > imgDivStart + 300) {
        // No carousel found, just copy as-is
        newH += h.slice(imgDivStart, h.indexOf('</div>', imgDivStart) + 6);
        pos = h.indexOf('</div>', imgDivStart) + 6;
        continue;
    }
    
    // Extract carousel ID
    var cidMatch = h.slice(carouselStart).match(/<div class="carousel" id="([^"]+)"/);
    var cid = cidMatch ? cidMatch[1] : null;
    var href = hrefMap[cid] || '#';
    
    // Find inner carousel content (find matching </div> for the carousel div itself)
    var carouselDivStart = h.indexOf('<div class="carousel"', carouselStart);
    var carouselDivEnd = findClosingDiv(h, carouselDivStart);
    
    // Find the closing of .product-image div
    var prodImgClose = findClosingDiv(h, imgDivStart);
    
    // Build: <div class="product-image"><a href="..."><div class="carousel"...>...</div></a></div>
    // Then product-info follows
    var beforeInfo = h.slice(imgDivStart, carouselDivStart);
    var carouselBlock = h.slice(carouselDivStart, carouselDivEnd);
    // Find </div></div> after carousel before product-info
    var afterCarousel = h.slice(carouselDivEnd, prodImgClose);
    var afterProdImg = h.slice(prodImgClose, prodImgClose + 50);
    
    // Rebuild: wrap carousel in <a>
    newH += beforeInfo + '<a href="' + href + '">' + carouselBlock + '</a>' + afterCarousel;
    
    pos = prodImgClose;
}

fs.writeFileSync('index.html', newH, 'utf8');
console.log('Done. New size:', newH.length);

// ── Verify ─────────────────────────────────────────────────────────────────────
var viewalls = (newH.match(/View All/g) || []).length;
var openA = (newH.match(/<a href="[^"]+"><div class="carousel"/g) || []).length;
var imgZoom = newH.indexOf('.product-image:hover') !== -1;
console.log('View All remaining:', viewalls);
console.log('Carousels wrapped in <a>:', openA, '(expect 23)');
console.log('Image zoom CSS injected:', imgZoom);