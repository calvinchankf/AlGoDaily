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
class RandomizedSet {
    constructor() {
        this.ht = {}
        this.nums = []
    }
    insert(x) {
        if (x in this.ht) {
            return false
        }
        this.ht[x] = this.nums.length
        this.nums.push(x)
        return true
    }
    remove(x) {
        if (x in this.ht == false) {
            return false;
        }
        const i = this.ht[x];
        const last = this.nums[this.nums.length-1];
        const j = this.ht[last];
        
        [this.nums[i], this.nums[j]] = [this.nums[j], this.nums[i]];
        this.ht[last] = i;
        
        this.nums.pop();
        delete this.ht[x];
        
        return true;
    }
    getRandom() {
        const i = Math.floor(Math.random() * this.nums.length)
        return this.nums[i]
    }
}