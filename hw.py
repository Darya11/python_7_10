#task_33
#---------------------------------
class Godzilla:

    def __init__(self, stomach=0, stomach_place=0):
        self.stomach = stomach
        self.stomach_place = stomach_place
    def eat(self, weight):
        self.stomach_place = (self.stomach + weight)
        return self.stomach_place
    def is_full(self):
        if self.stomach_place >= 90:
            return True
        else:
            return False


s =Godzilla()
print(s.eat(90))
print(s.is_full())