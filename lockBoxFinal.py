
def main():

    quote = "The Davinci code we are using: Simplicity is the ultimate sophistication."
    print("****************************************************************************")
    print("                  Welcome to the cryptex lock box!                           ")
    print()
    print("****************************************************************************")
    print()
    print(quote)

    #------------hashing code---------------------
    hasho = hash(quote)
    positive_hasho = abs(hasho)
    #print(quote)
    print(positive_hasho) #The hash of the quote
    print("_____________________________________________________________________________")

    print("Starting cracking processs.................")

    import itertools

    lock_passcode = positive_hasho
    lock_passcode_len = str(lock_passcode)
    digits = list(range(0, 10))

    for permutation in itertools.product(digits, repeat=len(lock_passcode_len)):
        permutation_list = [str(digit) for digit in permutation]
        permutation = "".join(permutation_list)
        permutation = int(permutation)
        if permutation == lock_passcode:
            print(f"Code unlocked: {permutation}")
            break

    print("Code has been cracked!")
    print("The code was: ", permutation)


if __name__ == '__main__':
    main()
