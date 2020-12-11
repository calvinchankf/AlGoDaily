/*
    1st approach: recursion

	Time	O(N)
	Space	O(H)
	68 ms, faster than 63.22%
*/
var isSameTree = function (p, q) {
	if (p == null && q == null) {
		return true;
	} else if (p == null || q == null) {
		return false;
	}
	return (
		p.val == q.val &&
		isSameTree(p.left, q.left) &&
		isSameTree(p.right, q.right)
	);
};

/*
    2nd approach: dfs using a stack

	Time	O(N)
	Space	O(H)
	116 ms, faster than 5.51%
*/
var isSameTree = function (p, q) {
	const stack = [[p, q]];
	while (stack.length > 0) {
		const [a, b] = stack.pop();

		if (a == null && b == null) {
			continue;
		} else if (a == null || b == null || a.val !== b.val) {
			return false;
		}
		stack.push([a.left, b.left]);
		stack.push([a.right, b.right]);
	}
	return true;
};

/*
    3rd: BFS

    Time	O(N)
	Space	O(H)
	80 ms, faster than 54.71%
*/
var isSameTree = function(p, q) {
    if (p == null && q == null) {
        return true
    } else if (p == null || q == null) {
        return false
    }
    const queue = [[p, q]]
    while (queue.length > 0) {
        const [a, b] = queue.shift()
        if (a.val !== b.val) {
            return false
        }
        if (a.left && b.left) {
            queue.push([a.left, b.left])
        } else if (a.left || b.left) {
            return false
        }
        
        if (a.right && b.right) {
            queue.push([a.right, b.right])
        } else if (a.right || b.right) {
            return false
        }
    }
    return true
};