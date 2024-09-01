import matplotlib.pyplot as plt
import math
import numpy as np

# Definição dos tipos de Pokémon e suas quantidades
types = {
    'Normal': 24,
    'Fire': 12,
    'Water': 32,
    'Electric': 9,
    'Grass': 14,
    'Ice': 5,
    'Fighting': 8,
    'Poison': 33,
    'Ground': 14,
    'Flying': 19,
    'Psychic': 14,
    'Bug': 12,
    'Rock': 11,
    'Ghost': 3,
    'Dragon': 3,
    'Streel': 2,
    'Fairy': 5
}
# Cálculo da entropia
total_pokemon = sum(types.values())
probabilities = {type_name: count / total_pokemon for type_name, count in types.items()}
entropy = -sum(probability * math.log2(probability) for probability in probabilities.values())

# Calculo da entropia máxima
num_types = len(types)
max_entropy = math.log2(num_types)

print(f"Entropia dos tipos de Pokémon: {entropy:.4f}")
print(f"Entropia Máxima dos tipos de Pokémon: {max_entropy:.4f}")

# Calcular a contribuição de cada tipo para a entropia
entropy_contributions = {type_name: -(probability * math.log2(probability)) for type_name, probability in probabilities.items()}

# Plotando o gráfico de barras para ilustrar o cálculo da entropia
plt.figure(figsize=(10, 6))
plt.bar(entropy_contributions.keys(), entropy_contributions.values(), color='orange')
plt.xlabel('Tipo de Pokémon')
plt.ylabel('Contribuição para a Entropia')
plt.title('Contribuição de Cada Tipo para a Entropia Total')
plt.xticks(rotation=45)
plt.show()
