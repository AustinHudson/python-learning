class hashSet(object):
    def __init__(self, numBuckets): 
        '''
        numBuckets: int. The number of buckets this hash set will have. 
        Raises ValueError if this value is not an integer, or if it is not greater than zero.
    
        Sets up an empty hash set with numBuckets number of buckets.
        '''
        if type(numBuckets) != int or numBuckets <= 0:
            raise ValueError
        self.NUM_BUCKETS = numBuckets
        self.set = []
        for i in range(self.NUM_BUCKETS):
            self.set.append([])

    def hashValue(self, e):
        '''
        e: an integer

        returns: a hash value for e, which is simply e modulo the number of 
        buckets in this hash set. Raises ValueError if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError
        return e % self.NUM_BUCKETS

    def member(self, e):
        '''
        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
        '''
        if type(e) != int:
            raise ValueError
        return e in self.set[self.hashValue(e)]

    def insert(self, e):
        '''
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        ''' 
        if type(e) != int:
            raise ValueError
        self.set[self.hashValue(e)].append(e)

    def remove(self, e):
        '''
        e: is an integer 
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        ''' 
        if type(e) != int or not self.member(e): 
            raise ValueError
        find = self.set[self.hashValue(e)]
        del find[find.index(e)]
    
    def getNumBuckets(self):
        '''
        Returns number of buckets.
        '''
        return self.NUM_BUCKETS

    def __str__(self):
        '''
        Returns string representation of data inside hash set.
        '''
        result = ""
        bucketNr = 0
        for bucket in self.set:
            result += str(bucketNr) + ": " + ",".join(str(e) for e in bucket) + "\n"
            bucketNr += 1
        return result

