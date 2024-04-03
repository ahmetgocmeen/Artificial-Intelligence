import libic as lb

w = lb.windowIC(800)
cityList = lb.readTSP2ListIC("berlin52.tsp")

lb.drawIC(cityList,w) 
input("Enter para continuar... ")
