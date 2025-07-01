from animal import Animal

class Panda(Animal):
    def __init__(self, name : str):
        super().__init__(name, "PangPang")
        
          
    def speak(self):
        print('PangPang')
        
    def move(self) -> int:
        return super().move(20)
        
    
    