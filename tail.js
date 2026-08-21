var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
console.log('Last 1000 chars:');
console.log('---');
console.log(h.slice(h.length - 1000));