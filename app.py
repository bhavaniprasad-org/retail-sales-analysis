from flask import Flask, render_template, request
from analysis import generate_charts
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    category_chart = None
    profit_chart = None
    segment_chart = None

    if request.method == "POST":

        file = request.files["file"]

        if file:

            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(file_path)

            category_chart, profit_chart, segment_chart = generate_charts(file_path)

    return render_template(
        "index.html",
        category_chart=category_chart,
        profit_chart=profit_chart,
        segment_chart=segment_chart
    )


if __name__ == "__main__":
    app.run(debug=True)