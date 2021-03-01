/*
    API rate limiting

    expect:
    function: abc() 
    properties: names, userId, ip...etc

    interval: threshold, window
    e.g.
    5 times(threshold) within 10 sec(window) for (userId, apiMethod)
    
    {
        "calvin,getTimeline,room": count 4->5

    }

    0 - 10
    11 - 20
    21 - 30
    ...

    8%10  = 0
    10%10 = 0
    11%10 = 1
    19%10 = 1
    21%10 = 2

    9s calvin -> getTimeline() ok
    9s calvin -> getTimeline() ok 9 - 10 = -1
    9s calvin -> getTimeline() ok
    9s calvin -> getTimeline() ok
    9s calvin -> getTimeline() ok
    11s calvin -> getTimeline() not ok 11 - 10 = 1 < 9

    datastream
    {
        calvin: 1
    }

    2 - 10 = -8
*/
class RateLimiting {
    constructor(threshold, window) {
        this.threshold = threshold
        this.window = window
        this.ht = {}
    }
    hit(fn, userId, timestamp) {
        const room = Math.floor(timestamp / this.window)
        const key = `${userId},${fn.name},${room}`
        if (key in this.ht) {

            const count = this.ht[key]
            if (count < this.threshold) {
                fn()
                this.ht[key] += 1
                return true
            } else {
                return false
            }

        } else {
            fn()
            this.ht[key] = 1
            return true
        }
    }
}

const haha = () => {
    // console.log('haha')
}

let rl = new RateLimiting(5, 10)

let a;
let b = 'calvin'

console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 11))

console.log("----")

rl = new RateLimiting(5, 10)

console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 11))

console.log("----")

let c = 'catherine'
rl = new RateLimiting(5, 10)

console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))
console.log(rl.hit(haha, b, 9))

console.log(rl.hit(haha, c, 9))
console.log(rl.hit(haha, c, 9))
console.log(rl.hit(haha, c, 9))
console.log(rl.hit(haha, c, 9))
console.log(rl.hit(haha, c, 9))
console.log(rl.hit(haha, c, 9))

console.log(rl.hit(haha, b, 11))