var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// 23 carousel IDs
var ids = [
    'fittedCarousel','flatCarousel','pillowCarousel','duvetCarousel','kidsCarousel',
    'puSheetCarousel','puDeskCarousel','quiltCarousel','blanketCarousel',
    'shawlCarousel','fishmanCarousel','beanieCarousel','hoodCarousel','capCarousel',
    'curtainCarousel','socksCarousel','eyeMaskCarousel','sleeveCarousel','loungeCarousel',
    'boxerCarousel','kitCordCarousel','kitPlugCarousel','kitTesterCarousel'
];

// Build goProductSlide_xxx + moveProductSlide_xxx
var funcs = ids.map(function(id) {
    return 'function goProductSlide_' + id + '(n) {\n' +
        '    var el = document.getElementById("' + id + '");\n' +
        '    if (!el) return;\n' +
        '    var slides = el.querySelectorAll(".carousel-img");\n' +
        '    var dots = el.querySelectorAll(".dot");\n' +
        '    if (!slides.length) return;\n' +
        '    var total = slides.length;\n' +
        '    var cur = Array.from(slides).findIndex(function(s){return s.classList.contains("active");});\n' +
        '    var next;\n' +
        '    if (n >= 0 && n < total) { next = n; }\n' +
        '    else { next = (cur + 1 + total) % total; }\n' +
        '    if (slides[cur]) slides[cur].classList.remove("active");\n' +
        '    if (slides[next]) slides[next].classList.add("active");\n' +
        '    if (dots[cur]) dots[cur].classList.remove("active");\n' +
        '    if (dots[next]) dots[next].classList.add("active");\n' +
        '}\n\n' +
        'function moveProductSlide_' + id + '(dir) { goProductSlide_' + id + '(dir); }';
}).join('\n\n');

// Init all 23 carousels on DOMContentLoaded
var idsJson = JSON.stringify(ids);
var init = 'document.addEventListener("DOMContentLoaded", function() {\n' +
    '    ' + ids.map(function(id) {
        return 'initHomepageCarousel("' + id + '")';
    }).join(';\n    ') +
    ';\n});\n\n' +
    'function initHomepageCarousel(id) {\n' +
    '    var el = document.getElementById(id);\n' +
    '    if (!el) return;\n' +
    '    var slides = el.querySelectorAll(".carousel-img");\n' +
    '    var dotsEl = el.querySelector(".carousel-dots");\n' +
    '    if (!slides.length || !dotsEl) return;\n' +
    '    dotsEl.innerHTML = "";\n' +
    '    for (var i = 0; i < slides.length; i++) {\n' +
    '        var dot = document.createElement("span");\n' +
    '        dot.className = "dot" + (i === 0 ? " active" : "");\n' +
    '        (function(idx) {\n' +
    '            dot.onclick = function() { window["goProductSlide_" + id](idx); };\n' +
    '        })(i);\n' +
    '        dotsEl.appendChild(dot);\n' +
    '    }\n' +
    '    var timer = null;\n' +
    '    el.addEventListener("mouseenter", function() { clearInterval(timer); });\n' +
    '    el.addEventListener("mouseleave", function() {\n' +
    '        timer = setInterval(function() { window["moveProductSlide_" + id](1); }, 3500);\n' +
    '    });\n' +
    '    el.dispatchEvent(new Event("mouseleave"));\n' +
    '}';

var newScript = '\n<script>\n' + funcs + '\n\n' + init + '\n</script>\n';

// Replace existing script block
var scriptOpen = h.indexOf('<script>');
var scriptClose = h.lastIndexOf('</script>');
var newH = h.slice(0, scriptOpen) + newScript + h.slice(scriptClose + 9);
fs.writeFileSync('index.html', newH, 'utf8');
console.log('New size:', newH.length);

// Verify
var funcCount = (newH.match(/function goProductSlide_/g) || []).length;
console.log('goProductSlide functions:', funcCount, '(expect 23)');
var missing = ids.filter(function(id) {
    return newH.indexOf('function goProductSlide_' + id) === -1;
});
console.log('Missing:', missing.length ? missing.join(', ') : 'none');
var buggy = (newH.match(/goProductSlide_\w+\([^,]+,[^)]+\)/g) || []).length;
console.log('Buggy onclicks:', buggy, '(expect 0)');