var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// Find the existing script block
var scriptOpen = h.indexOf('<script>');
var scriptClose = h.lastIndexOf('</script>');
var script = h.slice(scriptOpen, scriptClose + 9);
console.log('Script length:', script.length);
// Check for goProductSlide_ functions
var ids = ['beddingCarousel', 'puCarousel', 'quiltCarousel', 'blanketCarousel',
           'shawlCarousel', 'beanieCarousel', 'socksCarousel', 'eyemaskCarousel',
           'sleeveCarousel', 'loungeCarousel', 'kitCarousel'];
console.log('\nFunction check:');
ids.forEach(function(id) {
    var hasGo = script.indexOf('function goProductSlide_' + id) !== -1;
    var hasMove = script.indexOf('function moveProductSlide_' + id) !== -1;
    console.log('  ' + id + ': goProductSlide=' + hasGo + ' moveProductSlide=' + hasMove);
});
// Check what classes the script manages
console.log('\n.slides in script:', script.indexOf('.cert-slide') !== -1);
console.log('.carousel-img in script:', script.indexOf('.carousel-img') !== -1);
console.log('.carousel in script:', script.indexOf("'.carousel'") !== -1);