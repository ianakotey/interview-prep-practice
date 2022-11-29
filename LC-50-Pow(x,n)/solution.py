class Solution:
    def myPow(self, x: float, n: int) -> float:
        match n:
            case y if y < 0:
                return 1/self.myPow(x, -y)
            case 0:
                return 1
            case 1:
                return x
            case 2:
                return x * x
            case _:
                res = self.myPow(x, n//2)
                return res * res if n % 2 == 0 else res * res * x

        raise RuntimeError("Unreachable!")


def test():

    test_runner = Solution()

    for i in range(-5, 5):
        print(test_runner.myPow(2, i))


test()
