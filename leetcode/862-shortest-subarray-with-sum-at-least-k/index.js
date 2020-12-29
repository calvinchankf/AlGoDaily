/*
    2nd: dequeue
    - calculate prefix sum at every index
    - while prefixSum[i] - q[0][0] >= K, subtract the dequeue from the left
    - while prefixSum[i] <= q[-1][0], pop q[-1] and add prefixSum[i] to the queue.
    *** The reason is, if the current prefixSum[i] is smaller than q[-1][0], 
    *** then prefixSum[future] can just subtract prefixSum[i] to get a shorter subarray
    
    e.g. [1, 1, 1, 5, -2, -3, 4, 3, 6]
    pfs   1  2  3  8   6   3  7 10 16
    idx   0  1  2  3   4   5  6  7 8

    deq []
        [(0, 0)]
        [(0, 0), (1, 1)]
        [(0, 0), (1, 1), (2, 2)]
        [(0, 0), (1, 1), (2, 2), (3, 3)]
        [(2, 2), (3, 3), (8, 4)]
        [(2, 2), (3, 3), (6, 5)]
        [(2, 2), (3, 6)]
        [(2, 2), (3, 6), (7, 7)]
        [(7, 7), (10, 8)]                   <- final result = 8 - 6 = 2
        [(10, 8), (16, 9)]

    ref:
    - https://www.cnblogs.com/grandyang/p/11300071.html

    Time    O(N)
    Space   O(N)
    1288 ms, faster than 57.41%
*/
var shortestSubarray = function(A, K) {
    const pfss = [0]
    let pfs = 0
    for (let x of A) {
        pfs += x
        pfss.push(pfs)
    }
    const deq = []
    let res = 2**32
    for (let i = 0; i < pfss.length; i++) {
        while (deq.length > 0 && pfss[i] - deq[0][0] >= K) {
            const [_, j] = deq.shift()
            res = Math.min(res, i - j)
        }
        while (deq.length > 0 && pfss[i] <= deq[deq.length-1][0]) {
            deq.pop()
        }
        deq.push([pfss[i], i])
    }
    if (res == 2**32) { return -1 }
    return res
};