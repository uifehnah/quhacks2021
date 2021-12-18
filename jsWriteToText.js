console.log("YES")
const fs = require('fs')

let data = "Learning how to write in a file."
fs.writeFile('data.txt', data, (err) => {
    if (err) throw err;
})
