from animal import Animal

class Cat(Animal):
    def __init__(self, name : str):
        super().__init__(name, "Meow")
        
          
    def speak(self):
        print('Meow')
        
    def move(self) -> int:
        return super().move(5)
        
    
    