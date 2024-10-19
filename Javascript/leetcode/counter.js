/**
 * @param {number} n
 * @returns {Function} counter
 */
const createCounter = (n) => {
	n--;
	return () => {
		n++;
		return n;
	};
};

/** const counter = createCounter(10)
* counter() // 10
* counter() //11
* counter() //12
*/
