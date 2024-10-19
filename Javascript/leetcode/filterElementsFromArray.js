/**
 * @param {Array.<number>} arr
 * @param {Function} fn
 * @returns {number[]}
 */
const filter = (arr, fn) => {
	let filteredArr = [];
	arr.forEach((item, index) => {
		if (fn(item, index)) {
			filteredArr.push(item);
		};
	});
	return filteredArr;
}
