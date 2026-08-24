var fs = require('fs');
var h = fs.readFileSync('grounding-pillow-cases.html', 'utf8');

// Find all sections and their content
var sections = [];
var re = /<section[^>]*>/g;
var m;
while ((m = re.exec(h)) !== null) {
    var start = m.index;
    var tagEnd = h.indexOf('>', start);
    var openTag = h.slice(start, tagEnd + 1);
    
    // Find closing
    var depth = 0;
    var pos = start;
    while (pos < h.length) {
        var o = h.indexOf('<section', pos);
        var c = h.indexOf('</section>', pos);
        if (c === -1) break;
        if (o !== -1 && o < c) { depth++; pos = o + 8; }
        else { depth--; if (depth === 0) { var end = c + 10; break; } pos = c + 10; }
    }
    
    var content = h.slice(start, end);
    // Find h2/h3 in this section
    var hMatch = content.match(/<h[23][^>]*>([^<]+)<\/h[23]>/);
    var title = hMatch ? hMatch[1].trim() : '(no title)';
    
    sections.push({
        id: openTag.match(/id="([^"]+)"/) ? openTag.match(/id="([^"]+)"/)[1] : '(no id)',
        title: title,
        size: content.length
    });
}

console.log('Sections in grounding-pillow-cases.html:');
sections.forEach(function(s, i) {
    console.log((i+1) + '. id=' + s.id + ' | title=' + s.title + ' | size=' + s.size);
});