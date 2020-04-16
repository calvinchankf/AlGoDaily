/*
    1st: save the minValue for every item
    - for each push(), calculate the curMin and put it with the x in stack
    - for each pop(), pop the top item

    Time    O(n)
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
	if (this.arr.length == 0) {
		return this.arr.push([x, x]);
	}
	prevMin = this.arr[this.arr.length - 1][1];
	newMin = Math.min(prevMin, x);
	return this.arr.push([x, newMin]);
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
	return this.arr[this.arr.length - 1][0];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
	return this.arr[this.arr.length - 1][1];
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
