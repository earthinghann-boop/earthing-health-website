var fs = require('fs');
var h = fs.readFileSync('grounding-blanket.html', 'utf8');
h = h.split('>EMF Blanket<').join('>RF Shielding Blanket<');
h = h.split('>EMF Wearing<').join('>RF Shielding Wearing<');
fs.writeFileSync('grounding-blanket.html', h, 'utf8');
var emfLeft = (h.match(/EMF/g) || []).length;
console.log('EMF remaining:', emfLeft);
console.log('RF count:', (h.match(/RF/g) || []).length);
