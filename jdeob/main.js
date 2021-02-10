const astring = require("./astring-node.js")

//var fs = require('fs');
//var ast = fs.readFileSync(process.stdin.fd, 'utf-8');

function makeSpaces(amount) {
    var result = ''
    while (amount-- > 0) result += ' '
    return result
}

var indentAmount = 4
var indent = makeSpaces(indentAmount)

//var ast = process.argv[2]

//console.log(ast)

var ast = JSON.parse(process.argv[2])

//console.log(ast)

var formattedCode = astring.generate(ast, {
    indent: indent,
})

console.log(formattedCode)
