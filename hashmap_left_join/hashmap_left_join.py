from hash_tables.hash__tables import HashTable


def left_join(h1,h2):
    keys_1 = h1.keys
    keys_2 = h2.keys
    arr = []

    for key in keys_1:
        if key in keys_2:
            arr.append([f"{key}",f"{h1.get(key)}",f"{h2.get(key)}"])

        else:
            arr.append([f"{key}",f"{h1.get(key)}","NULL"])

    return arr

if __name__ == "__main__":
    hash_1 = HashTable()
    hash_2 = HashTable()
    hash_1.set('diligent','employed')
    hash_1.set('fond','enamored')
    hash_1.set('guide','usher')
    hash_1.set('outfit','garb')
    hash_1.set('wrath','anger')

    hash_2.set('diligent','idle')
    hash_2.set('fond','averse')
    hash_2.set('guide','follow')
    hash_2.set('flow','jam')
    hash_2.set('wrath','delight')

    print(left_join(hash_1,hash_2))



