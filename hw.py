#task_33
#---------------------------------
class Godzilla:
    stomach = 0


    def __init__(self, weight):
        self.weight = weight
        self.stomach_place = self.stomach + self.weight
    def is_full(self):
        if self.stomach_place >= 90:
            return True
        else:
            return False



s =Godzilla(80)
print(s.stomach_place)
print(s.is_full())