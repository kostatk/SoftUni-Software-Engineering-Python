
class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        species_to_print = []
        name_to_print = ""
        if species == "mammal":
            species_to_print += self.mammals
            name_to_print = "Mammals"
        elif species == "fish":
            species_to_print += self.fish
            name_to_print = "Fishes"
        elif species == "bird":
            species_to_print += self.birds
            name_to_print = "Birds"
        result = f"{name_to_print} in {self.name}: {', '.join(species_to_print)}\nTotal animals: {Zoo.__animals}"
        return result


our_zoo = Zoo(input())
animals_to_add = int(input())

for animal in range(animals_to_add):
    type_of_animal, animal_name = input().split()
    our_zoo.add_animal(type_of_animal, animal_name)

print(our_zoo.get_info(input()))
