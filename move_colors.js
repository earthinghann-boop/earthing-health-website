var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');

// Find available-colors section (start and end)
var colorsStart = h.indexOf('<section class="gb-category-section" id="available-colors"');
console.log('colorsStart:', colorsStart);
if (colorsStart === -1) { console.log('ERROR: colors section not found'); process.exit(1); }

// Find its closing tag (depth-count)
var depth = 0, pos = colorsStart, colorsEnd = -1;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { colorsEnd = pos; break; } }
}
console.log('colorsEnd:', colorsEnd);
var colorsSection = h.slice(colorsStart, colorsEnd);

// Find fitted-sheet section closing tag
var fittedStart = h.indexOf('<section class="gb-category-section" id="fitted-sheet"');
console.log('fittedStart:', fittedStart);
depth = 0; pos = fittedStart; var fittedEnd = -1;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { fittedEnd = pos; break; } }
}
console.log('fittedEnd:', fittedEnd);

// Remove from current position
var withoutColors = h.slice(0, colorsStart) + h.slice(colorsEnd);

// Insert after fitted-sheet section
var newH = withoutColors.slice(0, fittedEnd) + '\n' + colorsSection + withoutColors.slice(fittedEnd);

fs.writeFileSync('groundingbedding.html', newH, 'utf8');
console.log('\nMoved. New size:', newH.length, '(was', h.length, ', delta:', newH.length - h.length + ')');

// Verify: available-colors should now come after fitted-sheet
var newFitted = newH.indexOf('<section class="gb-category-section" id="fitted-sheet"');
var newColors = newH.indexOf('<section class="gb-category-section" id="available-colors"');
var newFlat = newH.indexOf('<section class="gb-category-section" id="flat-sheet"');
console.log('\nfitted-sheet start:', newFitted);
console.log('available-colors start:', newColors);
console.log('flat-sheet start:', newFlat);
console.log('Order correct (fitted < colors < flat):', newFitted < newColors && newColors < newFlat);