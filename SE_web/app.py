from flask import Flask, request, redirect, url_for
from flask import render_template


app = Flask(__name__)

user_input = {}


@app.route('/', methods=["GET", "POST"])
def index():
    global user_input
    user_input = {
        "multiplayer": False,
        "singleplayer": False,
        "platforma": [],
        "producator": "",
        "pegi": int
    }

    if request.method == "POST":
        # default multiplayer: True
        if request.form.get("multiplayer") == "multiplayer_yes":
            user_input["multiplayer"] = True
        elif request.form.get("multiplayer") == "multiplayer_no":
            user_input["multiplayer"] = False
        else:
            user_input["multiplayer"] = True

        # default singleplayer: True
        if request.form.get("singleplayer") == "singleplayer_yes":
            user_input["singleplayer"] = True
        elif request.form.get("singleplayer") == "singleplayer_no":
            user_input["singleplayer"] = False
        else:
            user_input["singleplayer"] = True

        platforme_selectate = []
        if request.form.get("platforma_pc") == "platforma_pc":
            platforme_selectate.append("pc")
        if request.form.get("platforma_ps") == "platforma_ps":
            platforme_selectate.append("ps")
        if request.form.get("platforma_xbox") == "platforma_xbox":
            platforme_selectate.append("xbox")

        # default: pc
        if platforme_selectate:
            user_input["platforma"] = platforme_selectate
        else:
            user_input["platforma"] = ['pc']

        if request.form["producator"]:
            user_input["producator"] = request.form["producator"]

        # default pegi: 3
        if request.form.get("pegi"):
            result_pegi = request.form.get("pegi")[5:]
            user_input["pegi"] = int(result_pegi)
        else:
            user_input["pegi"] = 3

        return redirect(url_for("results"))
    else:
        return render_template('index.html')


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run()
