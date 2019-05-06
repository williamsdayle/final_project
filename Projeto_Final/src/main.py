import methods as mt



dificuldade = int(input("1 - FÁCIL\n2 - MÉDIO\n3 - DIFÍCIL\n"))
if dificuldade == 1:
    pop = int(input("Tamanho da população a resolver o problema\n"))
    iter = int(input("Numero de iterações\n"))
    schema = int(input("1 - Schema DE/RAND/1/BIN\n2 - Schema DE/RAND/2\n3 - Schema DE/BEST/2\n"))
    if schema == 1:
        mt.process_facil_schema1(iter, pop)
    if schema == 2:
        mt.process_facil_schema2(iter, pop)
    if schema == 3:
        mt.process_facil_schema3(iter, pop)

if dificuldade == 2:
    pop = int(input("Tamanho da população a resolver o problema\n"))
    iter = int(input("Numero de iterações\n"))
    schema = int(input("1 - Schema DE/RAND/1/BIN\n2 - Schema  DE/RAND/2\n3 - Schema DE/BEST/2\n"))
    if schema == 1:
        mt.process_medio_schema1(iter, pop)
    if schema == 2:
        mt.process_medio_schema2(iter, pop)
    if schema == 3:
        mt.process_medio_schema3(iter, pop)
2
if dificuldade == 3:
    pop = int(input("Tamanho da população a resolver o problema\n"))
    iter = int(input("Numero de iterações\n"))
    schema = int(input("1 - Schema DE/RAND/1/BIN\n2 - Schema DE/RAND/2\n3 - Schema DE/BEST/2\n"))
    if schema == 1:

        mt.process_dificil_schema1(iter, pop)
    if schema == 2:
        mt.process_dificil_schema2(iter, pop)
    if schema == 3:
        mt.process_dificil_schema3(iter, pop)

