class DLLNode:
    def __init__(self, key: int, value: int):
        self.prev = None
        self.next = None
        self.key = key
        self.val = value

class LRUCache:

    def __init__(self, capacity: int):
        # creates a DLL with the Left & right ends
        self.cap = capacity
        # creating a dictionary to map key to node in the DLL
        self.map = defaultdict(DLLNode)
        # create a the left/head node
        self.Left = DLLNode(0,0)
        # create the right/tail node    
        self.Right = DLLNode(0,0)
        # init the linkages
        self.Left.next  = self.Right
        self.Right.prev = self.Left

    def remove(self, node: DLLNode):
        # removes provided node from LL
        # Usage: to remove from DLL when
            # cache overflow
            # key outdated
        node.prev.next = node.next
        node.next.prev = node.prev


    def insert(self, node:DLLNode):
        # insert node at the Left, blindly
        # Usage:
            # whenever a new key is encountered
            # whenever a key is hit (get() activated for the key)
        start = self.Left.next
        # node to left linkage
        self.Left.next = node
        node.prev = self.Left
        # node to pre-existent "start" linkage
        start.prev = node
        node.next = start
        

    def get(self, key: int) -> int:
        if key in self.map:
            # key exists, remove it
            self.remove( self.map[key] )
            # and insert it into the start/ Left
            self.insert( self.map[key] )

            return self.map[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # before putting we must check for capacity, and if node exists already or not
        if key in self.map:
            # if exists, overwrite
            self.remove( self.map[key] )
        # update val: the map contains a Node, not int
        self.map[key] = DLLNode(key, value)
            # this means updating LRU as well
        self.insert( self.map[key] ) 
        
        # after inserting, check for overflow
        if len(self.map) > self.cap:
            # remove(Right.prev, the LRU element)
            popped = self.Right.prev
            self.Right.prev = popped.prev
            popped.prev.next = self.Right
            del self.map[popped.key]
        


            # insert at left.next and update the rest
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)