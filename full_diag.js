var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
console.log('File size:', h.length);

// All carousel IDs
var re = /class="carousel" id="([^"]+)"/g;
var ids = [];
var m;
while ((m = re.exec(h)) !== null) ids.push(m[1]);
console.log('Carousel IDs (' + ids.length + '):');
ids.forEach(function(id) { console.log('  ' + id); });

// Buggy onclicks
var buggy = [];
var buggyRe = /onclick="goProductSlide_([^("]+)\([^,)]+,/g;
while ((m = buggyRe.exec(h)) !== null) buggy.push(m[0]);
console.log('\nBuggy onclicks (' + buggy.length + '):');
buggy.slice(0, 5).forEach(function(b) { console.log('  ' + b); });

// Correct onclicks
var correct = [];
var correctRe = /onclick="goProductSlide_([^("]+)\(\d+\)"/g;
while ((m = correctRe.exec(h)) !== null) correct.push(m[0]);
console.log('\nCorrect onclicks (' + correct.length + '):');
correct.slice(0, 5).forEach(function(c) { console.log('  ' + c); });

// Product card count
var cards = (h.match(/class="product-card"/g) || []).length;
console.log('\nProduct cards:', cards);