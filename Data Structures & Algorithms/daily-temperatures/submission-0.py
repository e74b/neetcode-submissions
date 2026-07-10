class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # i give up
        stack = []
        indexStack = []
        result = [0 for _ in temperatures]

        for index, temp in enumerate(temperatures):
            while (len(stack) > 0) and (temp > stack[-1]):
                top = stack.pop()
                idx = indexStack.pop()

                result[idx] = index - idx
            stack.append(temp)
            indexStack.append(index)

        return result