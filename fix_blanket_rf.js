var fs = require('fs');
var h = fs.readFileSync('grounding-blanket.html', 'utf8');
var orig = h;

var replacements = [
    // Meta
    ['<title>Grounding & EMF Blanket - Conductive Silver Fiber | Earthing Health</title>',
     '<title>Grounding & RF Shielding Blanket - Conductive Silver Fiber | Earthing Health</title>'],
    ['Wholesale EMF shielding and grounding blanket manufacturer',
     'Wholesale RF shielding and grounding blanket manufacturer'],
    ['Silver fiber technology for EMF protection and natural grounding',
     'Silver fiber technology for RF blocking and natural grounding'],
    // Hero h1
    ['<h1>Grounding & EMF Blanket</h1>',
     '<h1>Grounding & RF Shielding Blanket</h1>'],
    // Hero subtitle
    ['Conductive silver fiber blanket for EMF shielding and natural grounding',
     'Conductive silver fiber blanket for RF shielding and natural grounding'],
    // Hero badge
    ['<span class="hero-badge">EMF Shielding</span>',
     '<span class="hero-badge">RF Shielding</span>'],
    // Section comment
    ['<!-- EMF Shielding -->',
     '<!-- RF Shielding -->'],
    // Section h3
    ['<h3>EMF Shielding</h3>',
     '<h3>RF Shielding</h3>'],
    // Body "Our EMF shielding blanket"
    ['Our EMF shielding blanket uses high-conductivity silver fiber to',
     'Our RF shielding blanket uses high-conductivity silver fiber to'],
    // Alt tags
    ['alt="EMF Shielding Blanket"',
     'alt="RF Shielding Blanket"'],
    ['alt="EMF Shielding Blanket Detail"',
     'alt="RF Shielding Blanket Detail"'],
    ['alt="EMF Shielding Blanket Texture"',
     'alt="RF Shielding Blanket Texture"'],
    ['alt="EMF Shielding Blanket Side"',
     'alt="RF Shielding Blanket Side"'],
    // Bottom tagline
    ['and EMF protection.',
     'and RF protection.'],
];

replacements.forEach(function(r) {
    var n = (h.match(new RegExp(r[0].replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g')) || []).length;
    if (n > 0) {
        h = h.split(r[0]).join(r[1]);
        console.log('Replaced (' + n + 'x): ' + r[0].slice(0, 60));
    } else {
        console.log('NOT FOUND: ' + r[0].slice(0, 60));
    }
});

fs.writeFileSync('grounding-blanket.html', h, 'utf8');

var emfLeft = (h.match(/EMF/g) || []).length;
console.log('\nEMF remaining:', emfLeft);
console.log('RF count:', (h.match(/RF/g) || []).length);
console.log('Changed chars:', h.length - orig.length);
