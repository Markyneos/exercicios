/**
 * @param {number} index The index of a number in the fibonacci sequence.
 */
const fibonacci = (index) => {
  switch (Number(index)) {
    case 0:
      return 0;
    case 1:
      return 1;
    case 2:
      return 1;
  };
  if (index < 0) {
    return "OOPS";
  }
  let sequence = [1, 1];
  for (let i = 2; i < index; i++) {
    sequence.push(sequence[i - 1] + sequence[i - 2]);
  }
  return sequence[index - 1];
};

// Do not edit below this line
module.exports = fibonacci;
