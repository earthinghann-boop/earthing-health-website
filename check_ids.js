var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Check which carousel IDs exist in HTML vs in JS
var re = /class="carousel" id="([^"]+)"/g;
var htmlIds = [];
var m;
while ((m = re.exec(h)) !== null) htmlIds.push(m[1]);
console.log('HTML carousel IDs (' + htmlIds.length + '):', htmlIds.join(', '));

// Check goProductSlide_ functions in script
var scriptStart = h.indexOf('<script>');
var scriptEnd = h.lastIndexOf('</script>');
var script = h.slice(scriptStart, scriptEnd + 9);
var funcRe = /function goProductSlide_(\w+)\(/g;
var jsIds = [];
while ((m = funcRe.exec(script)) !== null) jsIds.push(m[1]);
console.log('\nJS goProductSlide functions (' + jsIds.length + '):', jsIds.join(', '));

// Missing
var missing = htmlIds.filter(function(id) { return jsIds.indexOf(id) === -1; });
console.log('\nMissing functions:', missing.length ? missing.join(', ') : 'none');