import unittest
import main

Solution = main.Solution


class TestMain(unittest.TestCase):
    def test1(self):
        arr = [-1, 0, 1, 2, -1, -4]
        res = Solution().threeSum(arr)
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertListEqual(res, expected)

    def test2(self):
        arr = [-2, 0, 1, 1, 2]
        res = Solution().threeSum(arr)
        expected = [[-2, 0, 2], [-2, 1, 1]]
        self.assertListEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
