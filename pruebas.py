from Hotel_pkg.hotel_env import Ht_distribution
from Guest import Guest




def main():
    guest1=Guest(id="086429", name="Marta", nights_at_hotel=7, room_type="suite")
    env = Ht_distribution("name", 5, 2, 2)
    hotel1=env.room_pricing(2)
    print("Rooms available before reservations: ")
    hotel1.available_rooms_summary()
    price = guest1.total_guest_price(hotel1.rooms_config)
    guest1.book_room(hotel1)
    print("Rooms available after reservations:")
    hotel1.available_rooms_summary()

if __name__ == "__main__":
    main()