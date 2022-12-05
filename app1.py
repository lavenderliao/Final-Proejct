from flask import Flask, render_template, request
from code_helper import movie_analysis

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def get_movie():
    if request.method == "POST":
        movie = request.form["Enter a movie"]
        try: 
            result = movie_analysis(movie)
            print(result)
            if result:
                return render_template("Result.html")
        except:
            return render_template("error.html")
    else:
        return render_template("hello.html")

@app.route('/summary')
def search_result():

    if request.method == "POST":
        data = request.form 
        MOVIE = []
        rating_review = movie_analysis(render_template('result.html', items = MOVIE))
        
        #try: 
            #result = movie_analysis(rating_review)
           

@app.route('/test')
def display():
    t = [('a', 10), ('b', 9), ('c', 8), ('d', 7)]
    return render_template('test_page.html', freq_word_list = t[:3])

if __name__ == "__main__":
    app.run(debug=True)

