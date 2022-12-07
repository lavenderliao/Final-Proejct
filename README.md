# Python Movie IMDB search software
Created by Anna & Peiyu

Hi, welcome! We have created an website for text analysis on IMDB movie reviews :)

Python Movie IMDB search software is a created website that would offer users with text analysis, including sentimental analysisi, similarity and most common words for IMDB movie reviews.

To use our code for your searches on movie reviews, here are the instructions and a few things to be aware of!

# Installation:

Please make sure the following packages are installed:

cinemagoer:
```pip install cinemagoer```

Flask:
```pip install Flask```

# Instructions / How the code runs

The project maily consists of three files: code_helper.py, app.py and the templates for creating the webste

**Code_helper.py:-**

code_helper.py returns functions associated with generating text analysis results. The functions within the files would offer the following:
1. Wether the movie is recommended.
2. The rating of the moving (out of 10).
3. The sentiment analysis, which include the ratios of negative, positive and neutral scores. The three scores together would add up to 1. The sentiment with the highest ratio would have the most influence on the sentiment of the rating and comments.
4. The similarity of the first two comments. The higher the score, the greater the similarity.
5. A list of most common words exclusing stopwords.

The function movie_analysis would return the summary involving all results of text analysis included in our system.

**app.py:-**

app.py would load the working website that could return the results generated from code_helper.py. When you run this file, a website address would appear in the terminal, and that is where you could access our website.

The file uses Flask for creating the website and also uses the funciton movie_analysis to return the results

**Important:-** Our system uses IMDB movie ids for searches. Thus, when searching for a movie on our website, please use the IMDB movie id of the film you are looking for. To find the movie id, you may search a movie on the IMDb website, and then find the number after "tt" shown in the website address. 

For example, when you search for movie "Titanic" on IMDb, the website address is https://www.imdb.com/title/tt0120338/?ref_=nv_sr_srsg_0 

In this case, the movie_id would be 0120338

**templates:-**

The html templates within the template folders are created for creating the website pages. Please do not change them when running the python files.

# Enjoy using our website for your searches!
