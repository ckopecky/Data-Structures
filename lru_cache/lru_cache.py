from doubly_linked_list import DoublyLinkedList

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit #if limited is not passed, then the default is 10
    self.size = 0 #current size
    self.list = DoublyLinkedList() #instantiate DLL
    self.storage = {} #instantiate dict

  def __repr__(self):
    return f"{self.list}"
  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key not in self.storage:  #if the key doesn't exist in self.storage return None
      return None    
    else:
      value = self.storage[key] #value is set to the key of dict
      self.list.move_to_end(value) #move the value to the end of the DLL
      return value.value[1]


  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):

    if key in self.storage: #if the key exists in the dict
      node = self.storage[key] #node references key
      node.value = (key, value) #tuple with key and value in it
      # mark as most recently used. Put it at head of DLL
      self.list.move_to_front(node)
      return

      
    if self.size == self.limit:
      print(self.storage, "1")
      print(self.list)
      del self.storage[self.list.tail.value[0]] #removes it from dict
      self.list.remove_from_tail() #removes it from linked list
      print(self.storage, "2")
      self.size -= 1
    
    self.list.add_to_head((key, value))
    self.storage[key] = self.list.head
    self.size += 1

