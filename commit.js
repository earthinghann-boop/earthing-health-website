var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
var re = /goProductSlide_\w+\([\s\S]*?\)/g;
var m, count = 0, lines = h.split('\n');
lines.forEach(function(line, i) {
    var matches = line.match(/goProductSlide_\w+\([\s\S]*?\)/g) || [];
    matches.forEach(function(m) {
        if (m.match(/,/)) { count++; console.log('Line ' + (i+1) + ': ' + m.slice(0, 120)); }
    });
});
console.log('Total 2-arg in lines:', count);