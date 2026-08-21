var fs = require('fs');
var { execSync } = require('child_process');
execSync('git checkout HEAD -- index.html', {cwd: 'C:/Users/18574/.qclaw/workspace/earthinghealth-website'});
var h = fs.readFileSync('index.html', 'utf8');
console.log('Restored. Size:', h.length);