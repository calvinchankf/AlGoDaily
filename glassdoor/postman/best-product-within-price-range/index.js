/*
    https://leetcode.com/discuss/interview-question/370770/Postman-or-HackerEarth-or-Software-Engineering-Intern-or-Bengaluru-India
    You want to buy a laptop. Each laptop has two parameters: Rating & Price. 
    Your task is to buy a laptop with the highest rating within a given price range. 
    Given Q tasks, each query consisting of price range required, 
    you have to print the highest rated laptop that can be bought within that price range.
    e.g.
    Input
    pricesAndRatings = [
        [1100, 299],
        [1000, 300],
        [1300, 200],
        [1700, 500],
        [2000, 600]
    ]
    queries = [
        [1000, 1400],
        [1700, 1900],
        [0, 2000],
    ]
    Output:
    [400, 500, 600]
    Note: If you cannot get any laptop within the range, print -1.
*/
const f = (pricesAndRatings, queries) => {
    pricesAndRatings.sort((a, b) => a[0] - b[0])
    console.log(pricesAndRatings)
    const res = []
    for (let [left, right] of queries) {
        const leftIdx = lowerBsearch(pricesAndRatings, left)
        const rightIdx = upperBsearch(pricesAndRatings, right) - 1
        let maxRating = -1
        if (leftIdx <= rightIdx) {
            for (let i = leftIdx; i <= rightIdx; i++) {
                if (pricesAndRatings[i][1] > maxRating) {
                    maxRating = pricesAndRatings[i][1]
                }
            }
        }
        res.push(maxRating)
    }
    return res
}

const lowerBsearch = (objs, target) => {
    let left = 0
    let right = objs.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target <= objs[mid][0]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}

const upperBsearch = (objs, target) => {
    let left = 0
    let right = objs.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target >= objs[mid][0]) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}

const a = [
    [1100, 299],
    [1000, 300],
    [1300, 200],
    [1700, 500],
    [2000, 600]
]
const b = [
    [1000, 1400],
    [1700, 1900],
    [0, 2000],
]
console.log(f(a, b))