const fs = require('fs');
const style = fs.readFileSync('style.css', 'utf8');

// Just extracting the desktop CSS values to understand the issue.
const regex = /#(outline-\w+(?:-\w+)*)\s*{\s*([^}]+)\s*}/g;
let match;
while ((match = regex.exec(style)) !== null) {
    if (match[2].includes('calc')) {
        console.log(match[1], match[2]);
    }
}
