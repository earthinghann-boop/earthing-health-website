var fs = require('fs');
var css = fs.readFileSync('css/style.css', 'utf8');

// Append zoom CSS to css/style.css
var zoomCSS = '\n\n/* Homepage product image zoom on hover */\n' +
    '.product-image .carousel-img { transition: transform 0.5s ease !important; }\n' +
    '.product-image:hover .carousel-img.active { transform: scale(1.05); }\n' +
    '.product-image a { display: block; overflow: hidden; }\n';

fs.writeFileSync('css/style.css', css + zoomCSS, 'utf8');
console.log('css/style.css updated. New size:', (css + zoomCSS).length);
console.log('Zoom CSS appended at end');

// Verify
var h = fs.readFileSync('css/style.css', 'utf8');
console.log('scale(1.05) present:', h.indexOf('scale(1.05)') !== -1);