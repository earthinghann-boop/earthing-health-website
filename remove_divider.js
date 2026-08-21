var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');

// Find section-divider block (and the blank lines / comments around it)
var openTag = '<section class="section-divider">';
var openIdx = h.indexOf(openTag);
console.log('divider opens at:', openIdx);
if (openIdx === -1) { console.log('ERROR: divider not found'); process.exit(1); }

// Find close with depth-count
var pos = openIdx; var depth = 0;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { var closeIdx = pos; break; } }
}
console.log('divider closes at:', closeIdx);

// Find preceding blank lines + optional comment to remove
// Look back for the most recent newline before closeIdx, then check what comes before
// Strategy: trim blank lines between kids-bedding close and divider open, and between divider close and available-colors
var beforeDivStart = openIdx;
// Find start of line containing openTag
var lastNL = h.lastIndexOf('\n', beforeDivStart - 1);
var trimStart = lastNL + 1;  // start of the line that contains <section class="section-divider">
console.log('trim start:', trimStart);

// Look at content before trimStart
console.log('Before divider line (50 chars):', JSON.stringify(h.slice(trimStart - 50, trimStart)));
console.log('Around divider close (100 chars):', JSON.stringify(h.slice(closeIdx, closeIdx + 100)));

// Simple approach: remove exactly from <section ... </section> for divider, and trim surrounding blank lines.
// Leave the blank-line structure between kids-bedding and divider, between divider and available-colors clean.
// Just remove the divider section itself plus one set of leading newlines.
var newH = h.slice(0, trimStart) + h.slice(closeIdx);
fs.writeFileSync('groundingbedding.html', newH, 'utf8');
console.log('New size:', newH.length, '  removed:', h.length - newH.length);

// Verify
var colorsAfterKids = (function() {
    var kidsIdx = newH.indexOf('<section class="gb-category-section" id="kids-bedding"');
    var colorsIdx = newH.indexOf('<section class="gb-category-section" id="available-colors"');
    return kidsIdx !== -1 && colorsIdx !== -1 && kidsIdx < colorsIdx;
})();
console.log('kids < colors:', colorsAfterKids);
console.log('Divider still present:', newH.indexOf('section-divider') !== -1);
console.log('Grounding sleep quote present:', newH.indexOf('Grounding sleep isn') !== -1);