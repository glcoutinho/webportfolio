#   TODO 1: See examples
# main https://josemukorivo.com/#latest
# ideas https://nelsonfai.dev/#project
#       https://sebkay.com/

# basics https://www.rida.dev/
# decorations https://parthmittal.netlify.app/
#   templates
# https://bootstrapmade.com/demo/iPortfolio/


#   TODO 2: Code the template
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)

posts = requests.get("https://api.npoint.io/424f38e0b2008d01e0a8").json()

@app.route("/")
def home():
    # demasiado formal?
    # Cores bem?
    # CV intro ou no intro summary bug
    # Favicon
    # what bold??
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    print(index) # 2

    requested_post = None
    for blog_post in posts:
        print(blog_post["id"])  # 1 2 3 4
        if blog_post["id"] == index:
            requested_post = blog_post
            print(requested_post)

    return render_template("portfolio-details.html", post=requested_post)
# {{ url_for('show_post', index=post.id) }}

@app.route("/about")
def about():
    # fazer link direto de imagens
    # conteudo do api
    return render_template("portfolio-details.html")


if __name__ == '__main__':
    app.run(debug=True)


#   TODO 3: Code the backend code including the blog display

#   Todo 4: Decorate and bugs

#   Todo 5: Write the text and correcpt