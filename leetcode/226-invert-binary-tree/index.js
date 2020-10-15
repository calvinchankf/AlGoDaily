/*
    1st: recusive dfs

    Time    O(N)
    Space   O(h)
    68 ms, faster than 54.89%
*/
var invertTree = function (root) {
	if (root == null) {
		return null;
	}
	const temp = root.left;
	root.left = invertTree(root.right);
	root.right = invertTree(temp);
	return root;
};

var invertTree = function (root) {
	if (root == null) {
		return null;
	}
	[root.left, root.right] = [invertTree(root.right), invertTree(root.left)];
	return root;
};

/*
    2nd: BFS

    Time    O(N)
    Space   O(h)
    68 ms, faster than 54.89%
*/
var invertTree = function (root) {
	if (!root) {
        return root
    }
    const q = [root]
    while (q.length > 0) {
        const node = q.shift() // pop(): stack based DFS also works
        
        const temp = node.left
        node.left = node.right
        node.right = temp
        
        if (node.left) {
            q.push(node.left)
        }
        if (node.right) {
            q.push(node.right)
        }
    }
    return root
};

/*
    followup: invert N-ary tree
*/
function Node(val, children) {
    this.val = val === undefined ? 0 : val;
    this.children = children === undefined ? [] : children;
}
const mirrorNaryTree = (root) => {
    if (!root) {
        return null
    }
    const newChildren = []
    for (let i = root.children.length-1; i >= 0; i--) {
        const child = root.children[i]
        const newChild = mirrorNaryTree(child)
        newChildren.push(newChild)
    }
    root.children = newChildren
    return root
}

const _printNaryTree = (node, hivens = '') => {
    if (node == null) {
        return
    }
    console.log(`${hivens}${node.val}`)
    for (let child of node.children) {
        _printNaryTree(child, hivens + '-')
    }
}

/*
            0
        1   2   3
    4 5 6   7
*/
const a = new Node(0)
const b = new Node(1)
const c = new Node(2)
const d = new Node(3)
const e = new Node(4)
const f = new Node(5)
const g = new Node(6)
const h = new Node(7)
a.children = [b, c, d]
b.children = [e, f, g]
c.children = [h]

const result = mirrorNaryTree(a)
_printNaryTree(result)