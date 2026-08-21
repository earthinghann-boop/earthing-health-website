var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Find all goProductSlide_ with 2+ args
var re = /goProductSlide_(\w+)\(([^)]+)\)/g;
var m;
while ((m = re.exec(h)) !== null) {
    var args = m[2].split(',');
    if (args.length > 1) {
        console.log('BUGGY at ' + m.index + ': ' + m[0]);
    }
}
// Also find moveProductSlide with 2 args
var re2 = /moveProductSlide_(\w+)\(([^)]+)\)/g;
while ((m = re2.exec(h)) !== null) {
    console.log('move at ' + m.index + ': ' + m[0]);
}
// Check for any onclick in the HTML section (between secStart 6967 and secEnd... well after)
var scriptOpen = h.indexOf('<script>');
var htmlPart = h.slice(6967, scriptOpen);
// Find remaining buggy patterns
var buggyHtml = (htmlPart.match(/goProductSlide_\w+\([^,]+,/g) || []);
console.log('\nBuggy in HTML section:', buggyHtml.length);
buggyHtml.forEach(function(b) { console.log('  ' + b); });