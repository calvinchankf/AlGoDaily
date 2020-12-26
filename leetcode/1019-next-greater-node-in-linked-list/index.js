/*
    1st approach: stack
    - similar to lc503

    Time    O(2n)
    Space   O(n)
    152 ms, faster than 73.21%
*/
var nextLargerNodes = function(head) {
    const ht = {}
    const stack = []
    let cur = head
    let i = 0
    while (cur != null) {
        while (stack.length > 0 && cur.val > stack[stack.length-1][0]) {
            const [val, idx] = stack.pop()
            ht[idx] = cur.val
        }
        stack.push([cur.val, i])
        i += 1
        cur = cur.next
    }
    const res = []
    for (let j = 0; j < i; j++) {
        if (j in ht) {
            res.push(ht[j])
        } else {
            res.push(0)
        }
    }
    return res
};