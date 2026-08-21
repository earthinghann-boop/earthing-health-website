var fs = require('fs');
var h = fs.readFileSync('grounding-kit.html', 'utf8');
var ids = [];
var re = /<section[^>]*id="([^"]+)"/g;
var m;
while ((m = re.exec(h)) !== null) ids.push(m[1]);
console.log('Kit anchors:', ids.join(', '));

var titles = [];
var tre = /<h[34][^>]*>([^<]+)<\/h[34]>/g;
while ((m = tre.exec(h)) !== null) titles.push(m[1].trim());
console.log('First 6 titles:', titles.slice(0, 6).join(' | '));