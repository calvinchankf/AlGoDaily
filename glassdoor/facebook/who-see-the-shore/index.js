/*
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=676442&ctid=230547
    There is a list of buildings, the right hand side of the buildings is the shore. Return a list of buildings that they can see the shore.

    - I assume that all the heights are positive

    Time    O(N)
    Space   O(1)
*/
const whoSeeTheShore = (nums) => {
    let peak = 0
    const res = []
    for (let i = nums.length - 1; i >= 0; i--) {
        const x = nums[i]
        if (x > peak) {
            res.push(x)
            peak = x
        }
    }
    return res
}

let a 

a = [6, 5, 4, 3, 2, 1]
console.log(whoSeeTheShore(a))

a = [8, 5, 7, 2, 3, 6, 1]
console.log(whoSeeTheShore(a))