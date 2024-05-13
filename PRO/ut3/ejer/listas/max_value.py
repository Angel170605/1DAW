def run(values: list) -> int:
    nums = []
    for value in values:
        nums.append(value)
        if value > nums[0]:
            nums[0] = value
            max_value = nums.pop(-1)

    return max_value


if __name__ == '__main__':
    run([-11, 10, -6, 15, -1])
