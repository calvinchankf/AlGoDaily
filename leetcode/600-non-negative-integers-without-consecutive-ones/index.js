/*
    1st: binary string contruction
    - it works in JS but fails in python

    Time    O(logN) -> O(N)
    Space   O(logN) -> O(N)
    6112 ms, faster than 20.00%
*/
var findIntegers = function(L) {
    if (L < 1) {
        return 0
    }
    let res = 1
    
    const dfs = cur => {
        if (cur > L) {
            return
        }
        res += 1
        if (cur % 2 == 0) {
            dfs(2 * cur)
            dfs(2 * cur + 1)
        } else {
            dfs(2 * cur)
        }
    }
    dfs(1)
    
    return res
};
