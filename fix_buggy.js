var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');

// Find script block
var scriptOpen = h.indexOf('<script>');
var scriptClose = h.lastIndexOf('</script>');
var beforeScript = h.slice(0, scriptOpen);
var script = h.slice(scriptOpen, scriptClose + 9);
var afterScript = h.slice(scriptClose + 9);

console.log('Script block length:', script.length);

// New carousel IDs we added
var newIds = ['beddingCarousel', 'puCarousel', 'quiltCarousel', 'blanketCarousel',
              'shawlCarousel', 'beanieCarousel', 'socksCarousel', 'eyemaskCarousel',
              'sleeveCarousel', 'loungeCarousel', 'kitCarousel'];

// Remove ALL old buggy dot onclicks from old script (they reference old carousel IDs)
var cleanedScript = script
    // Remove old buggy goProductSlide_xxx(this, n) calls in dot onclick attributes
    .replace(/onclick="goProductSlide_\w+\(this,\s*\w+\)"/g, '')
    // Remove old buggy moveProductSlide_ calls (buttons)
    .replace(/onclick="moveProductSlide_\w+\([^)]+\)"/g, '')
    // Remove old buildCarousel dot wiring (replaced by initHomepageCarousels)
    .replace(/buildCarousel\(\);[\s\S]*$/, '');

// Add fresh initHomepageCarousels function
var initScript = '\n\n// Homepage carousel initialization\n' +
    'function initHomepageCarousel(id) {\n' +
    '    var el = document.getElementById(id);\n' +
    '    if (!el) return;\n' +
    '    var slides = el.querySelectorAll(".carousel-img");\n' +
    '    var dotsContainer = el.querySelector(".carousel-dots");\n' +
    '    if (!slides.length || !dotsContainer) return;\n' +
    '    var total = slides.length;\n' +
    '    // Build dots\n' +
    '    dotsContainer.innerHTML = "";\n' +
    '    for (var i = 0; i < total; i++) {\n' +
    '        var dot = document.createElement("span");\n' +
    '        dot.className = "dot" + (i === 0 ? " active" : "");\n' +
    '        (function(idx) {\n' +
    '            dot.onclick = function() {\n' +
    '                goProductSlide_' + id.replace(/([A-Z])/g, "_$1").toLowerCase() + '(idx);\n' +
    '            };\n' +
    '        })(i);\n' +
    '        dotsContainer.appendChild(dot);\n' +
    '    }\n' +
    '    // Auto-play\n' +
    '    var timer = null;\n' +
    '    el.addEventListener("mouseenter", function() {\n' +
    '        clearInterval(timer);\n' +
    '    });\n' +
    '    el.addEventListener("mouseleave", function() {\n' +
    '        timer = setInterval(function() {\n' +
    '            moveProductSlide_' + id.replace(/([A-Z])/g, "_$1").toLowerCase() + '(1);\n' +
    '        }, 3500);\n' +
    '    });\n' +
    '    el.dispatchEvent(new Event("mouseleave"));\n' +
    '}\n\n' +
    'document.addEventListener("DOMContentLoaded", function() {\n' +
    '    var ids = ' + JSON.stringify(newIds) + ';\n' +
    '    ids.forEach(function(id) { initHomepageCarousel(id); });\n' +
    '});';

var newScript = cleanedScript + '\n' + initScript + '\n</script>';

var newH = beforeScript + newScript + afterScript;
fs.writeFileSync('index.html', newH, 'utf8');
console.log('New size:', newH.length, '(was', h.length + ')');

// Verify
var buggy = (newH.match(/goProductSlide_\w+\([^,]+,/g) || []).length;
console.log('Buggy onclicks remaining:', buggy, '(expect 0)');