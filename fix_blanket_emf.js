var fs = require('fs');
var h = fs.readFileSync('grounding-blanket.html', 'utf8');
var emfCount = (h.match(/EMF/g) || []).length;
console.log('EMF count:', emfCount);

var idx = h.indexOf('EMF');
while (idx !== -1) {
    console.log('@' + idx + ': ' + JSON.stringify(h.slice(Math.max(0, idx - 40), idx + 60)));
    idx = h.indexOf('EMF', idx + 1);
}
