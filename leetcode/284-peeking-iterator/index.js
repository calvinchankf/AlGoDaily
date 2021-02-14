/**
 * // This is the Iterator's API interface.
 * // You should not implement it, or speculate about its implementation.
 * function Iterator() {
 *    @ return {number}
 *    this.next = function() { // return the next number of the iterator
 *       ...
 *    }; 
 *
 *    @return {boolean}
 *    this.hasNext = function() { // return true if it still has numbers
 *       ...
 *    };
 * };
 */

/*
    1st: buffer?

    Time    O(1)
    Space   O(1)
*/
class PeekingIterator {
    constructor(iterator) {
        this.iterator = iterator
        this.cur = null
        if (this.iterator.hasNext()) {
            this.cur = this.iterator.next()
        }
    }
    peek() {
        return this.cur
    }
    next() {
        const res = this.cur
        if (this.iterator.hasNext()) {
            this.cur = this.iterator.next()
        } else {
            this.cur = null
        }
        return res
    }
    hasNext() {
        return this.cur != null
    }
}