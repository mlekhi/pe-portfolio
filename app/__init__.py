import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), photo='logo', about_text="I'm an MLH Fellow!", work_text="I've worked at x, y, z.")

@app.route("/maya")
def maya():
    return render_template('index.html', title="Maya Lekhi", url=os.getenv("URL"), photo='maya', about_text='Rising Sophomore at Western University')

@app.route("/joseph")
def joseph():
    return render_template('index.html', title="Joseph Ma", url=os.getenv("URL"), photo='logo', about_text='blank')

@app.route("/dilnaz")
def dilnaz():
    return render_template('index.html', title="Dilnaz Uasheva", url=os.getenv("URL"), photo='dilnaz', about_text='Rising Sophomore at Minerva University')

@app.route("/hobbies")
def hobbies():
    title = "Our Team's Hobbies"
    hobbies_list = [
        {
            'title': 'Reading',
            'image': 'reading.jpeg'
        },
        {
            'title': 'Gardening',
            'image': 'gardening.jpeg'
        },
        {
            'title': 'Painting',
            'image': 'painting.jpeg'
        },
        {
            'title': 'Cooking',
            'image': 'cooking.jpeg'
        }
    ]

    return render_template('hobbies.html', title=title, hobbies_list=hobbies_list)

if __name__ == '__main__':
    app.run()
