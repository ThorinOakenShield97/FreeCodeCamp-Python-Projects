** start of main.py **

from typing import Any, Optional

class HashTable:
    """
    A custom Hash Table implementation that uses a nested dictionary structure
    to handle hash collisions efficiently (Separate Chaining).
    """
    def __init__(self) -> None:
        self.collection: dict = {}
        
    def hash(self, key: str) -> int:
        """
        Generates a hash value for a given string key by summing the ASCII 
        values of its characters.
        """
        # sum() with a generator expression
        return sum(ord(char) for char in key)

    def add(self, key: str, value: Any) -> None:
        """
        Adds a key-value pair to the hash table. 
        Handles collisions by storing multiple pairs under the same hash 
        using a nested dictionary.
        """
        h_key = self.hash(key)
        
        # If the hash doesn't exist yet, create a new dictionary (bucket) for it
        if h_key not in self.collection:
            self.collection[h_key] = {}
            
        # Store or update the value at the specific key within the bucket
        self.collection[h_key][key] = value
        
    def remove(self, key: str) -> None:
        """
        Removes a key-value pair from the hash table based on the key.
        Also cleans up empty hash buckets to manage memory efficiently.
        """
        h_key = self.hash(key)
        
        # Check if the hash exists and the exact key is within that bucket
        if h_key in self.collection and key in self.collection[h_key]:
            self.collection[h_key].pop(key)
            
            # Memory management: remove the bucket entirely if it's now empty
            if not self.collection[h_key]:
                self.collection.pop(h_key)
    
    def lookup(self, key: str) -> Optional[Any]:
        """
        Retrieves the value associated with a given key. 
        Returns None if the key is not found in the hash table.
        """
        h_key = self.hash(key)
        
        if h_key in self.collection and key in self.collection[h_key]:
            return self.collection[h_key][key]
            
        return None


# --- Testing block ---
if __name__ == "__main__":
    ht = HashTable()
    
    print("--- Adding Items ---")
    ht.add("Thorin", "King Under the Mountain")
    ht.add("Gandalf", "Wizard")
    # 'Gimli' and 'Migil' would technically have the same hash (same letters), 
    # testing collision handling:
    ht.add("Gimli", "Dwarf Warrior") 
    ht.add("Migil", "Made-up character to force collision")
    
    print("Collection state:", ht.collection)
    
    print("\n--- Looking up Items ---")
    print("Thorin's title:", ht.lookup("Thorin"))
    print("Unknown character:", ht.lookup("Sauron"))
    
    print("\n--- Removing Items ---")
    ht.remove("Migil")
    print("Collection after removing 'Migil':", ht.collection)

** end of main.py **

