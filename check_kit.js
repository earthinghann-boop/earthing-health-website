var fs = require('fs');
var h = fs.readFileSync('grounding-kit.html', 'utf8');
var idx = h.indexOf('<h1>');
console.log('h1:', JSON.stringify(h.slice(idx, idx + 100)));
console.log('title:', h.match(/<title>([^<]+)</)[1]);
console.log('Grounding Kit count:', (h.match(/Grounding Kit/g) || []).length);
console.log('Grounding Accessories count:', (h.match(/Grounding Accessories/g) || []).length);