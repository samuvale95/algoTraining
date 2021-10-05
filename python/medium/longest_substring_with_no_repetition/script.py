def lengthOfLongestSubstring(s:str) -> int:
    hmap={}
    res,l=0,0

    for r in range(len(s)):
        if(s[r] in hmap):
            if(l>hmap[s[r]]):
                res=max(res,r-l+1)
            else:
                l=hmap[s[r]]+1
        else:
            res=max(res,r-l+1)
        hmap[s[r]]=r
    return res



def main():
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring(""))
    print(lengthOfLongestSubstring(" "))

if __name__ == '__main__':
    main()