from animal_dictionary.models import Animal
import json

def run():
    animals = json.loads(open('animal.json').read())
    Animal.objects.all().delete()
    for animal in animals['animal']:
        new_animal = Animal.objects.create(
            name=animal['name'],
            trash_name = animal['trash_name'],
            description=animal['description'],
            trash_description = animal['trash_description'],
            image=animal['image'],
            trash=animal['trash'],
            sick=animal['sick'],
            sil=animal['sil'],
            target=animal['target'],
            latitude=animal['latitude'],
            longtitude=animal['longtitude'],
        )
        new_animal.save()
if __name__ == '__main__':
    run()