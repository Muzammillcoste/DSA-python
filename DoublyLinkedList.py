class Node:
    def __init__(self,prev=None,data=None,next=None) -> None:
        self.data=data
        self.next=next
        self.prev=prev

class Doublelinkedlist:
    def __init__(self) -> None:
        self.head=None

    def append(self,data):
        if self.head is None:
            new_node=Node(None,data,None)
            self.head=new_node
            return

        itr=self.head
        while itr.next:
            itr=itr.next
        new_node=Node(itr,data,None)
        itr.next=new_node

    def append_left(self,data):
       new_node=Node(None,data,self.head) 
       self.head.prev=new_node
       self.head=new_node

    def reverse(self):
            tmp = None
            cur = self.head
            while cur:
                tmp = cur.prev
                cur.prev = cur.next
                cur.next = tmp
                cur = cur.prev
            if tmp:
                self.head = tmp.prev

    def insert(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("invalid index")
        elif index==0:
            self.append_left(data)
            return
        cur=self.head
        count=0
        while cur:
            if  count==index-1:
                new_node=Node(cur,data,cur.next)
                nxt=cur.next      #next node
                cur.next=new_node
                nxt.prev=new_node
            cur=cur.next
            count+=1

    def delete(self,key):
        cur=self.head
        while cur:
            #delete first node
            if cur.data==key and self.head==cur:
                #when only one node
                if cur.next is None:
                    self.head=None
                    cur=None
                    return
                #when there are node 
                else:
                    nxt=cur.next
                    nxt.prev=None
                    cur.next=None
                    cur=None
                    self.head=nxt
                    return
            #when node is in the middle or at the end
            elif cur.data==key:
                #when node at between
                if cur.next:
                    pre=cur.prev # it is previous node of targeted node
                    nxt=cur.next # it is next node of targeted node
                    pre.next=nxt
                    nxt.prev=pre
                    cur.next=None
                    cur.prev=None
                    cur=None
                    return
                #when node at end 
                else:
                    pre=cur.prev # it is previous node of targeted node
                    pre.next=None
                    cur.prev=None
                    cur=None
                    return
            cur=cur.next


    def print(self):
        if self.head is None:
            print("your linked list is empty")
            return
        itr=self.head
        llitr=''
        while itr:
            llitr+=str(itr.data)+'-->'
            itr=itr.next
        print(llitr)
    
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

if __name__=="__main__":
    dll=Doublelinkedlist()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append_left(0)
    dll.append_left(-1)
    dll.append_left(-2)
    dll.print()
    