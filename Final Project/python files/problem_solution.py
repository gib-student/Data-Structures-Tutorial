''' Query practice problem
    In this problem, most of the problem will be solved for you
    except for one or two small errors in the code. You will
    need to learn how this query works and fix the problems.
    
    Premise: This query is filled with key-value pairs to be 
    converted into a dictionary. The query has a key at every even 
    index (0 is considered even), and its value pair in the adjacent 
    odd position. The purpose of the program is to convert the 
    query into a dictionary.'''

class Dict_Query:
    def __init__(self):
        self._queue= []
    
    def enqueue(self, key, value):
        self._queue.append(key)
        self._queue.append(value)
    
    def dequeue(self):
        key = self._queue[0]
        value = self._queue[1]
        del self._queue[0]
        del self._queue[0]
        return (key, value)
    
    def convert_to_dict(self):
        d = {}
        while self.__len__() > 0 and self.__len__() % 2 == 0:
            pair = self.dequeue()
            d[pair[0]] = pair[1]
        return d

    def __len__(self):
        return len(self._queue)

# Demonstrate query usage
query = Dict_Query()
query.enqueue('name', 'Jethro')
query.enqueue('age', 45)
query.enqueue('favorite_food', 'Mutton')
query.enqueue('position', 'Elder')
query.enqueue('holiness_level', 9001)

dict = query.convert_to_dict()

print(dict)