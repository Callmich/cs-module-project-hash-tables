class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.elements = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.elements / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNVPrime = 1099511628211
        offsetBasis = 14695981039346656037

        hashedKey = offsetBasis

        byteString = key.encode()
        for b in byteString:
            hashedKey *= FNVPrime
            hashedKey ^= b

        return hashedKey


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # indexNumber = self.hash_index(key)
        # self.storage[indexNumber] = value

        indexNumber = self.hash_index(key)
        alreadyExists = self.storage[indexNumber]
        newNode = HashTableEntry(key, value)

        # First check if entry is in Table
        if alreadyExists:
            lastNode = None
            while alreadyExists:
                if alreadyExists.key == key:
                    alreadyExists.value = value
                    return alreadyExists.value
                lastNode = alreadyExists
                alreadyExists = alreadyExists.next
            lastNode.next = newNode
            self.elements += 1
            if self.get_load_factor() > 0.7:
                self.resize(len(self.storage) * 2)
        else:
            self.storage[indexNumber] = newNode
            self.elements += 1
            if self.get_load_factor() > 0.7:
                self.resize(len(self.storage) * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        # indexNumber = self.hash_index(key)
        # self.storage[indexNumber] = None

        indexNumber = self.hash_index(key)
        alreadyExists = self.storage[indexNumber]

        if alreadyExists:
            lastNode = None
            nextNode = alreadyExists.next
            while alreadyExists:
                if alreadyExists.key == key and lastNode is None:
                    self.storage[indexNumber] = alreadyExists.next
                    alreadyExists.value = None
                    alreadyExists.next = None
                    self.elements -= 1
                    return None
                elif alreadyExists.key == key and lastNode is not None:
                    alreadyExists.value = None
                    lastNode.next = nextNode
                    alreadyExists.next = None
                    self.elements -= 1
                    return None
                else:
                    nextNode = alreadyExists.next.next
                    lastNode = alreadyExists
                    alreadyExists = alreadyExists.next
        else:
            return None
                




    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        # indexNumber = self.hash_index(key)
        # return self.storage[indexNumber]

        indexNumber = self.hash_index(key)
        alreadyExists = self.storage[indexNumber]

        if alreadyExists:
            lastNode = None
            while alreadyExists:
                if alreadyExists.key == key:
                    return alreadyExists.value
                lastNode = alreadyExists
                alreadyExists = alreadyExists.next
            return None
        else:
            return None
           


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        oldHash = self.storage
        self.capacity = new_capacity

        self.storage = [None] * new_capacity

        for x in range(len(oldHash)):
            oldEntry = oldHash[x]

            while oldEntry:
                if oldEntry.key:
                    self.put(oldEntry.key, oldEntry.value)
                    oldEntry = oldEntry.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
