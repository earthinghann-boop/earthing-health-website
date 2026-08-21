var fs = require('fs');

// Add anchors to pages that don't have them
function addAnchorToFirstSection(file, anchorId) {
    var h = fs.readFileSync(file, 'utf8');
    // Find first <section> after hero and add id
    var heroEnd = h.indexOf('</section>'); // hero closes first
    if (heroEnd === -1) heroEnd = 0;
    var firstSection = h.indexOf('<section', heroEnd);
    if (firstSection === -1) { console.log(file + ': no section found'); return; }
    
    // Check if already has id
    var sectionTagEnd = h.indexOf('>', firstSection);
    var sectionOpen = h.slice(firstSection, sectionTagEnd + 1);
    if (sectionOpen.indexOf('id=') !== -1) { console.log(file + ': already has id'); return; }
    
    // Add id
    var newSectionOpen = sectionOpen.replace('<section', '<section id="' + anchorId + '"');
    h = h.slice(0, firstSection) + newSectionOpen + h.slice(sectionTagEnd + 1);
    fs.writeFileSync(file, h, 'utf8');
    console.log(file + ': added id="' + anchorId + '"');
}

addAnchorToFirstSection('pu-earthing-mat.html', 'pu-sheet');
addAnchorToFirstSection('grounding-mat.html', 'quilt-mat');
addAnchorToFirstSection('grounding-blanket.html', 'blanket');

// Now update index.html hrefs for these
var h = fs.readFileSync('index.html', 'utf8');
var updates = [
    ['puSheetCarousel', 'pu-earthing-mat.html#pu-sheet'],
    ['puDeskCarousel', 'pu-earthing-mat.html#pu-desk-mat'], // need to add second section anchor
    ['quiltCarousel', 'grounding-mat.html#quilt-mat'],
    ['blanketCarousel', 'grounding-blanket.html#blanket']
];

// For pu-earthing-mat.html, need to add id to second section too
var pu = fs.readFileSync('pu-earthing-mat.html', 'utf8');
var heroEnd = pu.indexOf('</section>');
var firstSec = pu.indexOf('<section', heroEnd);
var secondSec = pu.indexOf('<section', firstSec + 8);
if (secondSec !== -1) {
    var tagEnd = pu.indexOf('>', secondSec);
    var open = pu.slice(secondSec, tagEnd + 1);
    if (open.indexOf('id=') === -1) {
        var newOpen = open.replace('<section', '<section id="pu-desk-mat"');
        pu = pu.slice(0, secondSec) + newOpen + pu.slice(tagEnd + 1);
        fs.writeFileSync('pu-earthing-mat.html', pu, 'utf8');
        console.log('pu-earthing-mat.html: added id="pu-desk-mat" to second section');
    }
}

updates.forEach(function(u) {
    var cid = u[0], href = u[1];
    var re = new RegExp('<a href="[^"]*"><div class="carousel" id="' + cid + '"', 'g');
    h = h.replace(re, '<a href="' + href + '"><div class="carousel" id="' + cid + '"');
    console.log('Updated ' + cid + ' -> ' + href);
});

fs.writeFileSync('index.html', h, 'utf8');
console.log('\nAll anchor updates complete');