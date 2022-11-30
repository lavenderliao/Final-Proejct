# Data source

# Note: 
# The IMDB API sometimes does not work and will show 'IndexError: list index out of range', 
# just need to rerun a couple of times, one of the times would work

# The result would look like this:
# Not Recommend!
# The rating is 6.2
# The sentiment analysis results are {'neg': 0.075, 'neu': 0.667, 'pos': 0.257, 'compound': 1.0}
# The similarity result are 58
# The most common words are
#          31
# roberts          22
# film     21
# clooney          21
# movie    14
# romantic         12
# paradise         12
# good     10
# two      9
# ticket   9
# comedy   8
# one      7
# julia    7
# get      7
# actors   7
# will     6
# script   6
# made     6
# love     6
# great    6


from imdb import Cinemagoer
import sys
from unicodedata import category

# create an instance of the Cinemagoer class
ia = Cinemagoer()

def get_id(movie):
    """
    movie: string
    """
    search_result = ia.search_movie(movie)
    print(search_result)
    if len(search_result) == 0:
        print('Movie not found!')
        return
    else:
        movie_data = search_result[0] 
    movie_id = movie_data.movieID
    return movie_id

def get_point(movie_id):
    series = ia.get_movie(movie_id)
    rating = series.data['rating']
    return rating


# get comments
def get_comment_list(movie_id):
    '''
    return ... data type, parameters
    '''
    movie_reviews = ia.get_movie_reviews(movie_id)
    # check length of movie reviews
    comments = []
    for i in range(0,10):
        x = movie_reviews['data']['reviews'][i]['content']
        comments.append(x)
    return comments
    

def get_comments_str(comment_list):
    """Return all reviews in one string
    
    movie: string

    return: string
    """
    comment_text = ''.join(comment_list)
    return comment_text

# word frequencies

def process_file(filename):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding='utf8')

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist


def process_text(text):
    """Makes a histogram that contains the words from a text.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for word in text.split():
            # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

            # update the histogram
        hist[word] = hist.get(word, 0) + 1

    return hist

def most_common(hist, excluding_stopwords=True):
    """Makes a list of word-freq pairs(tuples) in descending order of frequency.
    hist: map from word to frequency
    excluding_stopwords: a boolean value. If it is True, do not include any stopwords in the list.
    returns: list of (frequency, word) pairs
    """
    t = []

    stopwords = process_file('data/stopwords.txt')

    stopwords = list(stopwords.keys())
    # print(stopwords)

    for word, freq in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue

        t.append((freq, word))

    t.sort(reverse=True)
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    # print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)

def word_frequency(comment_str):
    """
    comment_str: a string of all comments
    Return list of (frequency, word) pairs
    """
    hist = process_text(comment_str)
    t = most_common(hist, True)
    return t

# sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment(comment_str):
    score = SentimentIntensityAnalyzer().polarity_scores(comment_str)
    return score

# similarity of two comments
from thefuzz import fuzz
import random
def get_similarity(comment_list):
    """
    compare the similarity of the first two comments
    Return similarity score
    """
    first, second = comment_list[:2]
    result = fuzz.token_set_ratio(first, second)
    return result


def movie_analysis(movie_id):
    rating = get_point(movie_id)
    comment_list = get_comment_list(movie_id)
    comment_str = get_comments_str(comment_list)
    t = word_frequency(comment_str)
    sentiment_result = sentiment(comment_str)
    similarity_result = get_similarity(comment_list)
    if rating > 7 and sentiment_result['pos'] > 0.05:
        print('Recommend!')
        print('The rating is ' + str(rating))
        print('The sentiment analysis results are' + sentiment_result)
        print('The similarity result are'+ similarity_result)
        print('The most common words are')
        for freq, word in t[0:20]:
            print(word, '\t', freq)
    else:
        print('Not Recommend!')
        print('The rating is ' + str(rating))
        print('The sentiment analysis results are', sentiment_result)
        print('The similarity result are', similarity_result)
        print('The most common words are')
        for freq, word in t[0:20]:
            print(word, '\t', freq)

def main():
    # movie_analysis('Ticket to Paradise')
    # movie_title = 'Titanic'
    # movie_id = get_id(movie_title)
    # print(movie_id)
    movie_id = '14109724'
    movie_analysis(movie_id)

if __name__ == "__main__":
    main()