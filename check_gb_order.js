var fs = require('fs');
var h = fs.readFileSync('groundingbedding.html', 'utf8');
var secs = [
    ['id="fitted-sheet"', 'Grounding Fitted Sheet'],
    ['id="available-colors"', 'Available Colors'],
    ['id="flat-sheet"', 'Grounding Flat Sheet'],
    ['id="pillow-case"', 'Grounding Pillow Case'],
    ['id="duvet-cover"', 'Grounding Duvet Cover'],
    ['id="kids-bedding"', "Kid's Grounding Bedding"]
];
console.log('Section order:');
secs.forEach(function(s) {
    var idx = h.indexOf('<section class="gb-category-section" ' + s[0]);
    console.log(s[1] + ' starts at byte ' + idx);
});

// Confirm order
var positions = secs.map(function(s) {
    return h.indexOf('<section class="gb-category-section" ' + s[0]);
});
var inOrder = true;
for (var i = 0; i < positions.length - 1; i++) {
    if (positions[i] > positions[i + 1]) inOrder = false;
}
console.log('\nOrder correct:', inOrder);