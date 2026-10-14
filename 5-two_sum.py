def returnTwoSum(nums: list, target: int) -> list:
    seen = {}

    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
    return []

seen = {0:2}
seen[2] = 0
print(seen)