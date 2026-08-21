var fs = require('fs');
var h = fs.readFileSync('C:/Users/18574/.qclaw/workspace/earthinghealth-website/grounding-kit.html', 'utf8');
console.log('Size:', h.length);

// Find nav
var navStart = h.indexOf('<nav class="navbar"');
console.log('nav start:', navStart);

// Find footer
var footerStart = h.indexOf('<footer');
console.log('footer start:', footerStart);

// Existing categories
console.log('\nH2/H3 headings:');
var re = /<(h1|h2|h3)[^>]*>([^<]+)</g;
var m;
while ((m = re.exec(h)) !== null) {
    console.log('  <' + m[1] + '> ' + m[2]);
}