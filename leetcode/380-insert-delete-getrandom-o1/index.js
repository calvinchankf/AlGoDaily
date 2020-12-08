/*
    1st: hashtable
    - straight forward approach

    Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		    O(N)
	Space					O(n) the unique keys
    244 ms, faster than 21.56%
*/
class RandomizedSet {
    constructor() {
        this.ht = new Set()
    }
    insert(x) {
        if (this.ht.has(x)) {
            return false
        }
        this.ht.add(x)
        return true
    }
    remove(x) {
        if (this.ht.has(x) == false) {
            return false
        }
        this.ht.delete(x)
        return true
    }
    getRandom() {
        const keys = Array.from(this.ht)
        const n = keys.length
        const i = Math.floor(Math.random() * n)
        return keys[i]
    }
}
/*
    hashtable + array, learned from others
	- save value: index in hashtable
	- when delete, swap the target item and the last item in the array, and remove the last item
    - see ./idea_add.png and ./idea_remove.png
    
    Insert Time				O(1)
	Remove Time				O(1)
	GetRandom Time		    O(1)
	Space					O(n) the unique keys
    120 ms beats 99.01%
*/

/**
 * Initialize your data structure here.
 */
var RandomizedSet = function () {
	this.arr = [];
	this.ht = {};
};

/**
 * Inserts a value to the set. Returns true if the set did not already contain the specified element.
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.insert = function (val) {
	if (val in this.ht) {
		return false;
	}
	const n = this.arr.length;
	this.ht[val] = n;
	this.arr.push(val);
	return true;
};

/**
 * Removes a value from the set. Returns true if the set contained the specified element.
 * @param {number} val
 * @return {boolean}
 */
RandomizedSet.prototype.remove = function (val) {
	if (val in this.ht) {
		const targetIdx = this.ht[val];
		const lastIdx = this.arr.length - 1;
		const lastItem = this.arr[lastIdx];

		// swap
		[
            this.arr[targetIdx], 
            this.arr[lastIdx]
        ] = [
			this.arr[lastIdx],
			this.arr[targetIdx],
		];
		// assign new idx to swapped key which was at the end of array
		this.ht[lastItem] = targetIdx;

		// clear the shits
		delete this.ht[val];
		this.arr.pop();

		return true;
	}
	return false;
};

/**
 * Get a random element from the set.
 * @return {number}
 */
RandomizedSet.prototype.getRandom = function () {
	const n = this.arr.length;
	const idx = Math.floor(Math.random() * n);
	return this.arr[idx];
};
