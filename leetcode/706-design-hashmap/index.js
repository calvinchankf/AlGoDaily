/*
    2nd approach:
    - 1000 buckets
    - each bucket has 1000 slots

    however, there is a limition of total number of items inserted into the hashtable

    700 ms, faster than 5.01%
*/
class MyHashMap {
    constructor() {
        this.buckets = []
        for (let i = 0; i < 1000; i++) {
            this.buckets.push(Array(1000).fill(null))
        }
    }
    _getBucketIdx(key) {
        return Math.floor(key / 1000)
    }
    _getSlotIdx(key) {
        return key % 1000
    }
    put(key, value) {
        const b = this._getBucketIdx(key)
        const s = this._getSlotIdx(key)
        this.buckets[b][s] = value
    }
    get(key) {
        const b = this._getBucketIdx(key)
        const s = this._getSlotIdx(key)
        if (this.buckets[b][s] == null) {
            return -1
        }
        return this.buckets[b][s]
    }
    remove(key) {
        const b = this._getBucketIdx(key)
        const s = this._getSlotIdx(key)
        this.buckets[b][s] = null
    }
}