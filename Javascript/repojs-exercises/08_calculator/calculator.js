/**
 * @param {Array.<number>} array An array of numbers to have their elements summed.
 * @param {number} nums A number (or more) to be summed of subtracted.
 * @param {number} base The base that will be powered by the exponent.
 * @param {number} exponent The exponent of a power operation to elevate the base to it.
 * @param {number} numEntry The number to figure the factorial of.
 */
const add = (...nums) => {
  let sum = 0;
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
  }
  return sum;
};

const subtract = (...nums) => {
  let result = nums[0];
  for (let i = 1; i < nums.length; i++) {
    result -= nums[i];
  }
  return result;
};

const sum = (array) => {
  let sum = 0;
  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }
  return sum;
};

const multiply = (array) => {
  let result = array[0];
  for (let i = 1; i < array.length; i++) {
    result *= array[i];
  }
  return result;
};

const power = (base, exponent) => {
  let result = 1;
  for (let i = 0; i < exponent; i++) {
    result *= base;
  }
  return result;
};

const factorial = (numEntry) => {
  if (numEntry == 1 || numEntry == 0) {
    return 1;
  }
  else {
    return numEntry * factorial(numEntry - 1);
  }
};

// Do not edit below this line
module.exports = {
  add,
  subtract,
  sum,
  multiply,
  power,
  factorial
};
