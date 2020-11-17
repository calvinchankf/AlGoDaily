/*
    1st: math, brute force
    - very annoying constrain: lexicographically minimum coordinate

    Time    O(TRR)
    Space   O(RR)
    1140 ms, faster than 100.00%
*/
var bestCoordinate = function(towers, radius) {
    const cands = {}
    for (let t of towers) {
        const [x, y, q] = t
        for (let _x = -radius - x; _x <= radius + x; _x++) {
            for (let _y = -radius - y; _y <= radius + y; _y++) {
                const d = getDistance(x, y, _x, _y)
                if (d <= radius) {
                    const key = `${_x},${_y}`
                    cands[key] = [_x, _y]
                }
            }
        }
    }
    
    let res = [0,0]
    let maxQ = 0
    for (let key in cands) {
        const [_x, _y] = cands[key]
        let quality = 0
        for (let t of towers) {
            const [x, y, q] = t
            const d = getDistance(x, y, _x, _y)
            if (d <= radius) {
                quality += Math.floor(q / (1 + d))
            }
        }
        
        if (quality > maxQ) {
            maxQ = quality
            res = [_x, _y]
        } else if (quality === maxQ) {
            if (_x < res[0] || _x == res[0] && _y < res[1]) {
                res = cands[key]
            }
        }
    }
    return res
};

const getDistance = (x, y, _x, _y) => {
    return Math.sqrt((_x - x)**2 + (_y - y)**2)
}