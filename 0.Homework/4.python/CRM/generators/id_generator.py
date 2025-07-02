import uuid

class IdGenerator:
    
    def generate_id(self):
        id = uuid.uuid4()
        return str(id)

    
if __name__ == "__main__":
    generator = IdGenerator()
    id_list = [generator.generate_id() for _ in range(50)]
    for id in id_list:
        print(id)