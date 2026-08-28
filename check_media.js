var fs = require('fs');
var css = fs.readFileSync('css/style.css', 'utf8');

// Extract all @media rules
var re = /@media[^{]*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}/g;
var matches = css.match(re) || [];
console.log('Total @media blocks:', matches.length);
matches.forEach(function(m, idx) {
  var head = m.substring(0, m.indexOf('{'));
  console.log('--- #' + (idx+1) + ' ' + head + ' ---');
});

// Also check hero styles
console.log('');
console.log('=== Hero rules ===');
var heroRe = /\.(hero|hero-[a-z]+|hero-content|hero-text|hero-image|hero-cta|btn|btn-[a-z]+)[^{]*\{[^}]*\}/g;
var hs = css.match(heroRe) || [];
hs.slice(0, 20).forEach(function(s) { console.log(s); });

// Also footer mobile
console.log('');
console.log('=== Footer rules ===');
var fr = css.match(/\.footer[^{]*\{[^}]*\}/g) || [];
fr.forEach(function(s) { console.log(s); });
