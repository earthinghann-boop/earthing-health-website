var fs = require('fs');
var files = ['groundingbedding.html','pu-earthing-mat.html','grounding-mat.html','grounding-blanket.html','grounding-kit.html'];
files.forEach(function(f) {
    try {
        var h = fs.readFileSync(f, 'utf8');
        var ids = [];
        var re = /<section[^>]*id="([^"]+)"/g;
        var m;
        while ((m = re.exec(h)) !== null) ids.push(m[1]);
        console.log(f + ': ' + (ids.length ? ids.join(', ') : 'NO ANCHORS'));
    } catch(e) {
        console.log(f + ': FILE NOT FOUND');
    }
});