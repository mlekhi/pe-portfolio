import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
<<<<<<< HEAD
from app.text import about_text, work_text
=======
>>>>>>> 4888678 (Remove unused requirement, try to make marker bigger)

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    coords = [(34.037945, -117.677852), (45.231382, 16.577320), (45.537137, 119.137498)]
    markers = ""

    for id, (lat, lon) in enumerate(coords):
        # Create the marker and its pop-up for each shop
        idd = f"a{id}"
        print(idd)
        markers += "var {idd} = L.marker([{latitude}, {longitude}]);\
                    {idd}.options.iconSize = [100, 100];\
                    {idd}.addTo(map).bindPopup('{latitude}<br>{longitude}');".format(
            idd=idd,
            latitude=lat,
            longitude=lon,
        )

    # Render the page with the map
    return render_template(
        "index.html",
        markers=markers,
        lat=coords[0][0],
        lon=coords[0][1],
        title="MLH Fellow",
        url=os.getenv("URL"),
        photo="logo",
        about_text=about_text,
        work_text=work_text,
    )


@app.route("/maya")
def maya():
    return render_template(
        "index.html",
        title="Maya Lekhi",
        url=os.getenv("URL"),
        photo="maya",
        about_text="Rising Sophomore at Western University",
    )


@app.route("/joseph")
def joseph():
    return render_template(
        "index.html",
        title="Joseph Ma",
        url=os.getenv("URL"),
        photo="logo",
        about_text="blank",
    )


@app.route("/dilnaz")
def dilnaz():
    return render_template(
        "index.html",
        title="Dilnaz Uasheva",
        url=os.getenv("URL"),
        photo="dilnaz",
        about_text="Rising Sophomore at Minerva University",
    )


@app.route("/hobbies")
def hobbies():
    title = "Our Team's Hobbies"
    hobbies_list = [
        {"title": "Reading", "image": "reading.jpeg"},
        {"title": "Gardening", "image": "gardening.jpeg"},
        {"title": "Painting", "image": "painting.jpeg"},
        {"title": "Cooking", "image": "cooking.jpeg"},
    ]

    return render_template("hobbies.html", title=title, hobbies_list=hobbies_list)


if __name__ == "__main__":
    app.run()
