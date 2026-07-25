const fs = require('fs');
const path = require('path');

const src = path.join(__dirname, '_pages', '主页照.jpg');
const dstDir = path.join(__dirname, 'images');
const dst = path.join(dstDir, 'profile.jpg');

console.log('Source:', src);
console.log('Source exists:', fs.existsSync(src));

if (fs.existsSync(src)) {
    if (!fs.existsSync(dstDir)) {
        fs.mkdirSync(dstDir, { recursive: true });
    }
    fs.copyFileSync(src, dst);
    console.log('Copied successfully');
    console.log('Dest size:', fs.statSync(dst).size);
} else {
    console.log('ERROR: Source not found');
    process.exit(1);
}
