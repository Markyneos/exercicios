/**
 * @param {Array.<number>} list1 An array of numbers to be added to another.
 * @param {Array.<number>} list2 An array of numbers to be added to another.
 */

const sumTwoArrays = (list1, list2) => {
	let sum = 0;
	for (let i = 0; i < list1.length; i++) {
		sum += list1[i];
	}
	for (let i = 0; i < list2.length; i++) {
		sum += list2[i];
	}
	let media = sum / (list1.length + list2.length);
	return media;
}

console.log(sumTwoArrays([1, 2, 3], [4, 5, 6]));
