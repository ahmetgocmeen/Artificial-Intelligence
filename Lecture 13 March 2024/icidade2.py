import libic as lb

w = lb.windowIC(800)

# Criar uma lista de IC
#l = [(1, 10.0, 15.0), (2, 15.0, 6.5), (3, 12.1, 19.7)]

# Ler um TSP para uma lista de IC
l = lb.readTSP2ListIC("berlin52.tsp")
# Desenhar graficamente a lista de IC
lb.drawIC(l,w)
input("Enter para continuar... ")

# Ler o TSP e a tour Ã³ptima para uma lista de IC
l = lb.readTSP2ListICOpt("berlin52.tsp", "berlin52.opt.tour")
# Desenhar graficamente a lista de IC
lb.drawIC(l,w)
input("Enter para continuar... ")