from flask import Flask, request, render_template, redirect, url_for, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('assets', path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contract():
    return render_template("contact.html")

@app.route("/elements")
def elements():
    return render_template("elements.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/single-blog")
def singleBlog():
    return render_template("single-blog.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0')