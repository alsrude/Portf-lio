x = 1


def escopo ():
    x =10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()


    print(x)
escopo()
print(x)