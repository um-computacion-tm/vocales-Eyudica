# a in 'aeiou' da true
import unittest,pdb
def contar_vocales(valor):
    resultado={}
    valor=valor.lower()
    diccionario={'á':'a','é':'e','í':'i','ó':'o','ú':'u'}
    valor=valor.replace(" ","")
    for x in diccionario.keys():
        valor = valor.replace(x, diccionario[x])    
       
    for i in valor:
        if i  in 'aeiou':
            if i not in resultado:
                resultado[i]=0  
            resultado[i]+=1
    return resultado
""" while True:
    resultado=input("")
    print(contar_vocales(resultado)) """
class TestContarVocales(unittest.TestCase):
    def test_nada(self):            
        resultado=contar_vocales('zzz') 
        self.assertEqual(resultado,{})
    def test_a(self):
        resultado=contar_vocales('cas') 
        self.assertEqual(resultado,{'a':1})
    def test_aa(self):
        resultado=contar_vocales('casa') 
        self.assertEqual(resultado,{'a':2})
    def test_espacio(self):
        resultado=contar_vocales('probando con espacio') 
        self.assertEqual(resultado,{'a':2,'e':1,'i':1,'o':4})
    def test_mayuscula(self):
        resultado=contar_vocales('CASA') 
        self.assertEqual(resultado,{'a':2})
    def test_abecedario(self):
        resultado=contar_vocales('abEcedarIO') 
        self.assertEqual(resultado,{'a':2,'e':2,'i':1,'o':1})
    def test_final(self):
        resultado=contar_vocales('FINALMENTE el PROGRAMA funciona') 
        self.assertEqual(resultado,{'a':4,'e':3,'i':2,'o':2,'u':1})
        "a","éáíóú"
    def test_acento(self):
        resultado=contar_vocales('Además') 
        self.assertEqual(resultado,{'a':2,'e':1})
    def test_vocalesConAcento(self):
        resultado=contar_vocales('éáíóú') 
        self.assertEqual(resultado,{'a':1,'e':1,'i':1,'o':1,'u':1})


if __name__ == '__main__':
    unittest.main()  
