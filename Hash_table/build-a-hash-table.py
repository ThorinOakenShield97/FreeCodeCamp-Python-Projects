** start of main.py **

class HashTable:
    def __init__(self):
        self.collection = {}
        
    def hash(self,key):
        total = 0
        for char in key:
            total += ord(char)
        return total

    def add(self,key,value):
        h_key = self.hash(key)
        if h_key not in self.collection:
            self.collection[h_key] = {}
        self.collection[h_key][key] = value
        
    def remove(self,key):
        h_key = self.hash(key)
        if h_key in self.collection and key in self.collection[h_key]:
            self.collection[h_key].pop(key)
    
    def lookup(self,key):
        h_key = self.hash(key)
        if h_key in self.collection and key in self.collection[h_key]:
            return self.collection[h_key][key]
        return None

** end of main.py **

