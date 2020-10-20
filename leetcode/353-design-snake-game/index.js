/*
    2nd approach: orderdict
    - optimize the 1st: dont declare the grid
    - there is no orderdict in js, we can do it with a hashtable + an array

    be careful of this corner case:
    0HX
    0TX
    000

    H: head
    T: tail
    X: body

    it allows the snake move from (0,1) to (1,1)

    Time of move()  O(1)
    Time of init()  O(RC)
    Space           O(RC)
    232 ms, faster than 85.96%
*/
var SnakeGame = function (width, height, food) {
	this.width = width;
	this.height = height;
	this.food = food;
	this.foodIdx = 0;
	this.snakeBodyHt = new Set(["0,0"]);
	this.snakeBody = [[0, 0]];
};

SnakeGame.prototype.move = function (direction) {
	let di = 0;
	let dj = 0;
	if (direction == "U") {
		di = -1;
	} else if (direction == "D") {
		di = 1;
	} else if (direction == "R") {
		dj = 1;
	} else if (direction == "L") {
		dj = -1;
	}
	const n = this.snakeBody.length;
	const x = this.snakeBody[n - 1][0] + di;
	const y = this.snakeBody[n - 1][1] + dj;
	const key = `${x},${y}`;
	// check boundary
	if (x < 0 || x == this.height || y < 0 || y == this.width) {
		return -1;
	}
	// check if can score
	if (
		this.foodIdx < this.food.length &&
		x == this.food[this.foodIdx][0] &&
		y == this.food[this.foodIdx][1]
	) {
		this.snakeBody.push([x, y]);
		this.snakeBodyHt.add(key);
		this.foodIdx += 1;
		return this.snakeBody.length - 1;
	}
	// remove the tail first, because the snake can traverse in a close circle
	const [tailI, tailJ] = this.snakeBody.shift();
	const tailKey = `${tailI},${tailJ}`;
	this.snakeBodyHt.delete(tailKey);
	// check if body collision
	if (this.snakeBodyHt.has(key)) {
		return -1;
	}
	// add head
	this.snakeBody.push([x, y]);
	this.snakeBodyHt.add(key);
	return this.snakeBody.length - 1;
};
