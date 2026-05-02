class LinkedList:
    
    def __init__(self):
        self.data = []
    
    def get(self, index: int) -> int:
        try:
            return self.data[index]
        except:
            return -1

    def insertHead(self, val: int) -> None:
        self.data.insert(0,val)

    def insertTail(self, val: int) -> None:
        self.data.append(val)

    def remove(self, index: int) -> bool:
        try:
            self.data.pop(index)
            return True
        except:
            return False
        
    def getValues(self) -> List[int]:
        return self.data
