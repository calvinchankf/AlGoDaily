/*
    1st: array
    - for each position, move all chips to here and see how much does it cost

    Time    O(N^2)
    Space   O(N^2)
    76 ms, faster than 64.42%
*/
var minCostToMoveChips = function(position) {
    let res = 2**32
    for (let i = 0; i < position.length; i++) {
        let cost = 0
        for (let j = 0; j < position.length; j++) {
            if (i == j) {
                continue
            }
            let diff = Math.abs(position[i] - position[j])
            if (diff%2 == 1) {
                cost += 1
            }
        }
        res = Math.min(res, cost)
    }
    return res
};