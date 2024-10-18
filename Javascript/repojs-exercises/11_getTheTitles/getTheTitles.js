/**
 * @param {Array.<object>} array An array of objects that refers to books, with the attributes of title and author name.
 */
const getTheTitles = (array) => {
  let titles = [];
  array.forEach((obj) => {
    titles.push(obj.title);
  });
  return titles;
};

// Do not edit below this line
module.exports = getTheTitles;
