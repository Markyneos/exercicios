/**
 * @param {Array.<any>} array The array to remove item from
 * @param {any} items An item to remove from the array
  */
//const removeFromArray = (array, ...items) => {
//  let array2 = [];
//  array.forEach((item) => {
//    if (!items.includes(item)) {
//      array2.push(item);
//    }
//  });
//  return array2;
//};

const removeFromArray = (array, ...items) => array.filter(val => !items.includes(val));

// Do not edit below this line
module.exports = removeFromArray;
