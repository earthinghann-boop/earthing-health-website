var fs = require('fs');
var path = 'C:/Users/18574/Desktop/EARTHING/接地线资料/测试笔';
function list(d) {
    if (!fs.existsSync(d)) {
        console.log('NOT EXISTS:', d);
        return;
    }
    var items = fs.readdirSync(d, {withFileTypes: true});
    items.forEach(function(it) {
        if (it.isFile()) {
            var sz = fs.statSync(d + '/' + it.name).size;
            console.log(it.name + ' (' + sz.toLocaleString() + 'b)');
        }
    });
}
console.log('=== 测试笔 ===');
list(path);