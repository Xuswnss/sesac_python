import random
class AgeGenerator:
   
   def generate_age(self):
       return random.randint(12,100)
   

if __name__ == "__main__":
    generator = AgeGenerator()
    age_list = [generator.generate_age() for _ in range(50)]
    for address in age_list:
        print(address)