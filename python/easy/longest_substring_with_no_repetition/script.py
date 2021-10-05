def lengthOfLongestSubstring(s:str) -> int:
    hmap={}
    partial=''
    res=''
    i=0

    while i < len(s):
        if(s[i] in hmap.keys()):
            if(len(partial)>len(res)):
                res=partial
            partial=''
            i=hmap[s[i]]+1
            hmap={}
        else:
            hmap[s[i]] = i
            partial+=s[i]
            i+=1
    if(len(partial)>len(res)):
        res=partial
    return len(res)

def main():
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring(""))
    print(lengthOfLongestSubstring(" "))

if __name__ == '__main__':
    main()