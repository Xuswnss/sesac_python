from cat import Cat
from dog import Dog
from farm import Farm

if __name__ == "__main__":
    dog = Dog('Buddy')
    cat = Cat('Kitty')

    dog.speak()
    cat.speak()
    
    for _ in range(30):
        dog.move()
        cat.move()
        
    # farm = Farm()
    # farm.add_animal('shark', 'www')
    

    #반복문을 통해 10번 움직임.