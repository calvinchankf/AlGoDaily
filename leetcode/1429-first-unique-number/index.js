/*
    2nd: queue + hashtable
    - not a very optimal approach
    - counter the occurence of each number
    - when we do showFirstUnique(), pop the queue until we reach to a number which appears once only

    Time of init                O(N)
    Time of showFirstUnique()   O(N)
    Time of add()               O(1)
    Space                       O(N)
    1064 ms, faster than 23.39%
*/
class FirstUnique {
    constructor(nums) {
        this.counter = {}
        this.queue = []
        
        for (let x of nums) {
            if ((x in this.counter) == false) {
                this.counter[x] = 0
            }
            this.counter[x] += 1
        }
        
        for (let x of nums) {
            if (this.counter[x] == 1) {
                this.queue.push(x)
            }
        }
    }
    showFirstUnique() {
        this._findUnique()
        if (this.queue.length > 0) {
            return this.queue[0]
        }
        return -1
    }
    add(x) {
        if (x in this.counter) {
            this.counter[x] += 1
        } else {
            this.counter[x] = 1
            this.queue.push(x)
        }
    }
    _findUnique() {
        while (
            this.queue.length > 0 &&
            this.counter[this.queue[0]] > 1
        ) {
            this.queue.shift()
        }
    }
}

/*
    3rd: array + hashtable

    Time of init                O(N)
    Time of showFirstUnique()   O(N)
    Time of add()               O(1)
    Space                       O(N)
    376 ms, faster than 79.03%
*/
class FirstUnique {
    constructor(nums) {
        this.counter = {}
        this.nums = [...nums]
        this.firstUniqueIdx = 0

        for (let x of nums) {
            if ((x in this.counter) == false) {
                this.counter[x] = 0
            }
            this.counter[x] += 1
        }
        this._findUnique()
    }
    showFirstUnique() {
        if (this.firstUniqueIdx < this.nums.length) {
            return this.nums[this.firstUniqueIdx]
        }
        return -1
    }
    add(x) {
        if (x in this.counter) {
            this.counter[x] += 1
            this._findUnique()
        } else {
            this.counter[x] = 1
            this.nums.push(x)
        }
    }
    _findUnique() {
        while (this.firstUniqueIdx < this.nums.length) {
            const x = this.nums[this.firstUniqueIdx]
            if (this.counter[x] == 1) {
                break
            }
            this.firstUniqueIdx += 1
        }
    }
}