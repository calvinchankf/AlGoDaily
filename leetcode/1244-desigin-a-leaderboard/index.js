/*
    1st: binary search + hashtable

    - maintain an array to store the ids sorted by scores
    - a hashtable to store the relation for every {id: score}

    Time of addScore()      O(k), it can be O(logN) depends on language becos of array.insert()
    Time of top()           O(k)
    Time of reset()         O(N) binary search + linear search
    Space                   O(2N)
    96 ms, faster than 92.31%
*/
var Leaderboard = function() {
    this.arr = []   // ids sort by scores
    this.ht = {}    // {id1: score1, id2: score2}
};
Leaderboard.prototype.addScore = function(playerId, score) {
    let newScore = 0
    if (playerId in this.ht) {
        newScore = this.ht[playerId] + score
        this.ht[playerId] = newScore
        // remove
        const i = this.arr.indexOf(playerId)
        this.arr.splice(i, 1)
    } else {
        this.ht[playerId] = score
        newScore = score
    }
    // add
    const j = upperBsearch(this.arr, this.ht, newScore)
    this.arr.splice(j, 0, playerId)
};
Leaderboard.prototype.top = function(K) {
    let res = 0
    let count = 0
    for (let i = this.arr.length-1; i >= 0; i--) {
        const pId = this.arr[i]
        res += this.ht[pId]
        count += 1
        if (count === K) { break }
    }
    return res
};
Leaderboard.prototype.reset = function(playerId) {
    const i = this.arr.indexOf(playerId)
    this.arr.splice(i, 1)
    delete this.ht[playerId]
};
const upperBsearch = (arr, ht, target) => {
	let left = 0;
	let right = arr.length;
	while (left < right) {
		const mid = Math.floor((left + right) / 2);
        const pId = arr[mid]
		if (target >= ht[pId]) {
			left = mid + 1;
		} else {
			right = mid;
		}
	}
	return left;
};

/*
    in ES6

    Time of addScore()      O(k), it can be O(logN) depends on language becos of array.insert()
    Time of top()           O(k)
    Time of reset()         O(N) binary search + linear search
    Space                   O(2N)
    96 ms, faster than 92.31%
*/
class Leaderboard {
    constructor() {
        this.arr = []   // ids sort by scores
        this.ht = {}    // {id1: score1, id2: score2}
    }
    addScore(playerId, score) {
        let newScore = 0
        if (playerId in this.ht) {
            newScore = this.ht[playerId] + score
            this.ht[playerId] = newScore
            // remove
            const i = this.arr.indexOf(playerId)
            this.arr.splice(i, 1)
        } else {
            this.ht[playerId] = score
            newScore = score
        }
        // add
        const j = this._upperBsearch(this.arr, this.ht, newScore)
        this.arr.splice(j, 0, playerId)
    }
    top(K) {
        let res = 0
        let count = 0
        for (let i = this.arr.length-1; i >= 0; i--) {
            const pId = this.arr[i]
            res += this.ht[pId]
            count += 1
            if (count === K) { break }
        }
        return res
    }
    reset(playerId) {
        const i = this.arr.indexOf(playerId)
        this.arr.splice(i, 1)
        delete this.ht[playerId]
    }
    _upperBsearch(arr, ht, target) {
        let left = 0;
        let right = arr.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            const pId = arr[mid]
            if (target >= ht[pId]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    };
}