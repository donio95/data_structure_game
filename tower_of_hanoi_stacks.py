class Node:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next_node=next_node

    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self,new_value):
        self.next_node=new_value

class Stack:
  def __init__(self, name):
    self.size = 0
    self.top_item = None
    self.limit = 1000
    self.name = name
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
    else:
      print("No more room!")

  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("This stack is totally empty.")

  def peek(self):
    if self.size > 0:
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
  def get_size(self):
    return self.size
  
  def get_name(self):
    return self.name
  
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))

print("\nLet's play Towers of Hanoi!!")

stacks=[]
left_stack=Stack("Left")
middle_stack=Stack("Middle")
right_stack=Stack("Right")

stacks+=[left_stack,middle_stack,right_stack]



num_disks=int(input('\nHow many disks do you want to play with?\n'))
while num_disks<3:
  print("Enter a number greater than or equal to 3\n")
  num_disks=int(input('\nHow many disks do you want to play with?\n'))
  
for disk in range(num_disks,0,-1):
  left_stack.push(disk)
    
num_optimal_moves=pow(2,num_disks-1)
print("The optimal num of moves is {}".format(num_optimal_moves))

def get_input():
  
  choices = [i.get_name()[0] for i in stacks]
  
  
  while True :                          #put my choices in a list, by letter
    for i in range(len(stacks)):  
      name=stacks[i].get_name()
      letter=choices[i]
      print ("Enter {} for {}".format(letter,name))
      
    user_input = input("")
    
    if user_input in choices:
      return stacks[choices.index(user_input)]                   # return the Stack he chose, 
    else:
      print("input does not fit")
      
    
#The game:

num_user_moves=0

while right_stack.get_size() < num_disks:
  print("\n\n\n...current Stacks...")
  
  for i in stacks:
    i.print_items()
  
  while True:
    print("\nWhich stack do you want to move from?\n")
    
    
    while True:                #check not moving from empty stack, 
      from_stack=get_input()
      
      if not from_stack.is_empty():
        break    
      else:   
        print("\n\nThe stack you moving from is empty\n")
        
    print("\nWhich stack do you want to move to?\n")
    
    to_stack=get_input()
    
    
    
    if to_stack.is_empty() or from_stack.peek()<to_stack.peek():
      disc = from_stack.pop()
      to_stack.push(disc)
      num_user_moves+=1
      break 
      
    else:                  #when he didn't stand in condition of the game:
            
      print("\n\nThe move is not legal, you trying to put big disk on small one")
      for i in stacks:
        i.print_items() # print the stacks
print("\n\nYou completed the game in {0} moves,\n and the optimal number of moves is {1}".format(num_user_moves,num_optimal_moves))
  
  



