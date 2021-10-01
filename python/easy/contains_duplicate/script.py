def containsDuplicateWithHash(nums):
    hmap = {}
    for i in nums:
        if(i in hmap.keys()): return True
        hmap[i]=i

    return False

def containsDuplicateWithSet(nums):
    snum = set(nums)
    return len(set(snum)) != len(nums)

def main():
    print("Output: {}".format(containsDuplicateWithHash([1,2,3,1])))
    print("Output: {}".format(containsDuplicateWithHash([1,2,3,4])))
    print("Output: {}".format(containsDuplicateWithHash([1,1,1,3,3,4,3,2,4,2])))
    print("\n")
    print("Output: {}".format(containsDuplicateWithSet([1,2,3,1])))
    print("Output: {}".format(containsDuplicateWithSet([1,2,3,4])))
    print("Output: {}".format(containsDuplicateWithSet([1,1,1,3,3,4,3,2,4,2])))

if __name__ == "__main__":
    main()
