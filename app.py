from flask import Flask, render_template, request
from code_helper import movie_analysis

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def get_movie():
    if request.method == "POST":
        movie_id = request.form["Enter a movie ID"]
        try: 
            result = movie_analysis(movie_id)
            # print(result)
            if result:
                return render_template("Result.html",
                recommendation_result = result[4],
                rating = result[0],
                sentiment_result = result[2],
                similarity_result = result[3],
                freq_word_list = result[1])
        except:
            return render_template("error.html")
    else:
        return render_template("hello.html")


# @app.route('/test')
# def display():
#     t = [('a', 10), ('b', 9), ('c', 8), ('d', 7)]
#     return render_template('test_page.html', freq_word_list = t[:3])

if __name__ == "__main__":
    app.run(debug=True)