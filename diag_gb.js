var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
console.log('Size:', h.length, 'chars');
console.log('Total gb-category-section:', (h.match(/class="gb-category-section"/g) || []).length);

// H3 titles
var re = /<h3[^>]*>([^<]+)</g;
var m;
console.log('\nH3 sections:');
while ((m = re.exec(h)) !== null) {
    console.log('  -', m[1]);
}

// IDs
console.log('\nIDs in page:');
var re2 = /id="([^"]+)"/g;
while ((m = re2.exec(h)) !== null) {
    if (m[1].startsWith('gb')) console.log('  -', m[1]);
}

// Check if silveryes002.jpg exists
var srcPath = 'C:/Users/18574/Desktop/EARTHING/silveryes网站/silveryes002.jpg';
var fs2 = require('fs');
if (fs2.existsSync(srcPath)) {
    var sz = fs2.statSync(srcPath).size;
    console.log('\nsilveryes002.jpg:', sz.toLocaleString(), 'b');
} else {
    console.log('\nsilveryes002.jpg: NOT FOUND');
    // List similar
    var dir = 'C:/Users/18574/Desktop/EARTHING/silveryes网站';
    if (fs2.existsSync(dir)) {
        fs2.readdirSync(dir).forEach(function(f) {
            if (/silveryes/i.test(f)) console.log('  found:', f);
        });
    }
}