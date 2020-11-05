Alphabates = "".join(list(map(chr, range(97, 123))))

def is_pangram(sentence):
    
    sorted_pangram = "".join(sorted(set(list(map(lambda  x : x.lower() if (not x.isspace() and x.isalpha()) else "", sentence)))))
    if sorted_pangram == Alphabates:
        return True
    return False

    

if __name__ == "__main__":

    p ='"Five quacking Zephyrs jolt my wax bed."'
    print(is_pangram(p))
