from textblob import TextBlob
import logging

def polarity_tag(polarity):
    if polarity > 0:
        return 'positive'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def polarity_extended_tag(polarity):
    if polarity >= 0.6:
        return 'extremly positive'
    elif polarity >= 0.2:
        return 'positive'
    elif polarity >= -0.2:
        return 'neutral'
    elif polarity >= -0.6:
        return 'negative'
    else:
        return 'extremly negative'

def __get_extended_analysis(original_text, language, analysis):
    result = {
        "meta":  {
            "original": original_text,
            "original_lang": language,
        },
        "text": analysis.__str__(),
        "polarity": analysis.sentiment.polarity,
        "subjectivity": analysis.sentiment.subjectivity,
        "tag": polarity_tag(analysis.sentiment.polarity),
        'extended_tag': polarity_extended_tag(analysis.sentiment.polarity),
        "assesment": [v[0][0] for x, v in enumerate(analysis.sentiment_assessments.assessments)]
    }
    return result

def get_sentiment(text, language="en", extended=True):
    logging.debug({'text': text, 'lang': language, 'ext': extended})
    tmp = TextBlob(text)
    if language != "en":
        logging.warn('Message in '+language+' language. Need to be translated')
        tmp = tmp.translate(to='en')
        logging.debug('Translated: '+tmp.__str__())

    if extended:
        logging.debug('Extended message reques')
        return __get_extended_analysis(text, language, tmp)
    else:
        logging.debug('Simple message request')
        return {'polarity': tmp.sentiment.polarity, 'subjectivity': tmp.sentiment.subjectivity, 'tag': polarity_tag(tmp.sentiment.polarity)}

def configure_log_level(lvl):
    log_level = logging.INFO
    if lvl == 'WARN':
        log_level = logging.WARN
    elif lvl == 'DEBUG':
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)
    logging.debug('Log level:' + lvl)
    return log_level
    
if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(description='String sentiment analyzer')
    parser.add_argument('text', nargs='+', type=str, help="The text to be analyze. Could be into quotes or not")
    parser.add_argument('-l', '--lang', type=str, help="Text language. Default: en", default="en", required=False)
    parser.add_argument('-e', '--extended', action='store_true', help='Show analysis extended info')
    parser.add_argument('--log-level', choices=['INFO', 'WARN', 'DEBUG'], help='Defines log level', required=False, default="INFO")
    args = parser.parse_args()

    configure_log_level(args.log_level)

    print(get_sentiment(" ".join(args.text), args.lang, args.extended))