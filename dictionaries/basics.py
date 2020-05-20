# Unordered key / value pair

sample = {"a": 1, "b": 2, "c": 3}

print(sample["b"])

sick_bands = {
    'Gorguts': 'Death Metal',
    'Morbid Angel': 'Death Metal',
    'Immortal': 'Black Metal',
    'Taake': 'Black Metal'
}

if sick_bands.get('Gorguts') == 'Death Metal':
    print('YEA BOI, best death metal band besides Negativa!')
