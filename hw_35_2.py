from vehicle import Vehicle


class Train(Vehicle):
    def __init__(self, model, lux_class):
        super().__init__(model, lux_class)
        self.tickets_payement = 0
        self.number_of_seats = 300
    def free_places(self, reserved_places):
        self.number_of_seats = self.number_of_seats - reserved_places

    def print_info(self):
        super().print_info()
        print('Ticketspayement:         %s' % self.tickets_payement)
        print('Number of seats:         %s' % self.number_of_seats)


