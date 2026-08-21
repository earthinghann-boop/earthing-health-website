var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
var secStart = 6967;
var secEnd = 51753;
console.log('Section length:', secEnd - secStart);
console.log('After section:');
console.log(JSON.stringify(h.slice(secEnd - 20, secEnd + 60)));
// Confirm section text
console.log('Section start text:', JSON.stringify(h.slice(secStart, secStart + 60)));
// Confirm tech section starts here
var techStart = h.indexOf('<section class="technology" id="technology">');
console.log('Tech section at:', techStart);