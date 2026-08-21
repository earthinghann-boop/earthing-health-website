var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
var kidsStart = h.indexOf('<section class="gb-category-section" id="kids-bedding"');
// Walk through entire file from kidsStart to find all </section>
var pos = kidsStart;
var secCount = 0;
var lastSecEnd = -1;
while (pos < h.length) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { secCount++; pos = o + 8; }
    else { secCount--; pos = c + 10; if (secCount === 0) { lastSecEnd = pos; break; } }
}
console.log('kids-bedding section ends at byte:', lastSecEnd);
console.log('Content right after (first 300 chars):');
console.log(h.slice(lastSecEnd, lastSecEnd + 300));
console.log('\nLooking for: footer / closing of section before footer');
var footerIdx = h.indexOf('<footer', lastSecEnd);
console.log('footer starts at:', footerIdx);