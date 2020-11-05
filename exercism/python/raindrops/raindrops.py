def convert(number):
    msg = ""
    msg_factors = {
        3: 'Pling',
        5: 'Plang',
        7 : 'Plong'
    }
    for i in range(1,number+1):
        if number % i == 0:
            if msg_factors.get(i):
                msg += msg_factors.get(i)
    return msg if msg else str(number) 
    
    

if __name__ == "__main__":

    print(convert(9))