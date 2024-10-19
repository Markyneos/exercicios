/**
 * @param {number} init
 * @returns { increment: Function, decrement: Function, reset: Function } 
 */
const createCounter = (init) => {
	let num = init;
	return {
		increment: () => {
			num++;
			return num;
		},
		decrement: () => {
			num--;
			return num;
		},
		reset: () => {
			num = init;
			return num;
		}
	}
};

//const counter = createCounter(5);
//console.log(counter.increment()); // 6
//console.log(counter.reset()); // 5
//console.log(counter.decrement()) // 4

