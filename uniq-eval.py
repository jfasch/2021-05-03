def uniq(input_liste):
    output_liste = []
    elements_seen = set()
    for element in input_liste:
        if element not in elements_seen:
            elements_seen.add(element)
            output_liste.append(element)
    return output_liste

liste_als_string = input('Hier Liste herschreiben (und zwar unbedingt in Python-Syntax): ')

# liste_als_string in Python Liste verwandeln ...
l = eval(liste_als_string)

l2 = uniq(l)

for element in l2:
    print(element)    # -> 42, 1, 666, 5
