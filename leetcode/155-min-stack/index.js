/*
    1st: save the minValue for every item
    - for each push(), calculate the curMin and put it with the x in stack
    - for each pop(), pop the top item

    Time    O(1)
    Space   O(n)
    100ms beats 85.92%
*/

/**
 * initialize your data structure here.
 */
var MinStack = function () {
	this.arr = [];
};

/**
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function (x) {
	const n = this.arr.length;
	if (n == 0) {
		return this.arr.push([x, x]);
	}
	const newMin = Math.min(this.arr[n - 1][1], x);
	this.arr.push([x, newMin]);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
	return this.arr.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
	const n = this.arr.length;
	return this.arr[n - 1][0];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
	const n = this.arr.length;
	return this.arr[n - 1][1];
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */

/*
    ES6 class of 1st

    Time of all methods     O(1)
    Space                   O(N)
    124 ms, faster than 64.04%
*/
class MinStack {
	constructor() {
		this.arr = [];
	}
	push(x) {
		const n = this.arr.length;
		if (n == 0) {
			return this.arr.push([x, x]);
		}
		const newMin = Math.min(this.arr[n - 1][1], x);
		this.arr.push([x, newMin]);
	}
	pop() {
		return this.arr.pop();
	}
	top() {
		const n = this.arr.length;
		return this.arr[n - 1][0];
	}
	getMin() {
		const n = this.arr.length;
		return this.arr[n - 1][1];
	}
}
