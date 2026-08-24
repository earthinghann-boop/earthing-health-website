var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
var ids = [];
var re = /<section[^>]*id="([^"]+)"/g;
var m;
while ((m = re.exec(h)) !== null) ids.push(m[1]);
console.log('groundingbedding.html anchors:', ids.join(', '));

// Check if pillow-case exists
if (ids.indexOf('pillow-case') === -1) {
    console.log('MISSING: pillow-case anchor');
} else {
    console.log('FOUND: pillow-case anchor');
}