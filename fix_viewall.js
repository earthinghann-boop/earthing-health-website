var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// 1. Remove all "View All →" blocks (the whole .product-actions div)
h = h.replace(/<div class="product-actions">\s*<a[^>]+>View All →<\/a>\s*<\/div>\s*/g, '');
console.log('View All removed. Remaining:', (h.match(/View All/g) || []).length);

// 2. For each product-card, wrap .product-image .carousel inside an <a href="...">
// Pattern: find <div class="product-image">\n<div class="carousel" ...> and wrap both in <a>
var re = /(<div class="product-image">)\s*(\n<div class="carousel" id="([^"]+)")/g;
var replacements = 0;
h = h.replace(re, function(match, divOpen, carouselTag, cid) {
    // Find the corresponding href from the now-deleted View All
    // We need to capture href before removal — do a two-pass approach instead
    replacements++;
    return match;
});
console.log('product-image tags found:', replacements);

// Actually let's do it properly: find each product-card and rewrite the product-image div
var cards = h.split(/(?=<div class="product-card">)/);
console.log('Product cards:', cards.length - 1);

var newCards = [];
for (var i = 0; i < cards.length; i++) {
    var card = cards[i];
    // Skip the first element (before first card)
    if (!card.includes('<div class="product-card">')) {
        newCards.push(card);
        continue;
    }
    // Extract href from View All if any (already removed) — use href from original
    // Find carousel ID
    var cidMatch = card.match(/<div class="carousel" id="([^"]+)"/);
    if (!cidMatch) { newCards.push(card); continue; }
    var cid = cidMatch[1];
    // Find href for this card — need to look at original (before View All removal)
    // Alternative: extract href from the product card's own link context
    // Use a map of CID -> href based on naming convention
    var hrefMap = {
        'fittedCarousel':'earthing-fitted-sheet.html','flatCarousel':'groundingbedding.html',
        'pillowCarousel':'grounding-pillow-cases.html','duvetCarousel':'groundingbedding.html',
        'kidsCarousel':'groundingbedding.html',
        'puSheetCarousel':'pu-earthing-mat.html','puDeskCarousel':'pu-earthing-mat.html',
        'quiltCarousel':'grounding-mat.html','blanketCarousel':'grounding-blanket.html',
        'shawlCarousel':'emf-wearing.html','fishmanCarousel':'emf-wearing.html',
        'beanieCarousel':'emf-wearing.html','hoodCarousel':'emf-wearing.html',
        'capCarousel':'emf-wearing.html','curtainCarousel':'emf-wearing.html',
        'socksCarousel':'emf-wearing.html','eyeMaskCarousel':'emf-wearing.html',
        'sleeveCarousel':'emf-wearing.html','loungeCarousel':'emf-wearing.html',
        'boxerCarousel':'emf-wearing.html',
        'kitCordCarousel':'grounding-kit.html','kitPlugCarousel':'grounding-kit.html',
        'kitTesterCarousel':'grounding-kit.html'
    };
    var href = hrefMap[cid] || '#';
    // Wrap .product-image div contents with <a href>
    var newCard = card.replace(
        /(<div class="product-image">)\s*(\n<div class="carousel" id)/,
        '$1\n                            <a href="' + href + '">$2'
    );
    // Close the </a> after </div> </div> .product-image
    // Find the closing of .product-image div
    newCard = newCard.replace(
        /(\n                        <\/div>\s*<\/div>\s*\n                        <div class="product-info">)/,
        '\n                            </a>$1'
    );
    newCards.push(newCard);
}

var newH = newCards.join('');

// Verify
var viewalls = (newH.match(/View All/g) || []).length;
var openA = (newH.match(/<a href="[^"]+">\s*<div class="carousel"/g) || []).length;
var closeA = (newH.match(/<\/div>\s*<\/div>\s*<\/a>\s*\n                        <div class="product-info">/g) || []).length;
console.log('View All remaining:', viewalls);
console.log('Open <a> tags wrapping carousel:', openA);
console.log('Close </a> tags:', closeA);

fs.writeFileSync('index.html', newH, 'utf8');
console.log('Written. Size:', newH.length);