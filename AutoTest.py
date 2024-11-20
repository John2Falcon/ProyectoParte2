import Analizador_De_Codigo as LOC

# si agregan mas pruebas solo agreguen el nombre del archivo

archivos = ['Archivo_ABC.py','Archivo_XYZ.py','Prueba_A.py','Prueba_B.py','Prueba_C.py',
             'Prueba_D.py','Prueba_E.py','Prueba_F.py','Prueba_G.py','Prueba_H.py','Prueba_I.py']
#archivos = ['Prueba1.py','prueba2.py','prueba3.py']


for archivo in archivos: 
    file_path = './pruebas/' + archivo  
    analyzer = LOC.AnalizadorDeCodigo(file_path)
    analyzer.analizar_archivo()
    analyzer.informe()
