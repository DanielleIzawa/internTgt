# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua 
# preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def invertString(s):
  answer = ""
  for i in range(len(s) - 1, -1, -1):
    answer += s[i]
  return answer

string_original = input("Informe uma string: ")
invertString = invertString(string_original)

print("String original:", string_original)
print("String invertida:", invertString)
