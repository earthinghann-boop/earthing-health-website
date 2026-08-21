var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Find and REMOVE entire <script> block, replace with fresh one
var scriptOpen = h.indexOf('<script>');
var scriptClose = h.lastIndexOf('</script>');
console.log('Script block: ' + scriptOpen + '-' + scriptClose + ' (' + (scriptClose - scriptOpen + 9) + ' chars)');

// 11 carousel IDs
var ids = ['beddingCarousel', 'puCarousel', 'quiltCarousel', 'blanketCarousel',
           'shawlCarousel', 'beanieCarousel', 'socksCarousel', 'eyemaskCarousel',
           'sleeveCarousel', 'loungeCarousel', 'kitCarousel'];

// Build goProductSlide_xxx(n)
var goFuncs = ids.map(function(id) {
    return 'function goProductSlide_' + id + '(n) {\n' +
        '    var el = document.getElementById("' + id + '");\n' +
        '    if (!el) return;\n' +
        '    var slides = el.querySelectorAll(".carousel-img");\n' +
        '    var dots = el.querySelectorAll(".dot");\n' +
        '    if (!slides.length) return;\n' +
        '    var total = slides.length;\n' +
        '    var cur = Array.from(slides).findIndex(function(s) { return s.classList.contains("active"); });\n' +
        '    var next;\n' +
        '    if (n >= 0 && n < total) { next = n; }   // dot: absolute index\n' +
        '    else { next = (cur + 1 + total) % total; } // auto: relative +1\n' +
        '    if (slides[cur]) slides[cur].classList.remove("active");\n' +
        '    if (slides[next]) slides[next].classList.add("active");\n' +
        '    if (dots[cur]) dots[cur].classList.remove("active");\n' +
        '    if (dots[next]) dots[next].classList.add("active");\n' +
        '    return next;\n' +
        '}\n\n' +
        'function moveProductSlide_' + id + '(dir) {\n' +
        '    goProductSlide_' + id + '(dir);\n' +
        '}';
}).join('\n\n');

// Build init function
var idsJson = JSON.stringify(ids);
var initFunc = 'function initHomepageCarousel(id) {\n' +
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
    '        el.dispatchEvent(new Event("mouseleave"));\n' +
    '    });\n' +
    '}\n\n' +
    'document.addEventListener("DOMContentLoaded", function() {\n' +
    '    var ids = ' + idsJson + ';\n' +
    '    ids.forEach(function(id) { initHomepageCarousel(id); });\n' +
    '});';

var newScript = '\n<script>\n' + goFuncs + '\n\n' + initFunc + '\n</script>\n';

var newH = h.slice(0, scriptOpen) + newScript + h.slice(scriptClose + 9);
fs.writeFileSync('index.html', newH, 'utf8');
console.log('New size:', newH.length);

// Verify
var buggy = (newH.match(/goProductSlide_\w+\([^,]+,/g) || []).length;
console.log('Buggy onclicks remaining:', buggy, '(expect 0)');
var carouselCount = (newH.match(/class="carousel" id="/g) || []).length;
console.log('Carousels:', carouselCount);
var dotCount = (newH.match(/onclick="goProductSlide_/g) || []).length;
console.log('Dot handlers:', dotCount);