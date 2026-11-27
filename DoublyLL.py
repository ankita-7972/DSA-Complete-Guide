class NOde:
    def __init__(self, value=None):
        self.info = value 
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = NOde(value)
        if(self.head == None):
            self.head = temp
            return

        t = self.head
        while(t.next != None):
            t = t.next

        t.next = temp
        temp.prev = t

    def insertAtBeg(self , value):
        temp = NOde(value)
        if(self.head == None):
            self.head = temp
            return

        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMid(self,value,x):
        t = self.head
        while(t.next !=None):
            if(t.info == x):
                break
            else:
                t = t.next

        temp = NOde(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def deletionDLL(self,value):
        if(self.head == None):
            print("Linked List is empty")
            return

        t = self.head
        if(t.info == value):
            self.head = t.next
            self.head.prev = None
            return
        while(t.next != None):
            if(t.info == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:

                t= t.next
            if(t.info == value):
                t.prev.next = None

    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.info, end= " <--> ")
            t = t.next
        print(t.info)

obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(5)
obj.insertAtMid(15,10)
obj.deletionDLL(5)
obj.deletionDLL(20)
obj.deletionDLL(40)
obj.printDLL()





      