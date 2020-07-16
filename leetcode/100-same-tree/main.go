package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: recursion

	Time	O(n)
	Space	O(h)
	0 ms, faster than 100.00%
*/
func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	} else if p == nil || q == nil {
		return false
	} else if p.Val != q.Val {
		return false
	}
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

/*
	2nd approach: dfs using a stack

	Time	O(n)
	Space	O(h)
	0 ms, faster than 100.00%
*/
type StackItem struct {
	NodeA *TreeNode
	NodeB *TreeNode
}

func isSameTree1(p *TreeNode, q *TreeNode) bool {
	stack := []*StackItem{}
	stack = append(stack, &StackItem{p, q})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if pop.NodeA != nil && pop.NodeB != nil {
			if pop.NodeA.Val != pop.NodeB.Val {
				return false
			}
			stack = append(stack, &StackItem{pop.NodeA.Left, pop.NodeB.Left})
			stack = append(stack, &StackItem{pop.NodeA.Right, pop.NodeB.Right})
		} else if pop.NodeA == nil && pop.NodeB == nil {
			// return false
		} else {
			return false
		}
	}
	return true
}

func main() {

}
