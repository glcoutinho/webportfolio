from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


posts = requests.get("https://api.npoint.io/dbe70b7cb2821bda980d").json()



@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    print(index)  # 2

    requested_post = None
    for blog_post in posts:
        print(blog_post["id"])
        if blog_post["id"] == index:
            requested_post = blog_post
            print(requested_post)

    return render_template("portfolio-details.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("portfolio-details.html")


if __name__ == '__main__':
    app.run(debug=True)
