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

if __name__ == "__main__":
    app.run(debug=True)