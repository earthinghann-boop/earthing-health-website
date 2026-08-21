var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
// Show the bytes around divider section close
var dividerIdx = h.indexOf('<section class="section-divider">');
console.log('divider section opens at:', dividerIdx);
var slice = h.slice(dividerIdx, dividerIdx + 500);
console.log('---');
console.log(JSON.stringify(slice));
console.log('---');