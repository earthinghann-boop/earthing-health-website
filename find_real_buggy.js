var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
var re = /goProductSlide_(\w+)\(([^)]+)\)/g;
var m;
while ((m = re.exec(h)) !== null) {
    var args = m[2].split(',');
    if (args.length > 1) {
        console.log('2-arg at ' + m.index + ': ' + m[0]);
    }
}
// Also check moveProductSlide
var re2 = /moveProductSlide_(\w+)\(([^)]+)\)/g;
while ((m = re2.exec(h)) !== null) {
    var args = m[2].split(',');
    if (args.length > 1) {
        console.log('move 2-arg at ' + m.index + ': ' + m[0]);
    }
}