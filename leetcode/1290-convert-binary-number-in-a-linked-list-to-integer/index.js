/*
    2nd:
    - do math directly to compute the result
    e.g. 1011
    2*0 + 1 = 1
    2*1 + 0 = 2
    2*2 + 1 = 5
    2*5 + 1 = 11

    Time    O(2N)
    Space   O(1)
    80ms beats 80ms
*/
var getDecimalValue = function(head) {
    let res = 0
    let cur = head
    while (cur !== null) {
        res = res * 2 + cur.val
        cur = cur.next
    }
    return res
};