var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// ── Find products section boundaries ──────────────────────────────────────────
var secStart = h.indexOf('<section class="products" id="products">');
var pos = secStart; var depth = 0;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { var secEnd = pos; break; } }
}
console.log('Products section: ' + secStart + '-' + secEnd + ', len=' + (secEnd - secStart));

// ── Helpers ───────────────────────────────────────────────────────────────────
function img3(dir, alt) {
    return [
        {src: 'images/products/' + dir + '/1.jpg', alt: alt},
        {src: 'images/products/' + dir + '/2.jpg', alt: alt},
        {src: 'images/products/' + dir + '/3.jpg', alt: alt}
    ];
}
function makeCarousel(cid, imgs) {
    var dotsHtml = '';
    for (var i = 0; i < imgs.length; i++) {
        var cls = i === 0 ? 'dot active' : 'dot';
        dotsHtml += '\n                                    <span class="' + cls + '" onclick="goProductSlide_' + cid + '(' + i + ')"></span>';
    }
    var imgsHtml = '';
    imgs.forEach(function(img, i) {
        var cls = i === 0 ? 'carousel-img active' : 'carousel-img';
        imgsHtml += '\n                                    <img src="' + img.src + '" alt="' + img.alt + '" class="' + cls + '">';
    });
    return '\n                            <div class="carousel" id="' + cid + '">\n                                <div class="carousel-inner">' +
        imgsHtml +
        '\n                                </div>\n                                <div class="carousel-dots" id="' + cid + 'Dots">' +
        dotsHtml +
        '\n                                </div>\n                            </div>';
}
function makeCard(cid, title, imgs, href) {
    return '\n                    <div class="product-card">\n                        <div class="product-image">' +
        makeCarousel(cid, imgs) +
        '\n                        </div>\n                        <div class="product-info">\n                            <h4>' + title + '</h4>\n                            <div class="product-actions">\n                                <a href="' + href + '" class="btn btn-outline">View All →</a>\n                            </div>\n                        </div>\n                    </div>';
}
function makeCategory(id, title, href, cardsHtml) {
    return '\n            <div class="product-category" id="' + id + '">\n                <div class="category-header">\n                    <h3 class="category-title">' + title + '</h3>\n                    <a href="' + href + '" class="category-viewall">View All →</a>\n                </div>\n                <div class="products-grid">' +
        cardsHtml +
        '\n                </div>\n            </div>';
}

// ── All categories ────────────────────────────────────────────────────────────
// Grounding Bedding
var bedding = makeCategory('grounding-bedding', 'Grounding Bedding', 'groundingbedding.html',
    makeCard('fittedCarousel',  'Grounding Fitted Sheet',  img3('fitted_sheet',  'Grounding Fitted Sheet'),  'grounding-fitted-sheet.html') +
    makeCard('flatCarousel',    'Grounding Flat Sheet',    img3('flat_sheet',    'Grounding Flat Sheet'),    'groundingbedding.html') +
    makeCard('pillowCarousel',  'Grounding Pillow Case',  img3('pillow_case',   'Grounding Pillow Case'),   'grounding-pillow-cases.html') +
    makeCard('duvetCarousel',   'Grounding Duvet Cover',  img3('duvet_cover',  'Grounding Duvet Cover'),   'groundingbedding.html') +
    makeCard('kidsCarousel',    "Kid's Grounding Bedding", img3('kids_bedding', "Kid's Grounding Bedding"), 'groundingbedding.html')
);

// PU Leather
var pu = makeCategory('grounding-pu-leather', 'Grounding PU Leather', 'pu-earthing-mat.html',
    makeCard('puSheetCarousel',   'PU Sheet',       img3('pu_sheet',     'PU Grounding Sheet'),  'pu-earthing-mat.html') +
    makeCard('puDeskCarousel',    'PU Desk Mat',    img3('pu_desk_mat',  'PU Desk Mat'),         'pu-earthing-mat.html')
);

// Quilt Mat — NO bullet list, just title + CTA
var quiltCard = '\n                    <div class="product-card">\n                        <div class="product-image">' +
    makeCarousel('quiltCarousel', [
        {src: 'images/products/jia_mian_mat/1.jpg', alt: 'Quilted Grounding Mat'},
        {src: 'images/products/jia_mian_mat/2.jpg', alt: 'Quilted Grounding Mat'},
        {src: 'images/products/jia_mian_mat/3.jpg', alt: 'Quilted Grounding Mat'}
    ]) +
    '\n                        </div>\n                        <div class="product-info">\n                            <h4>Quilted Grounding Mat</h4>\n                            <div class="product-actions">\n                                <a href="grounding-mat.html" class="btn btn-outline">View All →</a>\n                            </div>\n                        </div>\n                    </div>';
var quilt = makeCategory('grounding-quilt-mat', 'Grounding Quilt Mat', 'grounding-mat.html', quiltCard);

// RF Blanket
var rfBlanket = makeCategory('emf-blanket', 'RF Shielding Blanket', 'grounding-blanket.html',
    makeCard('blanketCarousel', 'Grounding & RF Shielding Blanket', img3('emf_blanket', 'RF Shielding Blanket'), 'grounding-blanket.html')
);

// RF Wearing — 11 types
var rfWearing = makeCategory('emf-wearing', 'RF Shielding Wearing', 'emf-wearing.html',
    makeCard('shawlCarousel',    'RF Shielding Shawl',         img3('shawl',        'RF Shielding Shawl'),         'emf-wearing.html') +
    makeCard('fishmanCarousel',   'RF Shielding Fishman Cap',   img3('fishman_cap',  'RF Shielding Fishman Cap'),   'emf-wearing.html') +
    makeCard('beanieCarousel',    'RF Shielding Beanie',        img3('beanie',       'RF Shielding Beanie'),        'emf-wearing.html') +
    makeCard('hoodCarousel',      'RF Shielding Hood',         img3('hood',         'RF Shielding Hood'),          'emf-wearing.html') +
    makeCard('capCarousel',       'RF Shielding Baseball Cap', img3('baseball_cap', 'RF Shielding Baseball Cap'), 'emf-wearing.html') +
    makeCard('curtainCarousel',   'RF Shielding Curtain',      img3('curtain',      'RF Shielding Curtain'),       'emf-wearing.html') +
    makeCard('socksCarousel',     'Antibacterial Grounding Socks', img3('socks',    'Grounding Socks'),            'emf-wearing.html') +
    makeCard('eyeMaskCarousel',   'RF Shielding Eye Mask',     img3('eye_mask',     'RF Shielding Eye Mask'),      'emf-wearing.html') +
    makeCard('sleeveCarousel',    'RF Shielding Sleeve Shirt', img3('sleeve_shirt','RF Shielding Sleeve Shirt'),  'emf-wearing.html') +
    makeCard('loungeCarousel',    'RF Shielding Loungewear',   img3('loungewear',   'RF Shielding Loungewear'),   'emf-wearing.html') +
    makeCard('boxerCarousel',     'RF Shielding Boxer Shorts', img3('boxer',        'RF Shielding Boxer Shorts'),  'emf-wearing.html')
);

// Accessories — 3 groups
var accessories = makeCategory('accessories', 'Accessories', 'grounding-kit.html',
    makeCard('kitCordCarousel',   'Grounding Cord',   img3('kit_cord',   'Grounding Cord'),   'grounding-kit.html') +
    makeCard('kitPlugCarousel',   'Grounding Plug',   img3('kit_plug',   'Grounding Plug'),   'grounding-kit.html') +
    makeCard('kitTesterCarousel', 'Conductive Tester', img3('kit_tester', 'Conductive Tester'), 'grounding-kit.html')
);

// ── Assemble section ─────────────────────────────────────────────────────────
var sectionHtml = '\n    <section class="products" id="products">\n        <div class="container">\n            <div class="section-header">\n                <span class="section-label">Our Products</span>\n                <h2 class="section-title">Grounding Solutions for <br>Every Aspect of Life</h2>\n                <div class="section-cta">\n                    <a href="get-price.html" class="btn btn-primary">Get Wholesale Quote</a>\n                </div>\n            </div>\n' +
    bedding + pu + quilt + rfBlanket + rfWearing + accessories +
    '\n        </div>\n    </section>\n';

var newH = h.slice(0, secStart) + sectionHtml + h.slice(secEnd);
fs.writeFileSync('index.html', newH, 'utf8');
console.log('Done. New size:', newH.length);

// ── Verify ────────────────────────────────────────────────────────────────────
var cards = (newH.match(/class="product-card"/g) || []).length;
var cats  = (newH.match(/product-category/g) || []).length;
var dots  = (newH.match(/onclick="goProductSlide_/g) || []).length;
var carousels = (newH.match(/class="carousel" id="/g) || []).length;
console.log('Categories:', cats, '| Cards:', cards, '| Carousels:', carousels, '| Dots:', dots);
// bullet check
var bullets = (newH.match(/product-features/g) || []).length;
console.log('Bullet lists remaining (should be 0):', bullets);