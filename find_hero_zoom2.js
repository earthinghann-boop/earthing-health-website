var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
var styleEnd = h.indexOf('<script>');
var style = h.slice(0, styleEnd);
// Find the hero section
var heroSecIdx = style.indexOf('.hero');
console.log('.hero at:', heroSecIdx, ':', style.slice(heroSecIdx, heroSecIdx + 400));
console.log('\n---\n');
// Search for scale
var scaleIdx = style.indexOf('scale');
if (scaleIdx !== -1) console.log('scale at:', scaleIdx, ':', style.slice(Math.max(0, scaleIdx - 50), scaleIdx + 100));
else console.log('No scale in CSS');
// Search for overflow:hidden near product-image or product-card
var ovIdx = style.indexOf('overflow');
var ov = [];
while (ovIdx !== -1) { ov.push(ovIdx + ': ' + style.slice(ovIdx, ovIdx + 50)); ovIdx = style.indexOf('overflow', ovIdx + 1); }
console.log('\noverflow refs:', ov.slice(0, 5));
// Find product-image CSS
var piIdx = style.indexOf('.product-image');
if (piIdx !== -1) console.log('\n.product-image:', style.slice(piIdx, piIdx + 300));
// Find .carousel or .carousel-img CSS
var ciIdx = style.indexOf('.carousel-img');
if (ciIdx !== -1) console.log('\n.carousel-img:', style.slice(ciIdx, ciIdx + 200));
var caIdx = style.indexOf('.carousel');
if (caIdx !== -1) console.log('\n.carousel:', style.slice(caIdx, caIdx + 200));