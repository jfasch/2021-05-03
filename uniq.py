def uniq(input_liste):
    output_liste = []
    elements_seen = set()
    for element in input_liste:
        if element not in elements_seen:
            elements_seen.add(element)
            output_liste.append(element)
    return output_liste

l = [42, 1, 42, 666, 1, 5, 666]
l2 = uniq(l)

for element in l2:
    print(element)    # -> 42, 1, 666, 5
