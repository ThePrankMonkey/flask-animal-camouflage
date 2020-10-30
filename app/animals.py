import json


class Animal:
    def __init__(self, animal_type, filepath, name, location):
        self.animal_type = animal_type
        self.filepath = filepath
        self.name = name
        self.location = location

    def json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return f"{self.animal_type}: {self.name}"


camo = [
    Animal("camo", "camo/camo01.jpg", "Stick Insect", None),
    Animal("camo", "camo/camo02.jpg", "Desert Snake", None),
    Animal("camo", "camo/camo03.jpg", "Leopard", None),
    Animal("camo", "camo/camo04.jpg", "Gecko", None),
    Animal("camo", "camo/camo05.jpg", "Orchid Mantis", None),
    Animal("camo", "camo/camo06.jpg", "Parrot", None),
    Animal("camo", "camo/camo07.jpg", "Spotted Deer", None),
    Animal("camo", "camo/camo08.jpg", "Great Potoo bird", None),
    Animal("camo", "camo/camo09.jpg", "Frog", None),
    Animal("camo", "camo/camo10.jpg", "Snow Leopard", None),
    Animal("camo", "camo/camo11.jpg", "Mossy Leaf-Tailed Gecko", None),
    Animal("camo", "camo/camo12.jpg", "Lichen Spider", None),
    Animal("camo", "camo/camo13.jpg", "Leaf Frog", None),
    Animal("camo", "camo/camo14.jpg", "Common Baron Caterpillar", None),
    Animal("camo", "camo/camo15.jpg", "Seahorse", None),
    Animal("camo", "camo/camo16.jpg", "Tropidoderus Childrenii", None),
    Animal("camo", "camo/camo17.jpg", "Bat-Faced Toad", None),
]

expose = [
    Animal("expose", "expose/expose01.jpg", "Flamingo", None),
    Animal("expose", "expose/expose02.jpg", "Raccoon", None),
]