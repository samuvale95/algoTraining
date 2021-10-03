def romanToInt(s:str) -> int:
    romanMap = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
    }

    res=0
    for i in range(0, len(s)):
        if(i < len(s)-1 and romanMap[s[i]] < romanMap[s[i+1]]):
            res -= romanMap[s[i]]
        else:
            res += romanMap[s[i]]

    return res

def main():
    print(romanToInt("III"))
    print(romanToInt("IV"))
    print(romanToInt("IX"))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))

if __name__ == '__main__':
    main()