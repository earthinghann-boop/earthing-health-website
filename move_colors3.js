var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');

// 1. Extract available-colors section
var acPat = '<section class="gb-category-section" id="available-colors"';
var acStart = h.indexOf(acPat);
if (acStart === -1) { console.log('ERROR: colors not found'); process.exit(1); }
var pos = acStart; var depth = 0;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) { console.log('ERROR: no close'); process.exit(1); }
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { var acEnd = pos; break; } }
}
var colorsSection = h.slice(acStart, acEnd);
console.log('colors section: ' + colorsSection.length + ' chars');

// 2. Find insertion point: end of last product section (kids-bedding)
// Look for the </section> that closes kids-bedding, before any final CTA or footer
var kidsStart = h.indexOf('<section class="gb-category-section" id="kids-bedding"');
console.log('kids-bedding starts at:', kidsStart);
var slice = h.slice(kidsStart);
// Find last </section> in that slice (it's the kids-bedding close)
var lastSec = slice.lastIndexOf('</section>');
var kidsCloseAbs = kidsStart + lastSec + '</section>'.length;
console.log('kids-bedding closes at:', kidsCloseAbs);

// 3. Remove from current position
var withoutColors = h.slice(0, acStart) + h.slice(acEnd);
console.log('withoutColors length:', withoutColors.length);

// 4. Insert after kids-bedding
var newH = withoutColors.slice(0, kidsCloseAbs) + '\n' + colorsSection + withoutColors.slice(kidsCloseAbs);
console.log('newH length:', newH.length, '  delta:', newH.length - h.length);

// 5. Verify
var positions = [
    ['id="fitted-sheet"', 'Fitted'],
    ['id="flat-sheet"', 'Flat'],
    ['id="pillow-case"', 'Pillow'],
    ['id="duvet-cover"', 'Duvet'],
    ['id="kids-bedding"', 'Kids'],
    ['id="available-colors"', 'Colors']
];
console.log('\nSection order:');
positions.forEach(function(p) {
    var idx = newH.indexOf('<section class="gb-category-section" ' + p[0]);
    console.log('  ' + p[1] + ': ' + idx);
});
var inOrder = true;
var idxs = positions.map(function(p) { return newH.indexOf('<section class="gb-category-section" ' + p[0]); });
for (var i = 0; i < idxs.length - 1; i++) {
    if (idxs[i] > idxs[i+1]) inOrder = false;
}
console.log('\nCorrect order:', inOrder);

fs.writeFileSync('groundingbedding.html', newH, 'utf8');
console.log('Written.');