var fs = require('fs');
var path = 'C:/Users/18574/.qclaw/workspace/earthinghealth-website';
var prods = fs.readdirSync(path + '/images/products', {withFileTypes: true});
prods.sort(function(a, b) { return a.name.localeCompare(b.name); });
prods.forEach(function(it) {
    if (it.isDirectory()) {
        var dir = path + '/images/products/' + it.name;
        var files = fs.readdirSync(dir).filter(function(f) { return /\.(jpg|png)$/i.test(f); });
        // Count and show first 3
        var first3 = files.slice(0, 3);
        console.log(it.name + ' (' + files.length + ' total) -> using first 3: ' + first3.join(', '));
    }
});