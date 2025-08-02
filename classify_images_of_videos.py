import os

# Ruta de la carpeta donde están las imágenes
carpeta_imagenes = 'OneDrive\Documentos\Sexto_Semestre\Machine_Learning_I\Parcial3\ProyectoFinal\dataset\drowsy' # Para 'notdrowsy' cambiar lo último a -> 'dataset\\notdrowsy'
dic = {}
string = ""

# Recorremos todos los archivos en la carpeta
for archivo in os.listdir(carpeta_imagenes):
    name = archivo
    partes = name.split('_')
    name = '_'.join(partes[:-2])

    if(name != string):
        string = name

        dic[string] = 1
    else:
        dic[string] += 1

for key, value in dic.items():
    print(key, " ", value)
    print()
