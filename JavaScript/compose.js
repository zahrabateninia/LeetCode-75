/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x) {
        return functions.reduceRight((acc, fn) => fn(acc), x);
    };
};


const functions = [x => x + 1, x => x * x, x => 2 * x];
const composedFn = compose(functions);

console.log(composedFn(4)); // 65
// 2*4=8 then 8*8=64 then 64+1=65
