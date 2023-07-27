# #d = {'A, E, I, O, U, L, N, S, T, R': 1, 'D, G': 2, 'B, C, M, P': 3, 'F, H, V, W, Y': 4, 'K': 5, 'J, X' : 8, 'Q, Z' : 10, }
# d = {'A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т ': 1, 'D, G, Д, К, Л, М, П, У': 2, 'B, C, M, P, Б, Г, Ё, Ь, Я ': 3, 'F, H, V, W, Y, Й, Ы': 4, 'K, Ж, З, Х, Ц, Ч ': 5, 'J, X, Ш, Э, Ю' : 8, 'Q, Z, Ф, Щ, Ъ' : 10, }
# a = list(input("Введите слово: ").upper())
# for i in a:
#     if i in d.keys:
#         print(d.values())

k = 'ноутбук'

# Введите ваше решение ниже
import re 
def Scrabble(k): 
    return bool(re.search("[а-яА-Я]", k)) 
Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т", 2:"Д, К, Л, М, П, У", 3:"Б, Г, Ё, Ь, Я", 4:"Й, Ы", 5:"Ж, З, Х, Ц, Ч", 8:"Ш, Э, Ю", 10:"Ф, Щ, Ъ"} 
Eng = { 1:"A, E, I, O, U, L, N, S, T, R ", 2:"D, G", 3:"B, C, M, P", 4:"F, H, V, W, Y", 5:"K", 8:"J, X"} 
if Scrabble(k.upper()):
    print(sum([c for i in k for c, v in Rus.items() if i in v])) 
else: 
    print(sum([c for i in k for c, v in Eng.items() if i in v]))




import re 
def Scrabble(p): 
    return bool(re.search("[а-яА-Я]", p)) 
Rus = { 1:"А, В, Е, И, Н, О, Р, С, Т", 2:"Д, К, Л, М, П, У", 3:"Б, Г, Ё, Ь, Я", 4:"Й, Ы", 5:"Ж, З, Х, Ц, Ч", 8:"Ш, Э, Ю", 10:"Ф, Щ, Ъ"} 
Eng = { 1:"A, E, I, O, U, L, N, S, T, R ", 2:"D, G", 3:"B, C, M, P", 4:"F, H, V, W, Y", 5:"K", 8:"J, X"} 
k = 'aaaaajj'
p = k.upper()
if Scrabble(p): 
    print(sum([q for i in p for q, v in Rus.items() if i in v])) 
else: 
    print(sum([q for i in p for q, v in Eng.items() if i in v]))