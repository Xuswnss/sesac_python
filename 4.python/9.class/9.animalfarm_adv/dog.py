from animal import Animal

class Dog(Animal):
    def __init__(self, name:str):
        super().__init__(name, "Woof")
        
    def speak(self):
        print('Woof')
        
    def move(self) -> int:
        return super().move(10)
        
    
    
    
    
    