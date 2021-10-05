def findAllNumbersDisappeared(nums):
    for i in nums:
        if(nums[abs(i)-1] > 0):
            nums[abs(i)-1] *= -1

    return [i+1 for i,n in enumerate(nums) if(n > 0)]

def main():
    print("Output: {}".format(findAllNumbersDisappeared([4,3,2,7,8,2,3,1])))
    print("Output: {}".format(findAllNumbersDisappeared([1,1])))

if __name__ == "__main__":
    main()