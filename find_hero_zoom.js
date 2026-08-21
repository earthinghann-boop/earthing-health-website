var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Find hero section CSS
var heroIdx = h.indexOf('Grounded in Nature');
console.log('Hero phrase at:', heroIdx);
// Find surrounding CSS
var styleEnd = h.indexOf('<script>');
var style = h.slice(0, styleEnd);
// Find transform scale CSS
var scaleRe = /transform.*scale/gi;
var m;
while ((m = scaleRe.exec(style)) !== null) {
    console.log('transform:scale at byte', m.index, ':', h.slice(Math.max(0, m.index - 150), m.index + 100));
}