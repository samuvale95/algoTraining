def isPalindrome(x: int) -> bool:
    if(x < 0): return False

    return str(x) == ''.join(reversed(str(x)))

def main():
    print(isPalindrome(11))

if __name__ == "__main__":
    main()