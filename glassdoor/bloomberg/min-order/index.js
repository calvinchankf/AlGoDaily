/*
    https://leetcode.com/discuss/interview-question/506270/Bloomberg-or-Phoneor-Min-order

    Leetcode problem https://leetcode.com/problems/min-stack/

    Problem Description
    Imagine you are a Front Office trader, whose job is to execute trades. 
    To simplify things, you only trade a single stock, and the only input you receive for each trade is the amount.

    As your Back Office is really impatient, you need to execute the trades in order, such that the last request you have received is executed first. 
    Additionally, once in a while, your Back Office may ask you about th eminimal order you have, that is not executed yet.

    Design a data structure, that can help you solve these tasks. Implement a data structure that supports the following operations:

    - addOrder(int amount) : adds an order
    - executeOrder() : executes an Order (according to the rules above) and returns the amount associated with it
    - extractMinOrder() : returns the amount of the current minimal order, without executing it
    For converience all amounts can be assumed to be integers.

    Sample inputs - Expected outputs
    Below extractMin refers to the extractMinOrder.

    addOrder(13), addOrder(11), addOrder(9), addOrder(20)

    extractMin() -> 9
    executeOrder() -> 20
    extractMin() -> 9
    executeOrder() -> 9
    extractMin() -> 11
    addOrder(11)
    extractMin() -> 11
    executeOrder() -> 11
    extractMin() -> 11
    executeOrder() -> 11
    extractMin() -> 13
    executeOrder() -> 13
*/
class MinOrder {
    constructor() {
        this.stack = [] // (curNum, minNum) 
    }
    addOrder(order) {
        const n = this.stack.length
        if (n == 0) {
            return this.stack.push([order, order])
        }
        const minNum = Math.min(this.stack[n - 1][1], order)
        this.stack.push([order, minNum])
    }
    executeOrder() {
        const n = this.stack.length
        if (n == 0) {
            return -1
        }
        const [lastOrder, _] = this.stack.pop()
        return lastOrder
    }
    extractMinOrder() {
        const n = this.stack.length
        if (n == 0) {
            return -1
        }
        return this.stack[n - 1][1]
    }
}