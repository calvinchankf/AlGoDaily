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
const mergeIntervalsWithLowerPrice = (intervals) => {
    intervals.sort((a, b) => a[0] - b[0])
    const intvs = []
    for (let [s, e, p] of intervals) {
        const n = intvs.length
        if (n > 0 && s < intvs[n-1][1]) {
            if (p < intvs[n-1][2]) {
                if (e < intvs[n-1][1]) {
                    const lastE = intvs[n-1][1]
                    const lastP = intvs[n-1][2]
                    intvs[n-1][1] = s
                    intvs.push([s, e, p])
                    intvs.push([e, lastE, lastP])
                } else {
                    intvs[n-1][1] = s
                    intvs.push([s, e, p])
                }
            } else {
                const lastE = intvs[n-1][1]
                intvs.push([lastE, e, p])
            }
        } else {
            intvs.push([s, e, p])
        }
    }
    return intvs.filter(x => x[0] < x[1])
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

// same end
a = [[1, 5, 20], [4, 5, 30], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// same start
a = [[1, 5, 20], [5, 6, 30], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// higher within 1
a = [[1, 5, 20], [3, 4, 30], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))

// higher within 2
a = [[1, 5, 20], [3, 4, 30], [5, 8, 10]]
console.log(mergeIntervalsWithLowerPrice(a))