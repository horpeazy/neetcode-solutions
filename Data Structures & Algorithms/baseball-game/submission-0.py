class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for operation in operations:
            if operation == "+":
                num = sum(arr[-2:])
                arr.append(num)
            elif operation == "D":
                num = 2 * arr[-1]
                arr.append(num)
            elif operation == "C":
                arr.pop()
            else:
                try:
                    num = int(operation)
                    arr.append(num)
                except ValueError:
                    print("Invalid operation")
                    return -1

        return sum(arr)
        