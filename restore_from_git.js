var fs = require('fs');
var { execSync } = require('child_process');
// Restore groundingbedding.html from before f7b1c66 (last clean version)
var clean = execSync('git show f7b1c66^:groundingbedding.html', {encoding: 'utf8'});
fs.writeFileSync('groundingbedding.html', clean, 'utf8');
console.log('Restored. Size:', clean.length);