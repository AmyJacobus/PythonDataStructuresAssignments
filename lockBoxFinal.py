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

#create empty link list
class Node:
    def __init__(self, next=None, prev=None, data=None):
        # reference to next node in DLL
        self.next = next
        # reference to previous node in DLL
        self.prev = prev
        self.data = data

class LinkedList:
    # Init a Linked List object
    def __init__(self):
        self.head = None

    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data=new_data)
        # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None
        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node
        # 5. move the head to point to the new node
        self.head = new_node

    def pop(self):
        original_head = self.head
        new_head = original_head.next
        self.head = new_head
        new_head.previous = None
#----------------------------------------


DoubleLinkList = LinkedList()  # create object

#Use the linkedlist - reverse push into
print("Double linked list code format: ", end="")
for index in range(len(key_list)):
    #print("Printing index", index, end=" -->" )
    DoubleLinkList.push(key_list[len(key_list) - (index + 1)])  # reverse inserting

    print(DoubleLinkList.head.data, end=" ")
    if index < len(key_list)-1:
        print(end=" --> ")

# Get the first 4 head

print()
print("Cracking 4 digits......")
digits = list(range(0,10))
length = 4

CodeToCrack = ""

for number in range(length):
    CodeToCrack += str(DoubleLinkList.head.data)
    DoubleLinkList.pop()

print()
print("Code to be cracked: ", CodeToCrack) #Test and shows us the empty string


start_ss = perf_counter_ns() # Tracks the time
for permutation in itertools.product(digits, repeat=len(CodeToCrack)):
    permutation_list = [str(digit) for digit in permutation]
    permutation = "".join(permutation_list)
    permutation = int(permutation)
    if permutation == int(CodeToCrack):
        print("██ 39%")
        print("███ 49 %")
        print("████ 76 %")
        print("█████ 89 %")
        print("██████ 100 %")
        print(f"Code unlocked: {permutation}")
        break
stop_ss = perf_counter_ns() #Stop tracking time when the permutation is process is done
total_time_ss = stop_ss - start_ss
print("This process took", (total_time_ss * 10**-9), "Seconds!")
print()
print("________________________________________________________________________________________")
print()

print()
print(".....")
print("Since that was a success...")
print("Attempting 6 digits....")

length = 6

CodeToCrack = ""

for number in range(length):
    CodeToCrack += str(DoubleLinkList.head.data)
    DoubleLinkList.pop()

print()
print("Code to be cracked: ", CodeToCrack)  #Test and shows us the empty string


start_ss = perf_counter_ns()  # Tracks the time
for permutation in itertools.product(digits, repeat=len(CodeToCrack)):
    permutation_list = [str(digit) for digit in permutation]
    permutation = "".join(permutation_list)
    permutation = int(permutation)
    if permutation == int(CodeToCrack):
        print("██ 39%")
        print("███ 49 %")
        print("████ 76 %")
        print("█████ 89 %")
        print("██████ 100 %")
        print(f"Code unlocked: {permutation}")
        break
stop_ss = perf_counter_ns() #Stop tracking time when the permutation is process is done
total_time_ss = stop_ss - start_ss
print("This process took", (total_time_ss * 10**-9), "Seconds!")
print()
print("________________________________________________________________________________________")
print()

print("Well...why not push 8......")
print("Lets see...")
print("Attempting.....8 digits...")
print()

length = 8

CodeToCrack = ""

for number in range(length):
    CodeToCrack += str(DoubleLinkList.head.data)
    DoubleLinkList.pop()

print()
print("Code to be cracked: ", CodeToCrack) #Test and shows us the empty string


start_ss = perf_counter_ns() # Tracks the time
for permutation in itertools.product(digits, repeat=len(CodeToCrack)):
    permutation_list = [str(digit) for digit in permutation]
    permutation = "".join(permutation_list)
    permutation = int(permutation)
    if permutation == int(CodeToCrack):
        print("██ 39%")
        print("███ 49 %")
        print("████ 76 %")
        print("█████ 89 %")
        print("██████ 100 %")
        print(f"Code unlocked: {permutation}")
        break
stop_ss = perf_counter_ns() #Stop tracking time when the permutation is process is done
total_time_ss = stop_ss - start_ss
print("This process took", (total_time_ss * 10**-9), "Seconds!")
print()
print("________________________________________________________________________________________")
print()