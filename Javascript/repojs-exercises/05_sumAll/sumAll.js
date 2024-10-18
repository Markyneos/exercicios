/**
 * @param {number} num1 A number parameter initiate the sum
 *@param {number} num2 A number parameter to close the sum between the two numbers
  */
const sumAll = (num1, num2) => {
  let sum = 0;
  if (!Number.isInteger(num1) || !Number.isInteger(num2)) return "ERROR";
  if (num1 < 0 || num2 < 0) return "ERROR";
  if (num1 < num2) {
    for (let i = num1; i <= num2; i++) {
      sum += i;
    }
  }
  else if (num1 > num2) {
    for (let i = num1; i >= num2; i--) {
      sum += i;
    }
  }
  return sum;
};

// Do not edit below this line
module.exports = sumAll; 
