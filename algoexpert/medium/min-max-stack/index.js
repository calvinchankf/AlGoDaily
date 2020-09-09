// Feel free to add new properties and methods to the class.
class MinMaxStack {
	constructor() {
		this.stack = []; // [iteam, curMin, curMax]
	}

	peek() {
		// Write your code here.
		const n = this.stack.length;
		return this.stack[n - 1][0];
	}

	pop() {
		// Write your code here.
		const [v, curMin, curMax] = this.stack.pop();
		return v;
	}

	push(number) {
		// Write your code here.
		if (this.stack.length > 0) {
			const n = this.stack.length;
			this.stack.push([
				number,
				Math.min(number, this.stack[n - 1][1]),
				Math.max(number, this.stack[n - 1][2]),
			]);
		} else {
			this.stack.push([number, number, number]);
		}
	}

	getMin() {
		// Write your code here.
		const n = this.stack.length;
		return this.stack[n - 1][1];
	}

	getMax() {
		// Write your code here.
		const n = this.stack.length;
		return this.stack[n - 1][2];
	}
}

// Do not edit the line below.
exports.MinMaxStack = MinMaxStack;
