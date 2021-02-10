const astring = require("./astring-node.js");
function makeSpaces(amount) {
    var result = \'\';
    while (amount-- > 0) result += \' \';
    return result;
}
var indentAmount = 4;
var indent = makeSpaces(indentAmount);
var ast = JSON.parse(process.argv[2]);
var formattedCode = astring.generate(ast, {
    indent: indent
});
console.log(formattedCode);
