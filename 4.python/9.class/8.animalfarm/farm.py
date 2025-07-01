from animal import Animal
from typing import List

class Farm(Animal):
    def __init__(self):
        self.animals : List[Animal] = []
        self._name: str = name
        
    def add_animal(self, name:str, speak :str) -> None:
        newAnimal = Animal(name, speak)
        self.animals.append(newAnimal)
        print(f'새로운 동물이 추가 되었습니다.')
        
        
    def feed_all(self) -> None:
        print('동물들에게 밥 주는 중')
        for animal in self._animals:
            animal.feed("food")
    def show_all():
        pass