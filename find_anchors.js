var fs = require('fs');
var h = fs.readFileSync('index.html', 'utf8');
// What comes BEFORE the section
console.log('Before section (150 chars before 6967):');
console.log(JSON.stringify(h.slice(6967 - 150, 6967 + 50)));
// What comes AFTER the section
console.log('\nAfter section (300 chars from end 51753):');
console.log(JSON.stringify(h.slice(51753 - 50, 51753 + 300)));