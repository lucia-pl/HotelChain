class Hotel:
    def __init__(self, name, rating, capacity):
        self.name = name
        self.rating = rating
        self.capacity = capacity
        self.rooms = []  
                
    #para el main
    def agregar_room(self, type, base_price):
        room = {
            'type': type,
            'base_price': base_price
        }
        self.rooms.append(room)
        

    def mostrar_info_hotel(self):
        print(f"Hotel: {self.name}")
        print(f"Valoración: {self.rating} estrellas")
        print(f"Total de rooms: {self.capacity}")
        print("types de rooms:")
        for room in self.rooms:
            print(f"  - type: {room['type']}, price Base: ${room['base_price']}")
    
    


