a=7
while bool(a):   # En Python cualquier boolen es True excepto False, None, 0, "", [], (), {}. En este caso a=7 es True
    # Asi que la condicion se cumplira como True hasta que a=0
    a-=1
    if a%2==0:
        print("{a} Es par y salta a siguinete iteracion".format(a=a))
        continue
    print("El valor de a {}".format(a) )
print("Salimos del ciclo while")