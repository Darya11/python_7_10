class Vehicle:
    def __init__(self, model, lux_class):
        self.model = model
        self.lux_class = lux_class
        self.speed = 0
        self.volume = 0
        self.weight = 0

    def print_info(self):
        print('-----------------------------------')
        print('Model:         %s' % self.model)
        print('Lux class:       %s' % self.lux_class)
        print('Speed:        %s' % self.speed)
        print('Volume: %s' % self.volume)
        print('Weight: %s' % self.weight)