/**
 * // This is Sea's API interface.
 * // You should not implement it, or speculate about its implementation
 * function Sea() {
 *     @param {integer[]} topRight
 *     @param {integer[]} bottomLeft
 *     @return {boolean}
 *     this.hasShips = function(topRight, bottomLeft) {
 *         ...
 *     };
 * };
 */


/*
    1st: BFS + binary search <- iterative
    - divide 1 grid into 4 grids
    - when the left = right and top = bottom, we reach to a point where a ship is
    - see ./idea.png

    Time    O(klogRC)   k = 10 in this problem
    Space   O(klogRC)   the size of queue
    92 ms, faster than 35.90%
*/
var countShips = function(sea, topRight, bottomLeft) {
    let count = 0
    const q = [[topRight, bottomLeft]]
    while (q.length > 0) {
        const [_topRight, _bottomLeft] = q.shift()
        
        if ( _topRight[0] < _bottomLeft[0] || _topRight[1] < _bottomLeft[1] ) {
            continue
        }
        
        const hasShips = sea.hasShips(_topRight, _bottomLeft)
        if (hasShips == false) { continue }
        
        if (_topRight[0] == _bottomLeft[0] && _topRight[1] == _bottomLeft[1]) {
            count += 1
        } else {
            const midX = Math.floor((_topRight[0] + _bottomLeft[0]) / 2)
            const midY = Math.floor((_topRight[1] + _bottomLeft[1]) / 2)

            q.push([ _topRight, [midX + 1, midY + 1] ])
            q.push([ [_topRight[0], midY], [midX + 1, _bottomLeft[1]] ])
            q.push([ [midX, midY], _bottomLeft ])
            q.push([ [midX, _topRight[1]], [_bottomLeft[0], midY + 1] ])
        }
    }
    return count
};