class TeaLeaf:
    
    def __init__(self, age):
        self._age = age

    # Getter
    @property
    def age(self):
        return self._age + 2
    
    # Setter
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf.age)