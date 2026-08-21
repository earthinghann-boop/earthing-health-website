var fs = require('fs');
var { execSync } = require('child_process');
// Restore from 95040d6 - last clean version (no colors section)
var clean = execSync('git show 95040d6:groundingbedding.html', {encoding: 'utf8'});
fs.writeFileSync('groundingbedding.html', clean, 'utf8');
console.log('Restored from 95040d6. Size:', clean.length, 'chars');
// Sanity check: no available-colors
console.log('available-colors count:', (clean.match(/available-colors/g) || []).length);