#FLAT

bos = []
def duzlestir(liste):
    for a in liste:
        if isinstance(a,list):
            duzlestir(a)
        else:
            bos.append(a)



a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
duzlestir(a)
print(bos)

------------------------------------
#### PROJE 2 LIST REVERSE SYSTEM####
def cevir_liste(i):
    i.reverse()
    for eleman in i:
        if type(eleman) == list:
            cevir_liste(eleman)


liste = [[1, 2], [3, 4], [5, 6, 7]]
cevir_liste(liste)
print(liste)
