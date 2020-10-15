/**
 * Initialize your data structure here.
 */
var MyQueue = function () {
	this.mainStack = [];
	this.minorStack = [];
};

/**
 * Push element x to the back of queue.
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function (x) {
	while (this.mainStack.length > 0) {
		this.minorStack.push(this.mainStack.pop());
	}
	this.mainStack.push(x);
	while (this.minorStack.length > 0) {
		this.mainStack.push(this.minorStack.pop());
	}
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function () {
	return this.mainStack.pop();
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function () {
	return this.mainStack[this.mainStack.length - 1];
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function () {
	return this.mainStack == 0;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

/*
    ES6
*/
class MyQueue {
	constructor() {
		this.mainStack = [];
		this.minorStack = [];
	}
	push(x) {
		while (this.mainStack.length > 0) {
			this.minorStack.push(this.mainStack.pop());
		}
		this.mainStack.push(x);
		while (this.minorStack.length > 0) {
			this.mainStack.push(this.minorStack.pop());
		}
	}
	pop() {
		return this.mainStack.pop();
	}
	peek() {
		return this.mainStack[this.mainStack.length - 1];
	}
	empty() {
		return this.mainStack.length == 0;
	}
}
