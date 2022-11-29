class Node:
    def __init__(self, data):
        self.item = data # contains the data
        self.next = None # connects to the previous pointer
        self.prev = None # connects to the next pointer

# 0. Turn a code into a list
# 1. Turn the hash code into 4, 6, 10 lenght of code from
# 2. Turn the 4 code into the main digit to be cracked
# 3. Store those code in the stack
# 4. Print the stack and check againts the code
# - check the code against in for loop, each permutation code against the ones in the double linked list
# 5. Track the time for each, until completed
# ---
#6. Repeat again for the 6 digit
#7. Repeat again for the 10 digits

#8 Generate report