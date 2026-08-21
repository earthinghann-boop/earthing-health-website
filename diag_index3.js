var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Find <script> blocks
var scripts = [];
var pos = 0;
while (true) {
    var o = h.indexOf('<script>', pos);
    if (o === -1) break;
    var c = h.indexOf('</script>', o);
    if (c === -1) break;
    scripts.push({start: o, end: c, content: h.slice(o, c + 9)});
    pos = c + 9;
}
console.log('Script blocks found:', scripts.length);
scripts.forEach(function(s, i) {
    console.log('\n--- Script ' + i + ' (' + s.start + '-' + s.end + ', ' + (s.end - s.start) + ' chars) ---');
    console.log(s.content.slice(0, 600));
});