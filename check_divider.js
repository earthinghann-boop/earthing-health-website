var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
var idx = 0; var count = 0;
while ((idx = h.indexOf('section-divider', idx + 1)) !== -1) {
    count++;
    console.log('occurrence #' + count + ' at byte ' + idx + ': ' + h.slice(Math.max(0, idx - 30), idx + 60));
}
console.log('Total section-divider:', count);
console.log('Divider Quote comment:', h.indexOf('Divider Quote') !== -1);
console.log('Grounding sleep isn:', h.indexOf('Grounding sleep isn') !== -1);