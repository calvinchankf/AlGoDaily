/*
    1st: DFS brute force
    - get all the paths
    - see if each path has substring of linked list

    Time    O(L + T^2)
    Space   O(L+T)
    372 ms, faster than 5.13%
*/
var isSubPath = function(head, root) {
    const path = []
    let cur = head
    while (cur != null) {
        path.push(cur.val)
        cur = cur.next
    }
    const target = path.join(',')
    
    const paths = []
    const stack = [[root, [root.val]]]
    while (stack.length > 0) {
        const [node, path] = stack.pop()
        if (node.left == null && node.right == null) {
            paths.push(path.join(','))
        }
        if (node.left) {
            stack.push([node.left, path.concat(node.left.val)])
        }
        if (node.right) {
            stack.push([node.right, path.concat(node.right.val)])
        }
    }
    
    for (let p of paths) {
        if (p.indexOf(target) > -1) {
            return true
        }
    }
    return false
};

/*
    2nd: DFS
    - get all the paths
    - see if each path has substring of linked list
    - optimize the time to get the path string

    Time    O(L + T)
    Space   O(L+T)
    124 ms, faster than 16.67%
*/
var isSubPath = function(head, root) {
    const path = []
    let cur = head
    while (cur != null) {
        path.push(cur.val)
        cur = cur.next
    }
    const target = path.join(',')
    
    const paths = []
    const stack = [[root, '']]
    while (stack.length > 0) {
        const [node, path] = stack.pop()
        const newPath = `${path},${node.val}`
        if (node.left == null && node.right == null) {
            paths.push(newPath)
        }
        if (node.left) {
            stack.push([node.left, newPath])
        }
        if (node.right) {
            stack.push([node.right, newPath])
        }
    }
    
    for (let p of paths) {
        if (p.indexOf(target) > -1) {
            return true
        }
    }
    return false
};
*/
var isSubPath = function(head, root) {
    const path = []
    let cur = head
    while (cur != null) {
        path.push(cur.val)
        cur = cur.next
    }
    const target = path.join(',')
    
    const paths = []
    const stack = [[root, '']]
    while (stack.length > 0) {
        const [node, path] = stack.pop()
        const newPath = `${path},${node.val}`
        if (node.left == null && node.right == null) {
            paths.push(newPath)
        }
        if (node.left) {
            stack.push([node.left, newPath])
        }
        if (node.right) {
            stack.push([node.right, newPath])
        }
    }
    
    for (let p of paths) {
        if (p.indexOf(target) > -1) {
            return true
        }
    }
    return false
};