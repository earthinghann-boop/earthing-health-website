var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
var re = /goProductSlide_\w+\([\s\S]*?\)/g;
var m;
while ((m = re.exec(h)) !== null) {
    var s = m[0];
    if (s.match(/,/)) console.log(s.slice(0, 100));
}