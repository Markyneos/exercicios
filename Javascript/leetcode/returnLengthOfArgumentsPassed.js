/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @returns {number}
 */
const argumentsLength = (...args) => args.length;
console.log(argumentsLength(1, 2, 3, 4))
