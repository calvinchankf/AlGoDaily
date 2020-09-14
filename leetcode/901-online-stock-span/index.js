/*
    1st: brute force
*/
var StockSpanner = function () {
	this.stack = [];
};
StockSpanner.prototype.next = function (price) {
	this.stack.push(price);
	let i = 0;
	while (1) {
		const n = this.stack.length;
		if (this.stack[n - 1 - i] <= price) {
			i += 1;
		} else {
			break;
		}
	}
	return i;
};

/*
    2nd: stack

    e.g. [100, 80, 60, 70, 60, 75, 85]
    when next(100), stack = [100:1
    when next(80),  stack = [100:1, 80: 1
    when next(60),  stack = [100:1, 80: 1, 60: 1
    when next(70),  stack = [100:1, 80: 1, 70: 2
    when next(60),  stack = [100:1, 80: 1, 70: 2, 60: 1
    when next(75),  stack = [100:1, 80: 1, 75: 4
    when next(85),  stack = [100:1, 85: 6

    Time of next()      O(n) at worse but average O(1) because stock prices flutuate
    Space               O(n)
    332 ms, faster than 86.67% 
*/
var StockSpanner = function () {
	this.stack = [];
};
StockSpanner.prototype.next = function (price) {
	let weight = 1;
	while (
		this.stack.length > 0 &&
		this.stack[this.stack.length - 1][0] <= price
	) {
		const pop = this.stack.pop();
		weight += pop[1];
	}
	this.stack.push([price, weight]);
	return weight;
};
