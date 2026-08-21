var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');

// Find all top-level gb-category-sections by depth-counting from hero
var heroClose = h.indexOf('</section>', h.indexOf('collection-hero'));
console.log('Hero ends at:', heroClose);

// Walk through, print each section h2 and its start/end
var pos = heroClose;
var depth = 0;
var sections = [];
var i = 0;
while (pos < h.length && i < 20) {
    var o = h.indexOf('<section', pos);
    var c = h.indexOf('</section>', pos);
    if (c === -1) break;
    if (o !== -1 && o < c) { depth++; pos = o + 8; }
    else {
        depth--; pos = c + 10;
        if (depth === 0) {
            var chunk = h.slice(o, pos);
            var h2 = (chunk.match(/<h2[^>]*>([^<]+)</) || ['',''])[1];
            sections.push({ start: o, end: pos, h2: h2, len: pos - o });
            if (chunk.indexOf('<footer') !== -1) break;
        }
    }
    i++;
}

console.log('\nTop-level sections order:');
sections.forEach(function(s, i) {
    console.log((i+1) + '. [' + s.start + '-' + s.end + '] len=' + s.len + ' "' + s.h2 + '"');
});
console.log('\nTotal:', sections.length);

// Expected: Hero -> Fitted Sheet -> Available Colors -> Flat Sheet -> Pillow Case -> Duvet Cover -> Kids Bedding
var names = sections.map(function(s) { return s.h2; });
var expected = ['Grounding Fitted Sheet', 'Available Colors', 'Grounding Flat Sheet',
                'Grounding Pillow Case', 'Grounding Duvet Cover', "Kid's Grounding Bedding"];
var ok = JSON.stringify(names) === JSON.stringify(expected);
console.log('\nOrder correct:', ok);
if (!ok) {
    console.log('Expected:', expected);
    console.log('Got:     ', names);
}