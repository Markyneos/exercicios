/**
 * @param {number} fahrenheitTemp A Fahrenheit temperature to be converted to celsius temperature.
 * @param {number} celsiusTemp A Celsius temperature to be converted to fahrenheit temperature.
 */
const convertToCelsius = (fahrenheitTemp) => {
  let celsius = (fahrenheitTemp - 32) * 5 / 9;
  if (!Number.isInteger(celsius)) {
    return Number(celsius.toFixed(1));
  }
  else {
    return celsius;
  }
};

const convertToFahrenheit = (celsiusTemp) => {
  let fahrenheit = (celsiusTemp * 9 / 5) + 32;
  if (!Number.isInteger(fahrenheit)) {
    return Number(fahrenheit.toFixed(1));
  }
  else {
    return fahrenheit;
  }
};

// Do not edit below this line
module.exports = {
  convertToCelsius,
  convertToFahrenheit
};
