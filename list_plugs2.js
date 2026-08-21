var fs = require('fs');
var path = 'C:/Users/18574/Desktop/EARTHING/接地线资料/plugs';
function list(d, prefix) {
    var items = fs.readdirSync(d, {withFileTypes: true});
    items.forEach(function(it) {
        var p = d + '/' + it.name;
        if (it.isFile()) {
            var sz = fs.statSync(p).size;
            console.log(prefix + it.name + ' (' + sz.toLocaleString() + 'b)');
        }
    });
}
console.log('=== plugs 根目录 ===');
list(path, '  ');
console.log('\n=== cords&plugs 子目录 ===');
list(path + '/cords&plugs', '  ');
console.log('\n=== New US+plugs 子目录 ===');
list(path + '/New US+plugs', '  ');
console.log('\n=== US+Plugs 子目录 ===');
list(path + '/US+Plugs', '  ');