/*
    ref:
    - https://leetcode.com/discuss/interview-question/algorithms/233248/calculate-the-cheapest-price-for-the-item-during-the-day-within-different-time-intervals

    There is a shop, where vendors sell items. 
    They all sell same item but they can change the price of the item during the day. 
    Given intervals of time and a lower price for the item during this interval for each vendor, 
    calculate the cheapest price for the item during the day within different time intervals. 
    Input data for each vendor is {startTime, endTime, price}. 
    
    e.g.1
    Input
    [[0, 4, 5], [2, 8, 3], [7, 11, 10]]
    Output
    [[0, 2, 5], [2, 8, 3], [8, 11, 10]]

    e.g.2
    Input
    [[1, 5, 20], [4, 6, 30], [5, 8, 10]]
    Output
    [[1, 5, 20], [5, 8, 10]]

    e.g.3
    Input
    [[1, 10, 20], [4, 6, 10]]
    Ouput
    [[1, 4, 20], [4, 6, 10], [6, 10, 20]]
*/

/*
    corner cases:
    - a grid within another grid: [[1,5,10], [2,3,5]] 
    - 2 consecutive grids with same height: [[1,2,10], [2,3,10]] ? merge intervals first
*/
const mergeIntervalsWithLowerPrice = (intervals) => {
    intervals.sort((a, b) => a[0] - b[0])
    const res = []
    for (let [s, e, p] of intervals) {
        const n = res.length
        if (n > 0 && s <= res[n-1][1]) {
            if (p < res[n-1][2]) {
                if (e < res[n-1][1]) {
                    // within
                    const lastE = res[n-1][1]
                    const lastP = res[n-1][2]
                    res[n-1][1] = s
                    res.push([s, e, p])
                    res.push([e, lastE, lastP])
                } else {
                    // not within
                    res[n-1][1] = s
                    res.push([s, e, p])
                }
            } else {
                // extend and taller
                const lastE = res[n-1][1]
                res.push([lastE, e, p])
            }
        } else {
            res.push([s, e, p])
        }
    }
    return mergeIntervals(res)
}

const mergeIntervals = (intervals) => {
    const res = []
    for (let [s, e, p] of intervals) {
        if (e <= s) {
            continue
        }
        const n = res.length
        if (n > 0 && s <= res[n-1][1] && p == res[n-1][2]) {
            res[n-1][1] = Math.max(res[n-1][1], e)
        } else {
            res.push([s, e, p])
        }
    }
    return res
}

let a

// eg1
a = [[0, 4, 5], [2, 8, 3], [7, 11, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// eg2
a = [[1, 5, 20], [4, 6, 30], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// eg3: split
a = [[1, 10, 20], [4, 6, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// same end => [[1, 5, 20], [5, 8, 10]]
a = [[1, 5, 20], [4, 5, 30], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// same start => [[1, 5, 20], [5, 8, 10]]
a = [[1, 5, 20], [5, 6, 30], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// higher within => [[1, 5, 20], [5, 8, 10]]
a = [[1, 5, 20], [3, 4, 30], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// shorter within => [[1, 3, 20], [3, 4, 1], [4, 5, 20], [5, 8, 10]]
a = [[1, 5, 20], [3, 4, 1], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// consecutive grids with same height => [[1, 8, 20]]
a = [[1, 5, 20], [5, 8, 20]]
console.log(mergeIntervalsWithLowerPrice(a))

// consecutive grids with same height => [[1, 8, 20]]
a = [[1, 5, 20], [4, 5, 30], [5, 8, 20]]
console.log(mergeIntervalsWithLowerPrice(a))