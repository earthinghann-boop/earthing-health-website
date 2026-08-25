var fs = require('fs');
// 1. Find lang-switcher HTML in main pages
var files = ['index.html', 'zh/index.html', 'grounding-sheets.html', 'zh/grounding-sheets.html', 'zh/pu-earthing-mat.html'];
files.forEach(function(fp) {
  var h = fs.readFileSync(fp, 'utf8');
  var i = h.indexOf('lang-switcher-item');
  if (i < 0) i = h.indexOf('class="lang-switcher"');
  if (i < 0) {
    console.log('=== ' + fp + ' === NO lang-switcher');
    return;
  }
  var j = h.indexOf('</li>', i);
  if (j < 0) j = h.indexOf('</div>', i) + 6;
  var endJ = h.indexOf('</li>', i);
  var endDiv = h.indexOf('</div>', i);
  var end = (endJ > 0 && endJ < (endDiv > 0 ? endDiv + 200 : 999999)) ? endJ + 5 : endDiv + 6;
  console.log('=== ' + fp + ' ===');
  console.log(h.substring(Math.max(0, i - 30), end).replace(/\r/g, ' ').replace(/\n/g, ' '));
  console.log('');
});

// 2. Check CSS for lang-switcher
var css = fs.readFileSync('css/style.css', 'utf8');
var cssIdx = css.indexOf('.lang-switcher');
if (cssIdx >= 0) {
  // Find the rule block
  var braceStart = css.indexOf('{', cssIdx);
  var braceEnd = css.indexOf('}', braceStart);
  console.log('=== CSS .lang-switcher rules ===');
  // Print all lang-switcher related rules
  var rules = css.substring(cssIdx - 100, cssIdx + 1500);
  var matches = rules.match(/\.lang-switcher[^{]*\{[^}]*\}/g);
  if (matches) matches.forEach(function(m) { console.log(m); });
  console.log('');
}
