# A cryptex lock box is a vessel with numerous scrolling letter rings.
# Only the correct sequence of letters will open the box.
# Develop a program that uses a hash of any Leonardo DaVinci quote as the key to enter the box.
# Our lock box will use scrolling integers not letters.
# The lock box (simulated) must be created using stack rules implemented with a Doubly Linked List in Python.
# First - generate the hashed value of your quote - use absolute value for only positive numbers.
# Then simulate an attempt at opening the box, attempting to crack as many integers as you can (as the permutations increase time increases exponentially **) of our hash - comparing to our simulated Stack / DDL lock box.
# Start with 4 digits, then 6 then .... 19?  It will take hours or even days for 19.  I got up to 10 (see my output below for time outputs)
# The individual hash values will open the lockbox but only if they are in the correct hashed sequence - thus the stack.
# The stack will contain the correct sequence.
# Create printed outputs explaining the process and finalize with the unlocked code and the time it took to crack.
#
# Submit  your .py files and a couple of screen shots of it working


class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class LinkedList:
   def __init__(self):
      self.headval = None
list1 = LinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

#Travers it:
def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

# To provide the ability to insert we would add:
def AtBegining(self,newdata):
      NewNode = Node(newdata)

# Update the new nodes next val to existing node
   NewNode.nextval = self.headval
   self.headval = NewNode

#Then add to main:

def main():
    list1.listprint()

#Then add to main:
list.AtBegining("Sun")
list.listprint()