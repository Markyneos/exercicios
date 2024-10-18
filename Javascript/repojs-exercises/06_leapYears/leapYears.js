/**
 * @param {number} year A year to verify if it's a leap year or not
 */
const leapYears = (year) => {
  if (year % 4 == 0) {
    if (year % 100 == 0) {
      if (year % 400 == 0) {
        return true;
      }
      return false;
    }
    return true;
  }
  else {
    return false;
  }
};

// Do not edit below this line
module.exports = leapYears;
