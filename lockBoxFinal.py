import itertools
from time import perf_counter_ns

quote = "The Davinci code we are using: Simplicity is the ultimate sophistication"
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


lock_passcode = positive_hasho

# create list out of the lock passcode
key_list = [int(x)for x in str(lock_passcode)]
print(f"Secret passcode is: {key_list}")


# Add that lock code key to a double link list using the linked list
# Add that lock code key to a double link list
# compare linked linked list to each other and let the user know when it has been cracked
# Display the time



# Cracks the code with the number of digits based on how many digits there are in th key
lock_passcode_len = str(lock_passcode)
lock_passcode_lenz = len(lock_passcode_len)
digits = list(range(0, 10))
print(f"We are attempting to crack a code that has {lock_passcode_lenz} digits")
print()

# track time
start_ss = perf_counter_ns()
for permutation in itertools.product(digits, repeat=len(lock_passcode_len)):
    permutation_list = [str(digit) for digit in permutation]
    permutation = "".join(permutation_list)
    permutation = int(permutation)
    if start_ss > 10000:
        print("LOADING...")
        print("██████████████]99% ")
        print("Oops...the cracking process is taking longer than usual..")
        print("System crashed, unable to crack code at this time....CPU at 99%!")
        print("The last attempt was: ", permutation)
        break
    elif permutation == lock_passcode:
        print(f"Code unlocked: {permutation}")
        break
stop_ss = perf_counter_ns()
total_time_ss = stop_ss - start_ss
print("This process took", total_time_ss, "seconds!")
print()
print("________________________________________________________________________________________")
print()

if lock_passcode_lenz > 4:
    print("You are dealing with a very large digit number, we can do 4 digits with your current hardware specs.")
    print("We can provide you with a simulation of a smaller digit code being cracked.")

    key_code = 1542
    print("Code sample: ", key_code)
    attempts = 1
    for permutation in itertools.product(digits, repeat=4):
        permutation_list = [str(digit) for digit in permutation]
        permutation = "".join(permutation_list)
        permutation = int(permutation)
        attempts += 1
        if attempts == 50:
            print("Starting..")
            print("█▒▒▒▒▒▒▒▒▒")
        elif attempts == 100:
            print("███▒▒▒▒▒▒▒")
        elif attempts == 500:
            print("█████▒▒▒▒▒")
        elif attempts == 1000:
            print("███████▒▒▒")
        if permutation == key_code:
            print(f"‎███████████████████ 100% Code cracked successfully: {permutation}")
            break






