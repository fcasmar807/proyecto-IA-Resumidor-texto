[![Build Status](https://travis-ci.org/davidnuno-es/sentiment-analyzer.svg?branch=master)](https://travis-ci.org/davidnuno-es/sentiment-analyzer)
# Python Sentiment Analyzer

Programa que analiza los sentimientos de un texto

Este programa permite realizar un análisis simple o extendido de los sentimientos contenidos en un texto.
Utiliza la librería TextBlob para realizar dicho análisis.

## Usage

### Install requiremente
Este programa necesita librerías adicionales para funcionar. Para instalarlas, ejecute el siguiente comando:
```
pip install -r requirements.txt
```

### Command line
Analizar los sentimientos de un texto desde la linea de comandos es muy sencillo

Por ejemplo, para analizar un texto en ingles:
```
python start.py a I love your way bro
{'polarity': 0.5, 'subjectivity': 0.6, 'tag': 'positive'}
```

Si queremos realizar un análisis extendido:
```
python start.py a I love your way bro -e
{
    'meta': {
        'original': 'I love your way bro', 
        'original_lang': 'en'
    }, 
    'text': 'I love your way bro', 
    'polarity': 0.5, 
    'subjectivity': 0.6, 
    'value': 0, 
    'tag': 'positive', 
    'extended_tag': 
    'positive', 
    'assesment': ['love']
}
```

Por supuesto, podemos analizar texto en otros idiomas:
```
python start.py a Me encanta tu modo de vida amigo
{'polarity': 0.5, 'subjectivity': 0.6, 'tag': 'positive'}
```

### Import as module

### Help
Si tienes dudas, puedes solicitar la información de uso del programa con ```python start.py -h```

```
usage: start.py [-h] [-l LANG] [-e] [--log-level {INFO,WARN,DEBUG}]
                text [text ...]

String sentiment analyzer

positional arguments:
  text                  The text to be analyze. Could be into quotes or not

optional arguments:
  -h, --help            show this help message and exit
  -l LANG, --lang LANG  Text language. Default: en
  -e, --extended        Show analysis extended info
  --log-level {INFO,WARN,DEBUG}
                        Defines log level
```

### Test
Si quieres ejecutar los test unitarios:
```
python -m unittest test.py -v
```