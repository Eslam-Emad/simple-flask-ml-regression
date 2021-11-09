import uuid

from flask import render_template, request
from joblib import load

from app import app
from app.containers import Container


@app.route("/", methods=['GET', 'POST'])
def home():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href='static/base-img.svg')
    else:
        container = Container()
        text = request.form['text']
        random_string = uuid.uuid4().hex
        path = "static/" + random_string + ".svg"
        model = load("app/model.joblib")
        np_arr = container.repository_provider().floats_string_to_input_arr(text)
        container.repository_provider().make_picture('app/AgesAndHeights.pkl', model, np_arr, "app/"+path)
        return render_template('index.html', href=path)
