import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), photo='logo')

@app.route("/dilnaz")
def delete():
    return render_template('index.html', title="Dilnaz Uasheva", url=os.getenv("URL"), photo='dilnaz', about_text='Rising Sophomore at Minerva University')

@app.route("/hobbies")
def hobbies():
    title = "My Hobbies"
    hobbies_list = ["Cooking", "Reading", "Hiking", "Photography", "Gardening"]

    return render_template('hobbies.html', title=title, hobbies_list=hobbies_list)

if __name__ == '__main__':
    app.run()


