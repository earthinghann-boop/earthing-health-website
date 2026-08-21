var fs = require('fs');
var h = fs.readFileSync('grounding-kit.html', 'utf8');
var orig = h;

// Plug section update: alts and content
var plugAlts = [
    ['alt="EU Plug + New US Cord"', 'alt="EU Plug"'],
    ['alt="AU Plug + New US Cord"', 'alt="AU Plug"'],
    ['alt="UK Plug + New US Cord"', 'alt="UK Plug"'],
    ['alt="ITY Plug + New US Cord"', 'alt="ITY Plug"'],
    ['alt="CH Plug + New US Cord"', 'alt="CH Plug"'],
    ['alt="ISR Plug + New US Cord"', 'alt="ISR Plug"']
];
plugAlts.forEach(function(r) {
    var n = (h.match(new RegExp(r[0].replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g')) || []).length;
    if (n) { h = h.split(r[0]).join(r[1]); console.log('Replaced alt:', r[0].slice(0, 50)); }
});

// Plug section description update
var oldPlugDesc = '<p>Region-specific plugs compatible with our New US Cord series. Match your target market with locally certified connectors — designed for seamless integration with our grounding system.</p>';
var newPlugDesc = '<p>Region-specific bare plugs for global market compatibility. Match your target market with locally certified connectors — designed for seamless integration with our grounding system.</p>';
if (h.indexOf(oldPlugDesc) !== -1) {
    h = h.replace(oldPlugDesc, newPlugDesc);
    console.log('Plug description updated');
}

// Plug features list
var oldPlugFeat = '<li>Each plug paired with New US Cord ready-to-ship</li>';
var newPlugFeat = '<li>Available in 6 region variants for worldwide compatibility</li>';
if (h.indexOf(oldPlugFeat) !== -1) {
    h = h.replace(oldPlugFeat, newPlugFeat);
    console.log('Plug features updated');
}

// Tester section: alts and update 2.jpg
var oldTestAlt2 = 'alt="Conductive Tester"';
var newTestAlt2 = 'alt="Tester Pen Conductive"';
if (h.indexOf(oldTestAlt2) !== -1) {
    h = h.split(oldTestAlt2).join(newTestAlt2);
    console.log('Tester 2 alt updated (Conductive Tester -> Tester Pen Conductive)');
}

// Tester section description update (highlight Tester Pen)
var oldTesterDesc = '<p>Verify your grounding connection works — every time. From handheld continuity pens to region-specific outlet checkers, ensure your grounding products are performing correctly before each use.</p>';
var newTesterDesc = '<p>Verify your grounding connection works — every time. From handheld continuity pens and conductive testers to region-specific outlet checkers, ensure your grounding products are performing correctly before each use.</p>';
if (h.indexOf(oldTesterDesc) !== -1) {
    h = h.replace(oldTesterDesc, newTesterDesc);
    console.log('Tester description updated');
}

fs.writeFileSync('grounding-kit.html', h, 'utf8');
console.log('\nChanged chars:', h.length - orig.length);

// Verify
console.log('"+ New US Cord" remaining:', (h.match(/\+ New US Cord/g) || []).length, '(expect 0)');
console.log('Plug alts:', (h.match(/alt="[A-Z]{2,3} Plug"/g) || []).length, '(expect 6)');
console.log('Tester alt:', h.indexOf('alt="Tester Pen Conductive"') !== -1, '(expect true)');