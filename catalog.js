var fs = require('fs');
var path = 'C:/Users/18574/.qclaw/workspace/earthinghealth-website';
var items = fs.readdirSync(path + '/images/products', {withFileTypes: true});
items.sort(function(a, b) { return a.name.localeCompare(b.name); });
console.log('=== Products Directory ===');
items.forEach(function(it) {
    if (it.isDirectory()) {
        var dir = path + '/images/products/' + it.name;
        var files = fs.readdirSync(dir).filter(function(f) { return /\.(jpg|png)$/i.test(f); });
        console.log('\n[' + it.name + '] ' + files.length + ' files');
        files.slice(0, 6).forEach(function(f) { console.log('  ' + f); });
        if (files.length > 6) console.log('  ... (' + (files.length - 6) + ' more)');
    }
});