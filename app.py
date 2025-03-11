from flask import Flask, render_template, request

from predict import prediction  # Importing your prediction function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = str(request.form["user_text"])
        result = prediction(user_input) 
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
