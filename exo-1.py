land = ('France', 'Italie', 'Allemagne', 'Belgique')
score = (1925, 1423, 2012, 1836, 1730, 1556)

print(f"L'élément d’indice {score.index(score[0])} a pour valeur {score[0]}")
print(f"L'élément d’indice {score.index(score[2])} a pour valeur {score[2]}")
print(f"L'élément d’indice {score.index(score[-1])} a pour valeur {score[-1]}")

for index in range(len(land)):
    print(f"L'élément d’indice {index} a pour valeur {land[index]}")

land_sorted = sorted(land)
print(f"Elements par ordre alphabétique:\n")
for index in range(len(land_sorted)):
    print(f"{land_sorted[index]}\n")

print(f"Votre meilleur score est: {max(score)} ")

land_2 = ('Espagne', 'Portugal', 'Grèce')

lands = land + land_2
print(lands)

new_score = (1815, )

scores = score + new_score
print(scores)

print(f"Le tuple land comporte {len(land)} éléments ")
print(f"Le tuple score comporte {len(score)} éléments ")

print(sorted(land))
print(sorted(score))

print(sorted(land, reverse=True))
print(sorted(score, reverse=True))

def get_first_land_or_last_land(tup, reverse=False):
    sorted_tuple = sorted(tup, reverse=reverse)
    return sorted_tuple[0]

print(f'Le premier/dernier élément par ordre alphabétique est {get_first_land_or_last_land(land)}')

def get_best_score(tup):
    sorted_tuple = sorted(tup)
    return sorted_tuple[0]

print(f"Votre meilleur score est : {get_best_score(score)} ")
