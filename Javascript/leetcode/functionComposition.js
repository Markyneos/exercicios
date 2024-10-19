/**
 * @param {Array.<Function>} functions
 * @returns {Function}
 */
const compose = (functions) => {

	return (x) => {
		if (functions.length == 0) {
			return x;
		}
		let value = x;
		for (let i = functions.length - 1; i >= 0; i--) {
			value = functions[i](value);
		}
		return value;
	}
};

const fn = compose([x => x + 1, x => x * x, x => 2 * x]);
console.log(fn(4));
