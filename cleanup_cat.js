var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Remove .category-viewall CSS (no longer used)
h = h.replace(/\.category-viewall[^}]*\{[^}]*\}/g, '');
// Clean empty .category-header wrappers (just h3 remains)
// Replace <div class="category-header"><h3 ...>View All</h3></div> with just <h3>
h = h.replace(/<div class="category-header">\s*(<h3 class="category-title">)/g, '$1');
h = h.replace(/(<\/h3>)\s*<\/div>\s*(?=\s*<div class="products-grid")/g, '$1');
// Clean up orphaned .category-header
h = h.replace(/<div class="category-header">\s*<\/div>/g, '');

fs.writeFileSync('index.html', h, 'utf8');
console.log('Done. Size:', h.length);
// Final checks
var viewalls = (h.match(/View All/g) || []).length;
var catViewalls = (h.match(/category-viewall/g) || []).length;
var carouselsA = (h.match(/<a href="[^"]+"><div class="carousel"/g) || []).length;
var imgZoom = h.indexOf('.product-image:hover') !== -1;
var cards = (h.match(/class="product-card"/g) || []).length;
console.log('View All:', viewalls, '| category-viewall:', catViewalls);
console.log('Carousels in <a>:', carouselsA, '(expect 23)');
console.log('Image zoom CSS:', imgZoom);
console.log('Product cards:', cards, '(expect 23)');