var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Fix dot onclick: goProductSlide_<id>(id, n) -> goProductSlide_<id>(n)
// The correct logic: dot passes absolute index, button passes relative dir
// Inject corrected function before the existing script block closes

// Find the <script> closing tag
var scriptClose = h.lastIndexOf('</script>');
console.log('Script closes at:', scriptClose);

// Find all unique carousel IDs
var ids = [];
var re = /class="carousel" id="([^"]+)"/g;
var m;
while ((m = re.exec(h)) !== null) {
    if (ids.indexOf(m[1]) === -1) ids.push(m[1]);
}
console.log('Carousel IDs:', ids.join(', '));

// Build corrected goProductSlide_ function injection
// Pattern: goProductSlide_<id>(n) where n is 0-based absolute index
var goProductSlideFuncs = ids.map(function(id) {
    return 'function goProductSlide_' + id + '(n) {\n' +
        '    var el = document.getElementById("' + id + '");\n' +
        '    if (!el) return;\n' +
        '    var slides = el.querySelectorAll(".carousel-img");\n' +
        '    var dots = el.querySelectorAll(".dot");\n' +
        '    if (!slides.length) return;\n' +
        '    var total = slides.length;\n' +
        '    var cur = Array.from(slides).findIndex(function(s) { return s.classList.contains("active"); });\n' +
        '    var next;\n' +
        '    if (n >= 0 && n < total) { next = n; }  // dot click: absolute\n' +
        '    else { next = (cur + 1 + total) % total; }  // auto/button: relative +1\n' +
        '    slides[cur].classList.remove("active");\n' +
        '    slides[next].classList.add("active");\n' +
        '    if (dots[cur]) dots[cur].classList.remove("active");\n' +
        '    if (dots[next]) dots[next].classList.add("active");\n' +
        '    return next;\n' +
        '}';
}).join('\n\n');

var moveProductSlideFuncs = ids.map(function(id) {
    return 'function moveProductSlide_' + id + '(dir) {\n' +
        '    goProductSlide_' + id + '(dir);  // dir=-1 or +1, treated as relative\n' +
        '}';
}).join('\n\n');

// Fix the existing buggy dot onclicks: goProductSlide_<id>(id, n) -> goProductSlide_<id>(n)
var newH = h;
ids.forEach(function(id) {
    // Match goProductSlide_<id>(this, N) or goProductSlide_<id>(id, N)
    var buggy = new RegExp('goProductSlide_' + id + '\\([^)]+,' + '([^)]+)\\)', 'g');
    var fixed = 'goProductSlide_' + id + '($1)';
    var replaced = newH.replace(buggy, fixed);
    if (replaced !== newH) {
        console.log('Fixed dot onclick for', id);
        newH = replaced;
    }
});

// Inject corrected functions before </script>
var injected = newH.slice(0, scriptClose) + '\n' + goProductSlideFuncs + '\n\n' + moveProductSlideFuncs + '\n' + newH.slice(scriptClose);

fs.writeFileSync('index.html', injected, 'utf8');
console.log('\nInjected JS. New size:', injected.length, '(was', h.length, ', delta:', injected.length - h.length + ')');

// Verify no buggy onclicks remain
var buggyCount = (injected.match(/goProductSlide_\w+\([^,]+,/g) || []).length;
console.log('Buggy onclicks remaining:', buggyCount, '(expect 0)');