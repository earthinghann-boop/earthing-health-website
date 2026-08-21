var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
var lines = h.split('\n');
lines.forEach(function(line, i) {
    if (line.indexOf('View All') !== -1) {
        console.log('Line ' + (i+1) + ': ' + line.trim().slice(0, 120));
    }
});