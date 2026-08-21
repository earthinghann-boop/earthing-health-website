var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
// Find structure between hero and footer
var heroEnd = h.indexOf('<!-- ');
var footerStart = h.indexOf('<footer');
var mid = h.slice(heroEnd !== -1 ? heroEnd : 0, footerStart);
console.log('=== Mid section (between hero and footer) ===');
console.log(mid.length, 'chars');
// Print all section headers
var re = /<section[^>]*class="gb-category-section"[^>]*>[\s\S]*?<h3[^>]*>([^<]+)</g;
var m;
var idx = 0;
while ((m = re.exec(mid)) !== null) {
    idx++;
    var start = m.index;
    // Find close tag
    var depth = 0;
    var pos = start;
    while (pos < mid.length) {
        var o = mid.indexOf('<section', pos);
        var c = mid.indexOf('</section>', pos);
        if (c < 0) break;
        if (0 <= o && o < c) { depth++; pos = o + 8; }
        else { depth--; pos = c + 10; if (depth === 0) break; }
    }
    var nextSec = mid.indexOf('<section', pos);
    var lastEnd = nextSec !== -1 ? nextSec : mid.length;
    var chunk = mid.slice(start, lastEnd).slice(0, 200);
    console.log('\n--- Section ' + idx + ':', m[1], '---');
    console.log('chars:', lastEnd - start);
    console.log(chunk.replace(/\n/g, ' ').slice(0, 200));
}