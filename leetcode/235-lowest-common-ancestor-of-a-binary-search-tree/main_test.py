import unittest
import main

TreeNode = main.TreeNode
Solution = main.Solution


class TestMain(unittest.TestCase):

    def test1(self):
        #     5
        #   3   6
        # 2  4
        # 1
        a = TreeNode(5)
        b = TreeNode(3)
        c = TreeNode(6)
        d = TreeNode(2)
        e = TreeNode(4)
        f = TreeNode(1)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        d.left = f
        ans = Solution().lowestCommonAncestor(a, TreeNode(1), TreeNode(6))
        self.assertEqual(ans.val, 5)

    def test2(self):
        #     5
        #   3   6
        # 2  4
        # 1
        a = TreeNode(5)
        b = TreeNode(3)
        c = TreeNode(6)
        d = TreeNode(2)
        e = TreeNode(4)
        f = TreeNode(1)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        d.left = f
        ans = Solution().lowestCommonAncestor(a, TreeNode(1), TreeNode(5))
        self.assertEqual(ans.val, 5)

    def test3(self):
        #     5
        #   3   6
        # 2  4
        # 1
        a = TreeNode(5)
        b = TreeNode(3)
        c = TreeNode(6)
        d = TreeNode(2)
        e = TreeNode(4)
        f = TreeNode(1)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        d.left = f
        ans = Solution().lowestCommonAncestor(a, TreeNode(1), TreeNode(3))
        self.assertEqual(ans.val, 3)

    def test4(self):
        #     5
        #   3   6
        # 2  4
        # 1
        a = TreeNode(5)
        b = TreeNode(3)
        c = TreeNode(6)
        d = TreeNode(2)
        e = TreeNode(4)
        f = TreeNode(1)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        d.left = f
        ans = Solution().lowestCommonAncestor(a, TreeNode(1), TreeNode(4))
        self.assertEqual(ans.val, 3)

    def test5(self):
        #     5
        #   3   6
        # 2  4
        # 1
        a = TreeNode(5)
        b = TreeNode(3)
        c = TreeNode(6)
        d = TreeNode(2)
        e = TreeNode(4)
        f = TreeNode(1)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        d.left = f
        ans = Solution().lowestCommonAncestor(a, TreeNode(3), TreeNode(5))
        self.assertEqual(ans.val, 5)

    def test6(self):
        #     5
        #   3   6
        # 2  4
        # 1
        a = TreeNode(5)
        b = TreeNode(3)
        c = TreeNode(6)
        d = TreeNode(2)
        e = TreeNode(4)
        f = TreeNode(1)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        d.left = f
        ans = Solution().lowestCommonAncestor(a, TreeNode(3), TreeNode(4))
        self.assertEqual(ans.val, 3)


print('name', __name__)
if __name__ == '__main__':
    unittest.main()
