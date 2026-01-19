import unittest
import sys
import start


class TestSentimentAnalyzer(unittest.TestCase):

    def test_polarity_tag(self):
        polarities = [
            {'value': 0.01,"expected": "positive"},
            {'value': 0,"expected": "neutral"},
            {'value': -0.01,"expected": "negative"}
        ]

        for p in polarities:
            self.assertEqual(start.polarity_tag(p['value']), p['expected'])
    
    def test_polarity_extended_tag(self):
        polarities = [
            {'value': 0.6,"expected": "extremly positive"},
            {'value': 0.2,"expected": "positive"},
            {'value': -0.2,"expected": "neutral"},
            {'value': -0.6,"expected": "negative"},
            {'value': -0.601,"expected": "extremly negative"}
        ]

        for p in polarities:
            self.assertEqual(start.polarity_extended_tag(p['value']), p['expected'])

    def test_configure_log_level(self):
        levels = [
            {'value': 'INFO', 'expected': start.logging.INFO},
            {'value': 'WARN', 'expected': start.logging.WARN},
            {'value': 'DEBUG', 'expected': start.logging.DEBUG}
        ]
        
        for l in levels:
            self.assertEqual(start.configure_log_level(l['value']), l['expected'])

    def test_get_sentiment(self):
        sentiment = start.get_sentiment('this is my text', extended=False)
        self.assertEqual(len(sentiment), 3)
        self.assertIsInstance(sentiment, dict)

    def test_get_extendend_sentiment(self):
        sentiment = start.get_sentiment('this is my text', extended=True)
        self.assertEqual(len(sentiment), 7)
        self.assertIsInstance(sentiment, dict)

if __name__ == '__main__':
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSentimentAnalyzer)
    test_runner = unittest.TextTestRunner(verbosity=2).run(test_suite)
    ret = not test_runner.wasSuccessful()
    sys.exit(ret) 
    """ 
    Travis build status depends on exit code.
    Without the last line the exit code of the program is 0 even if the tests fail.
    """