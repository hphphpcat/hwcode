from random import choice

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.d = {}  # Key to value mapping
        self.indices = {}  # Value to index mapping

    def get(self, key):
        if key in self.d:
            return self.d[key]
        return -1  # Key does not exist

    def delete(self, key):
        if key not in self.d:
            return False  # Deletion unsuccessful

        value = self.d[key]
        position = list(self.indices[value])[0]
        if value == self.values[-1]:
            self.indices[value].remove(position)
            del self.d[key]
            return True
        # Update indices for the last value
        self.indices[self.values[-1]].remove(len(self.values) - 1)
        self.indices[self.values[-1]].add(position)
        self.indices[value].remove(position)

        self.values[position], self.values[-1] = self.values[-1], self.values[position]
        self.values.pop()

        del self.d[key]  # Remove key from dictionary
        return True  # Deletion successful

    def put(self, key, value):
        if key in self.d:
            self.delete(key)
        self.d[key] = value
        self.values.append(value)  # Update values array
        if value not in self.indices:
            self.indices[value] = set()
        self.indices[value].add(len(self.values) - 1)  # Record position

    def get_random_val(self):
        return choice(self.values)  # Return any random value from the values array
s =  RandomizedSet()
s.put("a",1)
s.put("b",1)
print(s.delete("a"))
print(s.delete("b"))


def getMin(n,debts):
    d=[0 for i in range(n)]
    for x,y,w in debts:
        d[x]-=w
        d[y]+=w
    d.sort()
    l = 0
    r = len(d) - 1
    res = 0
    while l<r:
        if d[r] == 0:
            r-=1
        elif d[l] == 0:
            l+=1
        else:
            res+=1
            if d[l] == -d[r]:
                d[l] = d[r] = 0
                l+=1
                r-=1
            elif d[r] + d[l] < 0 :
                d[l] += d[r]
                r -= 1
            else:
                d[r] += d[l]
                l += 1
    return res
print(getMin(3,[[0,1,10],[1,2,4],[2,0,8],[1,0,2]]))
print(getMin(3,[[0,1,10],[2,0,5]]))
print(getMin(4,[[1,2,15],[3,2,14],[0,3,10],[3,1,20]]))
