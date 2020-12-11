/*
    https://leetcode.com/discuss/interview-question/312500/eBay-phone-screen-Currency-exchange-rate

    We are given a list of list, for a currency exchnage application.
    [["USD","CAD",1.5] , ["CAD", "INR", 50] ,["INR", "BAD", 1.54] ],

    How do you calculate one currency to another currency, that is find the exchange rate? when a method is given such as exchnageValue(currency c1, currency c2)

    followups:
    1. make it a system, the currency can be added/changed in real time
    2. return the best rate for every query
*/
class CurrencyExchange {
    constructor() {
        this.graph = {}
    }
    upsertRate(a, b, rate) {
        if (a in this.graph === false) { this.graph[a] = {} }
        if (b in this.graph === false) { this.graph[b] = {} }
        
        this.graph[a][b] = rate
        this.graph[b][a] = 1.0/rate
    }
    queryRate(a, b) {
        if (a in this.graph === false || b in this.graph === false) {
            return -1
        }
        const seen = new Set()
        const q = [[a, 1.0]]
        while (q.length > 0) {
            const [node, r] = q.shift()
            if (node == b) {
                return r
            }
            if (seen.has(node)) {
                continue
            }
            seen.add(node)
            if (node in this.graph == false) { continue }
            for (let nb in this.graph[node]) {
                q.push([nb, r * this.graph[node][nb]])
            }
        }
        return -1
    }
}

const s = new CurrencyExchange()

s.upsertRate('USD', 'HKD', 8)
s.upsertRate('HKD', 'JPY', 13)
console.log(s.queryRate('USD', 'JPY')) // 104

s.upsertRate('USD', 'HKD', 7.75)
s.upsertRate('HKD', 'JPY', 13)
console.log(s.queryRate('USD', 'JPY')) // 100.75

console.log(s.queryRate('USD', 'CAD')) // -1