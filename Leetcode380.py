import random
class RandomizedSet:

    def __init__(self):
        self.num_list :List[int] = []
        self.val_to_idx :Dict[int, int] = {}
        

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
            
        self.num_list.append(val)
        self.val_to_idx[val] = len(self.num_list) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False

        idx = self.val_to_idx[val] 
        last_val = self.num_list[-1]
        self.num_list[idx] = last_val
        self.num_list.pop()
        self.val_to_idx[last_val] = idx
        del self.val_to_idx[val]
        return True
        

    def getRandom(self) -> int:
        idx = random.randint(0,len(self.num_list)-1)
        
        return self.num_list[idx]

"""
[1,2,3,4,5,6] remove 2
[1,6,3,4,5,6] pop 6 (last_val)
[1,3]
"""
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()