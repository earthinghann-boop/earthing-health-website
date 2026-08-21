var fs = require('fs');
var path = 'C:/Users/18574/Desktop/EARTHING/接地线资料/plugs';
function walk(d, prefix) {
    if (prefix.length > 3) return;
    var items = fs.readdirSync(d, {withFileTypes: true});
    items.forEach(function(it) {
        var p = d + '/' + it.name;
        if (it.isDirectory()) {
            console.log(prefix + '[DIR] ' + it.name);
            walk(p, prefix + '  ');
        } else {
            var sz = fs.statSync(p).size;
            console.log(prefix + it.name + ' (' + sz.toLocaleString() + 'b)');
        }
    });
}
walk(path, '');