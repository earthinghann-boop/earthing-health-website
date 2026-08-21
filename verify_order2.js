var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
var fEnd = h.lastIndexOf('</section>', h.indexOf('id="flat-sheet"'));
console.log('Fitted ends at:', fEnd, '  (+10 =', fEnd + 10, ')');
var colorsStart = h.indexOf('id="available-colors"');
var flatStart = h.indexOf('id="flat-sheet"');
console.log('Colors starts at:', colorsStart, '  Flat starts at:', flatStart);
console.log('Order (fittedEnd+10 < colors < flat):', fEnd + 10 < colorsStart, colorsStart < flatStart);
console.log('All correct?', (fEnd + 10 < colorsStart) && (colorsStart < flatStart));