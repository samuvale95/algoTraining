def twoSum(nums, target):
    hmap = {}

    for i in range(0, len(nums)):
        partial = target - nums[i]

        if(partial in hmap.keys()):
            return [hmap[partial], i]

        hmap[nums[i]] = i

def main():
    print(twoSum([2,7,11,15], 9))
    print(twoSum([3,2,4], 6))
    print(twoSum([3,3], 6))

if __name__ == "__main__":
    main()