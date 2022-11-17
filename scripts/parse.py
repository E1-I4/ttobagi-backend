from animal_dictionary.models import Animal
import json


def run():
    animals = json.loads(open('animal.json').read())
    for animal in animals['animal']:
        if Animal.objects.filter(name=animal['name']).exists():
            continue
        else:
            new_animal = Animal.objects.create(
                name=animal['name'],
                description=animal['description'],
                latitude=animal['latitude'],
                longtitude=animal['longtitude'],
            )
            new_animal.save()
if __name__ == '__main__':
    run()