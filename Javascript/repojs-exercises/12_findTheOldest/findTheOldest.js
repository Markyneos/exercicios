/**
 * @param {Array.<object>} array An array of objects with properties of age of birth and death to discover the oldest object (person).
 * @param {Array.<number>} array2 An array of numbers to find the biggest between them.
 */
const findTheBiggest = (array2) => {
  let index = 0;
  let biggest = array2[array2.length - 1];
  for (let i = 0; i < array2.length; i++) {
    if (biggest < array2[i]) {
      biggest = array2[i];
      index = i;
    }
  }
  return index;
}
const findTheOldest = (array) => {
  let ages = [];
  for (let i = 0; i < array.length; i++) {
    ages.push(array[i].yearOfDeath - array[i].yearOfBirth);
  }
  return array[findTheBiggest(ages)];
};

// Do not edit below this line
module.exports = findTheOldest;
