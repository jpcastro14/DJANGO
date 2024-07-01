""" notas = []


for x in range(3):
    nome = (input("Digite um nome:"))
    cod = int( input("Digite um numero:") )
    notas.append([nome,cod])
    print("Adicionado", "->" ,cod)
    print(notas)


for n in notas:
    cod = n[0]
    nota = n[1]
    print("O aluno",cod,"tirou a nota",nota) """


arr = []

for x in range(3):
    value1 = int((input("Digite um número:")))
    value2 = int((input("Digite o segundo número:")))
    arr.append([value1,value2])
    

sumarr = []

for x in arr:
    var1 = x[0]
    var2 = x[1]

    print ( var1 + var2, "<--", type(var1+var2))


print(len(arr),"<--- Tamanho do array")