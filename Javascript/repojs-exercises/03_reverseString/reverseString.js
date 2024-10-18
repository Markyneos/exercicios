/**
 * @param {string} str string parameter
 * @param {string} reverseString reverse string function
 *
 */
const reverseString = (str) => {
  let strArray = [];
  for (let i = 0; i < str.length; i++) {
    strArray.push(str[i]);
  }
  strArray.reverse();
  let str2 = "";
  for (let i = 0; i < str.length; i++) {
    str2 += strArray[i];
  }
  return str2
};

//const reverseString = (string) => string.split("").reverse().join("");

// Do not edit below this line
module.exports = reverseString;
