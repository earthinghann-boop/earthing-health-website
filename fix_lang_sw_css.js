var fs = require('fs');
var path = require('path');

// 1. Add lang-switcher CSS to css/style.css
var css = fs.readFileSync('css/style.css', 'utf8');
if (css.indexOf('.lang-switcher') < 0) {
  var append = '\n/* Language Switcher (shared across all pages) */\n'
    + '.lang-switcher { display:flex; align-items:center; gap:8px; margin-left:auto; padding:0 16px; }\n'
    + '.lang-switcher a, .lang-switcher span { font-size:14px; color:#888; text-decoration:none; padding:4px 8px; border-radius:4px; transition:all 0.2s; }\n'
    + '.lang-switcher .lang-current { color:#1D3A2D; font-weight:600; background:rgba(29,58,45,0.1); }\n'
    + '.lang-switcher a:hover { color:#1D3A2D; background:rgba(29,58,45,0.05); }\n'
    + '@media (max-width:768px){ .lang-switcher { margin:8px 16px; justify-content:center; } }\n';
  fs.writeFileSync('css/style.css', css + append, 'utf8');
  console.log('css/style.css: appended lang-switcher rules');
} else {
  console.log('css/style.css: already has lang-switcher');
}

// 2. Remove inline <style> blocks containing .lang-switcher from all HTML files (except index.html which we keep as fallback / clean it too)
var files = fs.readdirSync('.').filter(function(f) { return f.endsWith('.html'); })
  .concat(['zh/index.html', 'zh/grounding-sheets.html', 'zh/grounding-mat.html', 'zh/grounding-blanket.html',
    'zh/emf-wearing.html', 'zh/grounding-kit.html', 'zh/groundingbedding.html',
    'zh/grounding-pillow-cases.html', 'zh/pu-earthing-mat.html', 'zh/get-price.html']);

var seen = {};
files.forEach(function(fp) {
  if (seen[fp]) return;
  seen[fp] = true;
  if (!fs.existsSync(fp)) return;
  var h = fs.readFileSync(fp, 'utf8');
  // Match inline <style>...</style> blocks that contain ".lang-switcher"
  var re = /<style[^>]*>[\s\S]*?\.lang-switcher[\s\S]*?<\/style>/g;
  var matches = h.match(re);
  if (matches && matches.length > 0) {
    var removed = matches.reduce(function(s, m) { return s + m.length; }, 0);
    h = h.replace(re, '');
    fs.writeFileSync(fp, h, 'utf8');
    console.log(fp + ': removed ' + matches.length + ' inline <style> block(s), -' + removed + ' bytes');
  }
});
