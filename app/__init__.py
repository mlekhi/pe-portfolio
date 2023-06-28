import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.text import about_text, work_text_joseph, work_text_dilnaz, about_text_dilnaz, work_text, about_text_maya, \
    work_text_maya

load_dotenv()
app = Flask(__name__)


def mapping(coords):
    markers = ""

    for id, (lat, lon) in enumerate(coords):
        # Create the marker and its pop-up for each shop
        idd = f"a{id}"
        markers += "var {idd} = L.marker([{latitude}, {longitude}]);\
                            {idd}.addTo(map);".format(
            idd=idd,
            latitude=lat,
            longitude=lon,
        )
    return coords, markers


@app.route("/")
def index():
    coords = [(34.037945, -117.677852), (45.231382, 16.577320), (45.537137, 119.137498), (48.0196, 66.9237),
              (61.5240, 105.3188), (41.3775, 64.5853), (38.9637, 35.2433), (37.0902, -95.7129)]
    # Render the page with the map
    return render_template(
        "index.html",
        markers=mapping(coords)[1],
        lat=(mapping(coords))[0][0][0],
        lon=(mapping(coords))[0][0][1],
        title="MLH Fellow",
        url=os.getenv("URL"),
        photo="logo",
        about_text=about_text,
        work_text=work_text
    )


@app.route("/joseph")
def joseph():
    coords = [(34.037945, -117.677852), (45.231382, 16.577320), (45.537137, 119.137498)]

    # Render the page with the map
    return render_template(
        "index.html",
        markers=mapping(coords)[1],
        lat=(mapping(coords))[0][0][0],
        lon=(mapping(coords))[0][0][1],
        title="Joseph",
        url=os.getenv("URL"),
        photo="logo",
        about_text=about_text,
        work_text=work_text_joseph,
    )


@app.route("/maya")
def maya():
    coords = [(34.037945, -117.677852), (45.231382, 16.577320), (45.537137, 119.137498)]

    # Render the page with the map
    return render_template(
        "index.html",
        markers=mapping(coords)[1],
        lat=(mapping(coords))[0][0][0],
        lon=(mapping(coords))[0][0][1],
        title="Maya Lekhi",
        url=os.getenv("URL"),
        photo="profile",
        about_text=about_text_maya,
        work_text=work_text_maya,
    )


@app.route("/dilnaz")
def dilnaz():
    coords = [(48.0196, 66.9237), (61.5240, 105.3188), (41.3775, 64.5853), (38.9637, 35.2433), (37.0902, -95.7129)]

    # Render the page with the map
    return render_template(
        "index.html",
        markers=mapping(coords)[1],
        lat=(mapping(coords))[0][0][0],
        lon=(mapping(coords))[0][0][1],
        title="Dilnaz Uasheva",
        url=os.getenv("URL"),
        photo="dilnaz",
        about_text=about_text_dilnaz,
        work_text=work_text_dilnaz,
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
