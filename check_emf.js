var fs = require('fs');
var h = fs.readFileSync('emf-wearing.html', 'utf8');
// Find all sections with h3 or h4 titles
var re = /<h[34][^>]*>([^<]+)<\/h[34]>/g;
var m;
var titles = [];
while ((m = re.exec(h)) !== null) {
    titles.push(m[1].trim());
}
console.log('Found', titles.length, 'titles:');
titles.forEach(function(t, i) {
    console.log((i+1) + '. ' + t);
});
// Check if any section has id
var idRe = /<section[^>]*id="([^"]+)"/g;
var ids = [];
while ((m = idRe.exec(h)) !== null) ids.push(m[1]);
console.log('\nSection IDs:', ids.length ? ids.join(', ') : 'none');