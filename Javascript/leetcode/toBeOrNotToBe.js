/**
 * @param {string} val
 * @returns {object}
 * @
 */
const expect = (val) => {
	return {
		toBe: (anotherVal) => {
			if (val === anotherVal) {
				return true;
			}
			else {
				throw "Not Equal";
			}
		},
		notToBe: (anotherVal) => {
			if (val !== anotherVal) {
				return true;
			}
			else {
				throw "Equal";
			}
		}
	};
};

/**
 * expect(5).toBe(5); //true
 * expect(5).notToBe(5); //throws "Equal"
*/
