/*
    2nd: iterative (reversed) inorder traversal, one-pass

    Time    O(N)
    Space   O(n)
    116 ms, faster than 58.12%
*/
var convertBST = function (root) {
	if (!root) {
        return null
    }
    let total = 0
    let cur = root
    const stack = []
    while (cur != null || stack.length > 0) {
        while (cur != null) {
            stack.push(cur)
            cur = cur.right
        }
        const node = stack.pop()
        total += node.val
        node.val = total
        cur = node.left
    }
    return root
};
