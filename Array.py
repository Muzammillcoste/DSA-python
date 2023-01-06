import ctypes
import timeit

class Array:
    def __init__(self,n):
        assert n>0,'size of array should be greater than 0'
        self.element=(ctypes.py_object*n)()
        self.size=n
        self.clear(None)
     
    def clear(self,value):
        for i in range(self.size):
               self.element[i]=value
        
    def __len__(self):
        return self.size
    
    def __getitem__(self,index):
        assert self.size>index>=0,'index out of bound'
        return self.element[index]
    
    def __setitem__(self,index,value):
        assert self.size>index>=0,'index out of bound'
        self.element[index]=value
        
    def insert(self,index:int,value) -> None:
        assert self.size>index>=0,'index out of bound'
        for i in range(self.size-1,index,-1):
            self.element[i]=self.element[i-1]
        self.element[index]=value
        
    def delete(self,index:int) -> None:
        assert self.size>index>=0,'index out of bound'
        for i in range(index,self.size-1):
            self.element[i]=self.element[i+1]
        self.element[self.size-1]=None
        
    def transver(self):
        for i in range(self.size):
            print(self.element[i],end=',')
        print()
        
    def search(self,value):
        lo=0
        hi=self.size-1
        while lo<=hi:
            mid=(lo+hi)//2
            if self.element[mid]==value:
                return mid
            elif self.element[mid]>value:
                hi=mid-1
            else:
                lo=mid+1
        return None
    
    def sort(self:object) -> object:
        for i in range(self.size-1,0,-1):
            for j in range(i):
                if self.element[j]>self.element[j+1]:
                    temp=self.element[j]
                    self.element[j]=self.element[j+1]
                    self.element[j+1]=temp
        return self
                
        
if __name__ =='__main__':
    
    starttime=timeit.default_timer()         
    a1=Array(3)
    len(a1)
    a1[0]=101
    a1[1]=2
    a1[2]=-9
    a1.insert(1,37)
    a1.transver()
    a1.sort()
    a1.transver()
    print(a1.search(101))
    endtime=timeit.default_timer()
    print('Execution time is',"{:e}".format(endtime-starttime))
        
        
            
    
    