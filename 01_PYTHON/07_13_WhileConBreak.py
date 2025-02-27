a=5
while a>0:
    print(a,end=" ")
    if a==3:
        break # Interrumpe el ciclo, segun condicion y sale al print final
    a-=1
print("\nSalimos del ciclo while con a : {}".format(a))