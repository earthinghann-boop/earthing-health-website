var fs = require('fs');
var path = require('path');

function walkDir(dir, callback) {
    var files = fs.readdirSync(dir);
    files.forEach(function(file) {
        var filepath = path.join(dir, file);
        var stat = fs.statSync(filepath);
        if (stat.isDirectory() && file !== '.git' && file !== 'node_modules') {
            walkDir(filepath, callback);
        } else if (stat.isFile()) {
            var ext = path.extname(file).toLowerCase();
            if (['.html', '.css', '.js', '.md', '.txt'].indexOf(ext) !== -1) {
                callback(filepath);
            }
        }
    });
}

var totalFiles = 0;
var totalReplacements = 0;

walkDir('.', function(filepath) {
    var content = fs.readFileSync(filepath, 'utf8');
    var original = content;
    
    // Replace EARTHING/EARTHING/EARTHING etc with EARTHING
    content = content.replace(/EARTHING/gi, 'EARTHING');
    
    if (content !== original) {
        fs.writeFileSync(filepath, content, 'utf8');
        var count = (original.match(/EARTHING/gi) || []).length;
        console.log('Updated:', filepath, '-', count, 'replacements');
        totalFiles++;
        totalReplacements += count;
    }
});

console.log('\nTotal files updated:', totalFiles);
console.log('Total replacements:', totalReplacements);