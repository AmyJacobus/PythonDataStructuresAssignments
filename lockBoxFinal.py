

def generate_hash_code():
    pass
    # Our lock box will use scrolling integers not letters.

def lock_box_simulation():
    pass
    # The lock box (simulated) must be created using stack rules implemented with a Doubly Linked List in Python.

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
    #print(positive_hasho) #The hash of the quote
    print("_____________________________________________________________________________")

    print("Starting cracking processs.................")


if __name__ == '__main__':
    main()
