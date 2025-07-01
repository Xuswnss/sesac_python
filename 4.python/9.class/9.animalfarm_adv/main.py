from cat import Cat
from dog import Dog
from panda import Panda
from farm import Farm

if __name__ == "__main__":
    dog = Dog('Buddy')
    cat = Cat('Kitty')
    panda = Panda('fubao')

    dog.speak()
    cat.speak()
    panda.speak()
    
    for _ in range(30):
        dog.move()
        cat.move()
        panda.move()
        
        
    
        
    farm = Farm()
    farm.move_all()
    # farm.add_animal('shark', 'www')
    

    #반복문을 통해 10번 움직임.