
class House:
    __slots__=['no_rooms', 'facade_color','address', 'type' ]
    def __init__(self, no_rooms, color, address, type, blab):
        self.no_rooms=no_rooms
        self.facade_color=color
        self.address=address
        self.type=type
        self.blab=blab
        
house_a = House(7,'pink','Dubai Hills', 'villa','This will give me an attribute error')
print(f'The house in {house_a.address} has {house_a.no_rooms} rooms; it is a {house_a.facade_color} {house_a.type}.')

# Limit the number of members -----> __slots__