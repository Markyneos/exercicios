/**
 * @param {string} item An item to be checked if it's an palindrome or not
 */
const palindromes = (item) => {
  const alphanumerical = "abcdefghijklmnopqrstuvwxyz0123456789";
  const cleanedString = item.toLowerCase().split("").filter((character) => alphanumerical.includes(character)).join("");
  const reversedString = cleanedString.split("").reverse().join("");
  return cleanedString === reversedString;
};

module.exports = palindromes;

