var fs = require('fs');
var path = 'C:/Users/18574/Desktop/EARTHING/接地线资料/plugs';
function list(d) {
    var items = fs.readdirSync(d, {withFileTypes: true});
    items.forEach(function(it) {
        if (it.isFile()) {
            var sz = fs.statSync(d + '/' + it.name).size;
            console.log(it.name + ' (' + sz.toLocaleString() + 'b)');
        }
    });
}
console.log('=== plugs root *.png ===');
list(path);