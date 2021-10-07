def maxArea(height: list[int]) -> int:
    l=0
    r=len(height)-1
    _max = 0

    while(l<r):
        _max = max(_max, (r-l)*min(height[l], height[r]))
        if(height[l]<height[r]): l+=1
        else: r-=1
    return(_max)


def main():
    print(maxArea(height = [1,8,6,2,5,4,8,3,7]))

if __name__ == '__main__':
    main()