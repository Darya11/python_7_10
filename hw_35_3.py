from vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, model, lux_class):
        super().__init__(model, lux_class)
        self.plane_rows = 0
        self.water_bottles_alloweds_allowed= 1
    def quantaty_water_bottles_prohibited(self,yours_bottles ):
        if self.water_bottles_alloweds_allowed <=1:
            self.water_bottles_alloweds_allowed = self.water_bottles_alloweds_allowed + yours_bottles
        else:
            'Number of bottles is prihibited'

    def print_info(self):
        super().print_info()
        print('Plane_rows:         %s' % self.plane_rows)
        print('Water bottles allowed:         %s' % self.water_bottles_alloweds_allowed)



