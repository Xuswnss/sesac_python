
class Animal:
    def __init__(self, name : str, speak : str) -> None:
        self._name = name
        self._energy = 100
        self._speak = speak
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name : str):
        self._name = name
        print(f'name : {self._name}')
        
    @property
    def energy(self) -> int:
        return self._energy
    
    @energy.setter
    def energy(self, energy: int):
        if self._energy > 0:
            self._energy = energy
        else: print('에너지가 소진되면 움직일 수 없습니다.')
        print(f'energy :{self._energy}')
        
    @property
    def speak(self) -> str:
        print(f'{self._name}은 {self._speak}~')
        return self._speak
    
    @speak.setter
    def speak(self, speak : str):
        self._speak = speak
        
        
        
    def move(self, amount : int) -> int:
        print(f'{self._name}의 에너지는{self._energy}')
        if self._energy > 0:
            self._energy -= amount
        else: 
            print('움직일 수 없습니다')
            return

        return self._energy
    
    
    def feed(self, food:str) -> None:
        self._energy += 50
        print(f'{self._name}은 {food}를 먹었습니다. 잔여 에너지 : {self._energy}')
    
    
        
        
    def animal_info(self):
        print(f"i'am{self._name}, my energy is {self._energy}!!!")