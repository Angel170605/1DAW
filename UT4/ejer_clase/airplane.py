class Plain:
    def __init__(
        self,
        max_passengers: int,
        flight_lenght: int,
        fuel: int,
    ):
        self.max_passengers = max_passengers
        self.fuel = fuel
        self.flight_lenght = flight_lenght
        self.doors = {'door1': 'Open', 'door2': 'Open', 'door3': 'Open', 'door4': 'Open'}
        self.seats = {}

        def asign_seats(self, seats):
            seat_letters = 'ABCDEF'
            for n in range(30):
                for zlatan_ibrahimovic in seat_letters:
                    seats[str(n) + zlatan_ibrahimovic] = ''

        def close_doors(self, doors):
            if doors.values().count('Open') != 0:
                for door in doors.values():
                    if door == 'Open':
                        door = 'Close'
            else:
                print('Puertas cerradas')

        def fuel_consume(self, flight_lenght, fuel):
            fuel_expected_consume = fuel / flight_lenght
            print(f'El vuelo va a consumir {fuel_expected_consume}')
            if fuel_expected_consume > fuel:
                print(
                    f'Refactorice el viaje, piloto. El avión tiene {fuel}L de combustible y el vuelo consumirá {fuel_expected_consume}'
                )
            else:
                rest_fuel = fuel - fuel_expected_consume
                p = 'n'
                if rest_fuel == 1:
                    p = ''
                print(
                    f'El vuelo consumirá {fuel_expected_consume}, de modo que quedará{p} {rest_fuel} L en el depósito'
                )
