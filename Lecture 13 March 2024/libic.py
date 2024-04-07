import math
import random
from tkinter import *

def minmaxListaIC(l):
    min,max = l[0][1], l[0][1]
    for ic in l:
        if ic[0] < min:
            min = ic[0]
        if ic[0] > max:
            max = ic[0]
        if ic[1] < min:
            min = ic[1]
        if ic[1] > max:
            max = ic[1]
    return min,max

def convertXY(x, y, min, max, size):
    limite = 15
    ratio =  (size - 2*limite) / (max-min)
    xNew = (limite + (x-min) * ratio)
    yNew = (limite + (y-min) * ratio)
    return xNew, yNew

def windowIC(tamanho):
    window = Tk()
    window.title("iCidade")
    window.geometry("+10+10")
    window.minsize(tamanho,tamanho)

    c = Canvas(window,bg="black", height=tamanho, width=tamanho)
    return window, c, tamanho

def drawIC(l, windefs):
    (window, c, tamanho) = windefs
    c.delete('all')

    min, max = minmaxListaIC(l)
    for i in range(-1,len(l)-1):
        xi,yi = convertXY(l[i][0], l[i][1], min, max, tamanho)
        xf,yf = convertXY(l[i+1][0], l[i+1][1], min, max, tamanho)
        c.create_line(xi,yi,xf,yf, fill="blue", width=2)
    for ic in l:
        x,y = convertXY(ic[0], ic[1], min, max, tamanho)
        c.create_oval(x-5,y-5,x+5,y+5, fill="yellow")
        c.create_text(x,y, text=str(ic[0]), fill="black", font=('Helvetica', '8', 'bold'))

    c.pack()
    window.update()
    return windefs


def checkStrBegin(s, txt):
    return (s == txt[0:len(s)])

def readTSP2ListIC(file):
    readIC = False
    listaIC = []
    fin = open(file,"r")
    llinhas = fin.read().splitlines()
    for linha in llinhas:
        if checkStrBegin("NODE_COORD_SECTION", linha):
            readIC = True
            continue
        if checkStrBegin("EOF", linha):
            readIC = False
            break
        if readIC:
            lista = linha.split()
            ic = float(lista[1]), float(lista[2])
            listaIC.append(ic)
    fin.close()
    return listaIC

def readTSP2ListICOpt(file, fileOpt):
    listaIC = readTSP2ListIC(file)
    readID = False
    listaOpt = []
    fin = open(fileOpt,"r")
    llinhas = fin.read().splitlines()
    for linha in llinhas:
        if checkStrBegin("TOUR_SECTION", linha):
            readID = True
            continue
        if checkStrBegin("EOF", linha):
            readID = False
            break
        if readID:
            id = int(linha)
            if(id==-1):
                readID = False
                break
            listaOpt.append(listaIC[id-1])
    fin.close()
    return listaOpt

