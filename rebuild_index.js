var fs = require('fs');

// Load current index
var h = fs.readFileSync('index.html', 'utf8');

// Products section start/end
var secStart = h.indexOf('<section class="products" id="products">');
var pos = secStart; var depth = 0;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { var secEnd = pos; break; } }
}
var secLen = secEnd - secStart;
console.log('Products section: ' + secStart + '-' + secEnd + ', ' + secLen + ' chars');

// ── Carousel HTML builder (homepage goProductSlide_<id> naming) ──────────────
function makeCarousel(cid, imgs) {
    // imgs = [{src, alt}]
    var imgsHtml = '';
    imgs.forEach(function(img, i) {
        var cls = 'active';
        imgsHtml += '\n                                    <img src="' + img.src + '" alt="' + img.alt + '" class="carousel-img ' + cls + '">';
    });
    // Reset all except first to '' (active set above only for first)
    // Fix: set all to '' first, then first gets 'active'
    imgsHtml = '';
    imgs.forEach(function(img, i) {
        var cls = i === 0 ? 'carousel-img active' : 'carousel-img';
        imgsHtml += '\n                                    <img src="' + img.src + '" alt="' + img.alt + '" class="' + cls + '">';
    });

    var dotsHtml = '';
    imgs.forEach(function(img, i) {
        var cls = i === 0 ? 'dot active' : 'dot';
        dotsHtml += '\n                                    <span class="' + cls + '" onclick="goProductSlide_' + cid + '(' + i + ')"></span>';
    });

    return '\n                            <div class="carousel" id="' + cid + '">\n                                <div class="carousel-inner">' +
        imgsHtml +
        '\n                                </div>\n                                <button class="carousel-btn carousel-prev" onclick="moveProductSlide_' + cid + '(-1)">❮</button>\n                                <button class="carousel-btn carousel-next" onclick="moveProductSlide_' + cid + '(1)">❯</button>\n                                <div class="carousel-dots" id="' + cid + 'Dots">' +
        dotsHtml +
        '\n                                </div>\n                            </div>';
}

// ── Product Card builder ─────────────────────────────────────────────────────
function makeCard(cid, title, desc, imgs, href, features) {
    var featHtml = '';
    features.forEach(function(f) {
        featHtml += '\n                                    <li>' + f + '</li>';
    });
    return '\n                    <div class="product-card">\n                        <div class="product-image">' +
        makeCarousel(cid, imgs) +
        '\n                        </div>\n                        <div class="product-info">\n                            <h4>' + title + '</h4>\n                            <p class="product-desc">' + desc + '</p>\n                            <ul class="product-features">' +
        featHtml +
        '\n                            </ul>\n                            <div class="product-actions">\n                                <a href="' + href + '" class="btn btn-outline">View All →</a>\n                            </div>\n                        </div>\n                    </div>';
}

// ── 6 categories ────────────────────────────────────────────────────────────
var categories = [];

// Category 1: Grounding Bedding
categories.push({
    id: 'grounding-bedding',
    title: 'Grounding Bedding',
    href: 'groundingbedding.html',
    cards: [
        makeCard('beddingCarousel', 'Grounding Fitted Sheet',
            'The cornerstone of any grounding sleep system. Full-coverage mattress sheet with conductive silver fiber grid — stays firmly in place all night.',
            [
                {src: 'images/products/fitted_sheet/1.jpg', alt: 'Grounding Fitted Sheet'},
                {src: 'images/products/fitted_sheet/2.jpg', alt: 'Grounding Fitted Sheet'},
                {src: 'images/products/fitted_sheet/3.jpg', alt: 'Grounding Fitted Sheet'},
                {src: 'images/products/fitted_sheet/4.jpg', alt: 'Grounding Fitted Sheet'}
            ],
            'groundingbedding.html',
            ['Conductive silver fiber grid', 'Elastic skirt, all-night stay', 'Twin / Full / Queen / King sizes', 'Machine washable, durable'])
    ]
});

// Category 2: Grounding PU Leather
categories.push({
    id: 'grounding-pu-leather',
    title: 'Grounding PU Leather',
    href: 'pu-earthing-mat.html',
    cards: [
        makeCard('puCarousel', 'PU Sheet',
            'Premium PU leather top with built-in grounding grid. Combines the elegance of leather with full-body earthing connectivity.',
            [
                {src: 'images/products/pu_sheet/1.jpg', alt: 'PU Grounding Sheet'},
                {src: 'images/products/pu_sheet/2.jpg', alt: 'PU Grounding Sheet'},
                {src: 'images/products/pu_sheet/3.jpg', alt: 'PU Grounding Sheet'},
                {src: 'images/products/pu_sheet/4.jpg', alt: 'PU Grounding Sheet'}
            ],
            'pu-earthing-mat.html',
            ['PU leather + silver fiber grid', 'Non-slip base', 'Desk mat & full sheet options', 'OEM colors available'])
    ]
});

// Category 3: Grounding Quilt Mat
categories.push({
    id: 'grounding-quilt-mat',
    title: 'Grounding Quilt Mat',
    href: 'grounding-mat.html',
    cards: [
        makeCard('quiltCarousel', 'Quilted Grounding Mat',
            'Quilted sandwich construction with outer silver fiber fabric and inner conductive layer. Comfortable enough for daily use, effective enough for clinical results.',
            [
                {src: 'images/products/jia_mian_mat/1.jpg', alt: 'Quilted Grounding Mat'},
                {src: 'images/products/jia_mian_mat/2.jpg', alt: 'Quilted Grounding Mat'},
                {src: 'images/products/jia_mian_mat/3.jpg', alt: 'Quilted Grounding Mat'},
                {src: 'images/products/jia_mian_mat/4.jpg', alt: 'Quilted Grounding Mat'}
            ],
            'grounding-mat.html',
            ['Quilted 3-layer construction', 'Silver fiber outer + conductive inner', 'Foldable, portable', 'Multiple sizes available'])
    ]
});

// Category 4: RF Shielding Blanket
categories.push({
    id: 'emf-blanket',
    title: 'RF Shielding Blanket',
    href: 'grounding-blanket.html',
    cards: [
        makeCard('blanketCarousel', 'Grounding & RF Shielding Blanket',
            'Dual-action blanket: RF shielding layer blocks up to 99.99% of wireless radiation; grounding layer connects you to earth. Two sides, two functions.',
            [
                {src: 'images/products/emf_blanket/1.jpg', alt: 'RF Shielding Blanket'},
                {src: 'images/products/emf_blanket/2.jpg', alt: 'RF Shielding Blanket'},
                {src: 'images/products/emf_blanket/3.jpg', alt: 'RF Shielding Blanket'},
                {src: 'images/products/emf_blanket/4.jpg', alt: 'RF Shielding Blanket'}
            ],
            'grounding-blanket.html',
            ['Up to 63dB RF shielding (GJB 8820)', 'Grounding layer for earth connection', 'Adult & child sizes', 'Machine washable'])
    ]
});

// Category 5: RF Shielding Wearing
categories.push({
    id: 'emf-wearing',
    title: 'RF Shielding Wearing',
    href: 'emf-wearing.html',
    cards: [
        makeCard('shawlCarousel', 'RF Shielding Shawl',
            'Elegant draped shawl woven with silver fiber for everyday EMF protection. Style and safety in one.',
            [{src: 'images/products/shawl/1.jpg', alt: 'RF Shielding Shawl'}, {src: 'images/products/shawl/2.jpg', alt: 'RF Shielding Shawl'}, {src: 'images/products/shawl/3.jpg', alt: 'RF Shielding Shawl'}, {src: 'images/products/shawl/4.jpg', alt: 'RF Shielding Shawl'}],
            'emf-wearing.html', ['Up to 63dB RF shielding', 'Lightweight, breathable fabric', 'One size fits all', 'Antibacterial & grounding']),
        makeCard('beanieCarousel', 'RF Shielding Beanie',
            'Knitted beanie cap with embedded silver fiber. Keep your head shielded while on the go.',
            [{src: 'images/products/beanie/1.jpg', alt: 'RF Shielding Beanie'}, {src: 'images/products/beanie/2.jpg', alt: 'RF Shielding Beanie'}, {src: 'images/products/beanie/3.jpg', alt: 'RF Shielding Beanie'}, {src: 'images/products/beanie/4.jpg', alt: 'RF Shielding Beanie'}],
            'emf-wearing.html', ['Knitted silver fiber construction', 'Unisex, one size', 'Machine washable', 'RF blocking + grounding']),
        makeCard('socksCarousel', 'Antibacterial Grounding Socks',
            'Soft conductive socks that keep your feet grounded throughout the day. Tested for antibacterial performance by Intertek.',
            [{src: 'images/products/socks/1.jpg', alt: 'Grounding Socks'}, {src: 'images/products/socks/2.jpg', alt: 'Grounding Socks'}, {src: 'images/products/socks/3.jpg', alt: 'Grounding Socks'}, {src: 'images/products/socks/4.jpg', alt: 'Grounding Socks'}],
            'emf-wearing.html', ['Intertek A-class antibacterial', 'Conductive silver fiber', 'Multiple sizes', 'Machine washable']),
        makeCard('eyemaskCarousel', 'RF Shielding Eye Mask',
            'Sleep mask with RF shielding layer for EMF-free rest. Blocks wireless radiation while you sleep.',
            [{src: 'images/products/eye_mask/1.jpg', alt: 'RF Shielding Eye Mask'}, {src: 'images/products/eye_mask/2.jpg', alt: 'RF Shielding Eye Mask'}, {src: 'images/products/eye_mask/3.jpg', alt: 'RF Shielding Eye Mask'}],
            'emf-wearing.html', ['RF shielding layer', 'Soft memory foam', 'Light-blocking design', 'USB-C rechargeable']),
        makeCard('sleeveCarousel', 'RF Shielding Sleeve Shirt',
            'Long-sleeve shirt with silver fiber weave for full-arm EMF protection during desk work or travel.',
            [{src: 'images/products/sleeve_shirt/1.jpg', alt: 'RF Shielding Sleeve Shirt'}, {src: 'images/products/sleeve_shirt/2.jpg', alt: 'RF Shielding Sleeve Shirt'}, {src: 'images/products/sleeve_shirt/3.jpg', alt: 'RF Shielding Sleeve Shirt'}, {src: 'images/products/sleeve_shirt/4.jpg', alt: 'RF Shielding Sleeve Shirt'}],
            'emf-wearing.html', ['Silver fiber long-sleeve', 'Breathable fabric', 'Multiple sizes S-3XL', 'RF blocking + grounding']),
        makeCard('loungeCarousel', 'RF Shielding Loungewear',
            'Comfortable loungewear set with integrated silver fiber for all-day grounding at home.',
            [{src: 'images/products/loungewear/1.jpg', alt: 'RF Shielding Loungewear'}, {src: 'images/products/loungewear/2.jpg', alt: 'RF Shielding Loungewear'}, {src: 'images/products/loungewear/3.jpg', alt: 'RF Shielding Loungewear'}, {src: 'images/products/loungewear/4.jpg', alt: 'RF Shielding Loungewear'}],
            'emf-wearing.html', ['Silver fiber loungewear set', 'Relaxed comfortable fit', 'Multiple sizes', 'Antibacterial & grounding'])
    ]
});

// Category 6: Accessories
categories.push({
    id: 'accessories',
    title: 'Accessories',
    href: 'grounding-kit.html',
    cards: [
        makeCard('kitCarousel', 'Grounding Cord',
            'The connection lifeline for your grounding system. Second-generation smart cord with built-in safety valve — 6 variants for every application.',
            [
                {src: 'images/products/kit_cord/1.jpg', alt: 'Grounding Cord Gen 2'},
                {src: 'images/products/kit_cord/2.jpg', alt: 'Grounding Cord 2-in-1'},
                {src: 'images/products/kit_cord/3.jpg', alt: 'Grounding Cord Rod'},
                {src: 'images/products/kit_cord/4.jpg', alt: 'Grounding Cord Snake'},
                {src: 'images/products/kit_cord/5.jpg', alt: 'Grounding Cord Golden'},
                {src: 'images/products/kit_cord/6.jpg', alt: 'Grounding Cord Dual-Head'}
            ],
            'grounding-kit.html',
            ['6 variants: Gen 2 / 2-in-1 / Rod / Snake / Golden / Dual-Head', 'Built-in current-limiting protection', '10m / 20m outdoor rod versions', 'OEM length customization'])
    ]
});

// ── Assemble section HTML ─────────────────────────────────────────────────────
var sectionHtml = '\n    <section class="products" id="products">\n        <div class="container">\n            <div class="section-header">\n                <span class="section-label">Our Products</span>\n                <h2 class="section-title">Grounding Solutions for <br>Every Aspect of Life</h2>\n                <div class="section-cta">\n                    <a href="get-price.html" class="btn btn-primary">Get Wholesale Quote</a>\n                </div>\n            </div>\n';

categories.forEach(function(cat) {
    var cardsHtml = cat.cards.join('\n');
    sectionHtml += '\n            <div class="product-category" id="' + cat.id + '">\n                <div class="category-header">\n                    <h3 class="category-title">' + cat.title + '</h3>\n                    <a href="' + cat.href + '" class="category-viewall">View All →</a>\n                </div>\n                <div class="products-grid">\n' + cardsHtml + '\n                </div>\n            </div>\n';
});

sectionHtml += '\n        </div>\n    </section>\n';

// Replace old section
var newH = h.slice(0, secStart) + sectionHtml + h.slice(secEnd);

fs.writeFileSync('index.html', newH, 'utf8');
console.log('\nDone. New size:', newH.length, '(was', h.length, ', delta:', newH.length - h.length + ')');

// Count cards
var cardCount = (newH.match(/class="product-card"/g) || []).length;
console.log('Product cards total:', cardCount);
// Count carousels
var carouselCount = (newH.match(/class="carousel" id="/g) || []).length;
console.log('Carousels total:', carouselCount);
// Count dot handlers
var dotCount = (newH.match(/onclick="goProductSlide_/g) || []).length;
console.log('Dot handlers total:', dotCount);