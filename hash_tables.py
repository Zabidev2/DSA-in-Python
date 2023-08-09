class HashTable:
    def __init__(self, length):
        self.max_length = length
        self.array = [[] for i in range(self.max_length)]

    def get_hash(self, value):
        h = 0
        for char in value:
            h = h + ord(char)

        return h % self.max_length

    def __setitem__(self, key, value):
        index = self.get_hash(key)
        index_list = self.array[index]
        found = False
        for position, element in enumerate(index_list):
            if element[0] == key:
                index_list[position] = (key, value)
                found = True
                break
        if not found:
            index_list.append((key, value))

    def __getitem__(self,key):
        index = self.get_hash(key)
        index_list = self.array[index]

        for position, element in enumerate(index_list):
            if element[0] == key:
                print(f"index of {key} is {index}")
                print(f"Value is {element[1]}")

    def __delitem__(self,key):
        found = False
        index = self.get_hash(key)
        index_list = self.array[index]
        for position, element in enumerate(index_list):
            if element[0] == key:
                del index_list[position]
                found = True
                print(f"{key} removed from the list!")
        if not found:
            print(f"{key} not found in the list!")




t = HashTable(10)
t["march 6"] = 100
t["Feb"] = 150
t["Mar"] = 160
t["march 17"] = 120
print(t.array)
print(f"Lenght of hash Table is {len(t.array)}")
t["Feb"] = 250
print(t.array)
print(f"Lenght of hash Table is {len(t.array)}")


t['Mar']

del t["Feb"]
del t['Apr']

print(t.array)

