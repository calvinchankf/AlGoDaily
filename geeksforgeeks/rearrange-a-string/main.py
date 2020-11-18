def f(s):
    num = 0
    chars = 26 * [0]
    for c in s:
        if c.isdigit():
            num += int(c)
        else:
            key = ord(c) - ord('A')
            chars[key] += 1
    res = ''
    for i in range(26):
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count = chars[i]
        if count > 0:
            res += count * alphabets[i]
    res += str(num)
    return res

a = 'AC2BEW3'
print(f(a)) # ABCEW5

a = 'ACCBA10D2EW30'
print(f(a)) # AABCCDEW6

a = 'DORWBL4A16H1'
print(f(a)) # ABDHLORW12

a = 'MJEEAKCOUQWXWSJXBWAGMSDNFQ18W4P1'
print(f(a)) # AABCDEEFGJJKMMNOPQQSSUWWWWXX14