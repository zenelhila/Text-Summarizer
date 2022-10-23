import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq


def nltk_summarization(text):
    stop_words = set(stopwords.words("english"))
    frequency_word = {}
    for words in nltk.word_tokenize((text)):
        if words not in stop_words:
            if words not in frequency_word.keys():
                frequency_word[words] = 1
            else:
                frequency_word[words] += 1
    max_freq = max(frequency_word.values())

    for words in frequency_word.keys():
        frequency_word[words] = (frequency_word[words]/max_freq)

    listOfSentence = nltk.sent_tokenize(text)
    sentence_freq = {}
    for sentence in listOfSentence:
        for words in nltk.word_tokenize(sentence.lower()):
            if words in frequency_word.keys():
                if len(sentence.split(' ')) < 30:
                    if sentence not in sentence_freq.keys():
                        sentence_freq[sentence] = frequency_word[words]
                    else:
                        sentence_freq[sentence] += frequency_word[words]

    sentences_summarized = heapq.nlargest(7,sentence_freq, key = sentence_freq.get)

    summarization = ' '.join(sentences_summarized)

    return summarization


