def reverse1(x:int) -> int:
        is_neg = x < 0

    rev_x = int(''.join(reversed(str(abs(x)))))

    if(is_neg):
        rev_x=rev_x*-1

    return  rev_x if rev_x > -2**31 and rev_x < (2**31)-1 else 0

def reverse2(x:int)-> int:
        op=''
        sx = str(x)

        if(sx[0] == '-'):
            op = sx[0]
            sx=sx[1:]

        res=''
        for i in range(len(sx)-1, -1, -1): res+=sx[i]

        reverse_int = int(op+res)
        return  reverse_int if reverse_int > -2**31 and reverse_int < (2**31)-1 else 0

def main():
    print(reverse1(123))
    print(reverse1(-123))
    print(reverse1(120))
    print(reverse1(0))

if __name__ == "__main__":
    main()