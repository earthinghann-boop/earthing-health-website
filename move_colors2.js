var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');

// ── 1. Extract available-colors section (full tag + content) ──────────────────
var acPat = '<section class="gb-category-section" id="available-colors"';
var acStart = h.indexOf(acPat);
if (acStart === -1) { console.log('ERROR: available-colors not found'); process.exit(1); }

// Find closing tag using depth count
var pos = acStart; var depth = 0;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) { console.log('ERROR: no closing tag found'); process.exit(1); }
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else { depth--; pos = c + 10; if (depth === 0) { var acEnd = pos; break; } }
}
var colorsSection = h.slice(acStart, acEnd);
console.log('colorsSection length:', colorsSection.length);

// ── 2. Find fitted-sheet section closing position ────────────────────────────
// Fitted ends where flat-sheet begins (both are top-level siblings under hero)
// Look for the literal sequence: </section>\n    <section class="gb-category-section" id="flat-sheet"
var fittedCloseIdx = h.indexOf('</section>\n    <section class="gb-category-section" id="flat-sheet"');
console.log('fittedCloseIdx:', fittedCloseIdx);
if (fittedCloseIdx === -1) {
    // Try without newline
    fittedCloseIdx = h.indexOf('</section>\r\n    <section class="gb-category-section" id="flat-sheet"');
    console.log('with CR:', fittedCloseIdx);
}
if (fittedCloseIdx === -1) {
    // Fallback: find last </section> before flat-sheet start tag
    var flatTagStart = h.indexOf('<section class="gb-category-section" id="flat-sheet"');
    console.log('flat-sheet tag at:', flatTagStart);
    var slice = h.slice(0, flatTagStart);
    fittedCloseIdx = slice.lastIndexOf('</section>');
    console.log('fallback fittedCloseIdx:', fittedCloseIdx);
}
var insertAfter = fittedCloseIdx + '</section>'.length;  // right after </section>

// ── 3. Remove from current position ──────────────────────────────────────────
var withoutColors = h.slice(0, acStart) + h.slice(acEnd);
console.log('withoutColors length:', withoutColors.length);

// ── 4. Insert after fitted-sheet closes ─────────────────────────────────────
var newH = withoutColors.slice(0, insertAfter) + '\n' + colorsSection + withoutColors.slice(insertAfter);
console.log('newH length:', newH.length, '(was', h.length, ', delta:', newH.length - h.length + ')');

// ── 5. Verify ───────────────────────────────────────────────────────────────
var fittedS = newH.indexOf('<section class="gb-category-section" id="fitted-sheet"');
var flatS = newH.indexOf('<section class="gb-category-section" id="flat-sheet"');
var colorsS = newH.indexOf('<section class="gb-category-section" id="available-colors"');
console.log('\nfitted-sheet starts:  ', fittedS);
console.log('available-colors starts:', colorsS);
console.log('flat-sheet starts:     ', flatS);
console.log('Order correct (fitted < colors < flat):', fittedS < colorsS && colorsS < flatS);

fs.writeFileSync('groundingbedding.html', newH, 'utf8');
console.log('\nFile written.');