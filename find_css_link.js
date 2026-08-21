var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Find all <link rel="stylesheet"> in head
var linkRe = /<link[^>]+href="([^"]+)"[^>]*>/g;
var m;
while ((m = linkRe.exec(h)) !== null) console.log('Link:', m[0]);
// Find all <style> blocks
var pos = 0; var count = 0;
while (true) {
    var o = h.indexOf('<style', pos);
    if (o === -1) break;
    var c = h.indexOf('</style>', o);
    count++;
    console.log('Style block #' + count + ': byte ' + o + '-' + c + ', ' + (c - o) + ' chars');
    pos = c + 8;
}
console.log('Total style blocks:', count);
// Find scale anywhere in file
var scaleIdx = h.indexOf('scale(');
if (scaleIdx !== -1) console.log('\nscale() at byte', scaleIdx, ':', h.slice(Math.max(0, scaleIdx - 100), scaleIdx + 150));
else console.log('\nNo scale() in index.html');