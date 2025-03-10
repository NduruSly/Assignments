class Dog:
    def make_sound(self):
        print("Huuuu!")

class Cat:
    def make_sound(self):
        print("Meow!")

def process_sound(sound_object):
    sound_object.make_sound()

# Usage
dog = Dog()
cat = Cat()
process_sound(dog)
process_sound(cat)