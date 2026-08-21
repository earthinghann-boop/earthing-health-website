var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
var idx = 0;
var count = 0;
while ((idx = h.indexOf('id="available-colors"', idx + 1)) !== -1) {
    count++;
    console.log('occurrence #' + count + ' at byte ' + idx);
}
console.log('Total:', count);