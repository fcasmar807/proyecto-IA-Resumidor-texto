# proyecto-IA-Resumidor-texto
Este script utiliza gensim para generar resúmenes de mejor calidad y también es capaz de procesar archivos PDF utilizando pytesseract para extraer texto de los documentos PDF. Al momento de ejecutarlo solicita al usuario la ubicación del archivo, sino está en una ruta en específico entonces asume que está en la ruta actual. Luego lista los archivos disponibles en esa ubicación, después permite al usuario seleccionar un archivo y luego resume ese archivo. El resúmen se guarda en un nuevo archivo de texto en la misma ubicación.

Resu.py permite al usuario ingresar la cantidad de sentencias que desea incluir en el resúmen, el resúmen se generará según el número de sentencias ingresadas por el usuario. Esto proporciona una mayor flexibilidad en la generación de resúmenes de documentos de texto.

GIF
Instalación
Clonamos el repositorio

git clone https://github.com/Yextep/Resu
Accedemos a la carpeta

cd Resu
Instalamos requerimientos

pip install -r requeriments.txt
Ejecutamos el Script

python3 resu.py
