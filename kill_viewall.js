var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Remove category-viewall links
h = h.replace(/<a href="[^"]*" class="category-viewall">View All →<\/a>/g, '');
var remaining = (h.match(/View All/g) || []).length;
console.log('View All remaining:', remaining);
fs.writeFileSync('index.html', h, 'utf8');
console.log('Done. Size:', h.length);