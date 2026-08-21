var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Confirm: goProductSlide with TWO args (buggy) should be 0
var buggyTwoArgs = (h.match(/goProductSlide_\w+\([^,]+,/g) || []).length;
console.log('goProductSlide with 2 args (buggy):', buggyTwoArgs, '(expect 0)');
// Confirm: goProductSlide with 1 arg (correct dot)
var correctDot = (h.match(/onclick="goProductSlide_\w+\(\d+\)"/g) || []).length;
console.log('Correct dot onclicks:', correctDot);
// Confirm: moveProductSlide with 1 arg (correct button)
var correctBtn = (h.match(/onclick="moveProductSlide_\w+\(-?\d+\)"/g) || []).length;
console.log('Correct button onclicks:', correctBtn);
// Confirm goProductSlide_ functions exist in script
var funcs = (h.match(/function goProductSlide_\w+\(/g) || []).length;
console.log('goProductSlide functions defined:', funcs, '(expect 11)');
// File size
console.log('File size:', h.length);
// Product cards
var cards = (h.match(/class="product-card"/g) || []).length;
console.log('Product cards:', cards, '(expect 11)');
// Sections
var cats = (h.match(/product-category"/g) || []).length;
console.log('Product categories:', cats, '(expect 6)');
// View all links
var viewalls = (h.match(/category-viewall/g) || []).length;
console.log('View All links:', viewalls, '(expect 6)');