from Kopalnie.params import list_of_objects


def most_nutritive_coal_min(list_of_objects):
    result = sorted(list_of_objects, key=lambda x: x.get_mount_of_energy(), reverse=True)[0]
    return result.name, result.get_mount_of_energy()

print(most_nutritive_coal_min(list_of_objects))