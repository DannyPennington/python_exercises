def median(num):
    nums = sorted(num)
    total = 0
    if len(nums) % 2 == 0:
        f_index = nums[len(nums) // 2]
        s_index = nums[(len(nums) // 2) - 1]
        avg = (f_index + s_index) / 2.0
        total += avg

    else:
        med = nums[(len(nums) - 1) // 2]
        total += med

    return total


