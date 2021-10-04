def findNumberDisappeared(nums:int) -> list(int):
    hmap={i:i for i in nums}

    return [i for i in range(1,len(nums)+1) if i not in hmap.keys()]

def findNumberDisappearedCostantSpace(nums:int) -> list(int):
    for i in nums:
            if(nums[abs(i)-1] > 0):
                nums[abs(i)-1] *= -1
    
    return [i+1 for i,n in enumerate(nums) if(n > 0)]


def main():
    pass

if __name__ == '__main__':
    main()
