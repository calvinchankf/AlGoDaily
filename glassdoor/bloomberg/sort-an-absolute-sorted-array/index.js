/*
    https://leetcode.com/discuss/interview-question/951073/Bloomberg-or-Onsite-or-Maximum-path-sum

    Given an array sorted by its absolute values, return sorted array by it actually values (less than NlgN)
    
    Input
    [0, -1, 2, -4, 5, 6, -10, -13, -22]
    
    Output
    [-22, -13, -10, -4, -1,0, 2, 5, 6]
*/
const sortAbsSortedArray = (nums) => {
    /*
        approach:
        negatives = [-1, -4, -10, -13, -22]
        positive  = [0, 2, 5, 6]

        result = negatives[::-1] + positive
    */
    const negs = []
    const poss = []
    nums.forEach(x => {
        if (x >= 0) {
            poss.push(x)
        } else {
            negs.push(x)
        }
    });
    // return [...negs.reverse(), ...poss]
    return negs.reverse().concat(poss)
}

let a

a = [0, -1, 2, -4, 5, 6, -10, -13, -22]
console.log(sortAbsSortedArray(a))