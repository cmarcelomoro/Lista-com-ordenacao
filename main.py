def combsort(lista):
  n = len(lista)#define o numero de elementos
  gap = int(n/1.3)
  while gap >= 1:
    #todo
    indice = 0
    while indice+gap < n:
      if lista[indice] > lista[indice+gap]:#troca
        lista[indice],lista[indice+gap]=lista[indice+gap],lista[indice]
        indice = -1
      indice +=1 #incremento o indice
    gap = int(gap/2)#pega a parte inteira da divisao
 
 
lista = []
def menu():
    print("1 - Adicionar nome na lista")
    print("2 - Excluir nome da lista")
    print("3 - Ver lista")
    print("4 - Sair")
menu()
op = int(input("O que você gostaria de fazer?\n"))
while op != 0:
    if op ==1:
       qtd = int(input("Quantos nomes você gostaria de inserir na lista?\n"))
       for i in range(qtd):
           nome = input("Digite um nome\n")
           lista.append(nome.lower())  ##insere na lista os nomes desejados
           combsort(lista)
       print(lista)
       menu()
       op = int(input("O que você gostaria de fazer?\n"))
    if op == 2:
        if len(lista) == 0:
            print("A lista está vazia!")
            menu()
            op = int(input("O que você gostaria de fazer?\n"))

        else :
            qtd = int(input("Quantos nomes você gostaria de excluir da lista?\n"))

            i = 0
            for i in range(qtd):  ## percorre a lista e procura o nome para exclusão
                nome = input("Qual nome você quer excluir da lista?\n")
                if nome == lista[i]:
                    lista.remove(nome)
            print("O nome", nome, "foi excluido da lista\n")
            print(lista)
            menu()
            op = int(input("O que você gostaria de fazer?\n"))
    if op == 3:
        print(lista)
        menu()
        op = int(input("O que você gostaria de fazer?\n"))

    if op == 4:
         break
