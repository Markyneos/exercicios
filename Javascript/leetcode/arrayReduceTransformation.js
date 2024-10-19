/**
 * @param {Array.<number>} nums
 * @param {Function} fn
 * @param {number} init
 * @returns {number}
 */
const reduce = (nums, fn, init) => {
	if (nums.length === 0) {
		return init;
	}
	let val = fn(init, nums[0]);
	for (let i = 1; i < nums.length; i++) {
		val = fn(val, nums[i]);
	}
	return val;
}
