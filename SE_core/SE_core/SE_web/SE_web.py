import os

from flask import Flask, request, redirect, url_for
from flask import render_template

app = Flask(__name__)

preferences: dict = {}
my_questions: dict = {}

getPreferenceMethod = None


@app.route('/', methods=["GET", "POST"])
def index():
    global preferences, my_questions

    preferences = {
        "multiplayer": False,
        "singleplayer": False,
        "platforma": [],
        "producator": "",
        "pegi": int,
        "like_to_play_with_others": False,
        "like_to_play_alone": False,
        "both_alone_and_with_others": False
        }

    preferences['questions'] = []

    if request.method == "POST":
        # default multiplayer: True
        if request.form.get("multiplayer") == "multiplayer_yes":
            preferences['questions'] += ["like_to_play_with_others"]
        elif request.form.get("multiplayer") == "multiplayer_no":
            preferences['questions'] += ["like_to_play_alone"]
        elif request.form.get("multiplayer") == "multiplayer_both":
            preferences['questions'] +=["both_alone_and_with_others"]

        platforme_selectate = []
        if request.form.get("platforma_pc") == "platforma_pc":
            platforme_selectate.append("pc")
        if request.form.get("platforma_ps") == "platforma_ps":
            platforme_selectate.append("ps")
        if request.form.get("platforma_xbox") == "platforma_xbox":
            platforme_selectate.append("xbox")

        # default: pc
        if platforme_selectate:
            preferences["platforma"] = platforme_selectate
        else:
            preferences["platforma"] = None  # by default nu a selectat nimic

        if request.form["producator"]:
            preferences["producator"] = request.form["producator"]

        # default pegi: 3
        if request.form.get("pegi"):
            result_pegi = request.form.get("pegi")[5:]
            preferences["pegi"] = int(result_pegi)
        else:
            preferences["pegi"] = 18  # ok

        for keyword in my_questions:
            if request.form.get(keyword) == keyword+"_yes":
                preferences['questions'] += [keyword]

        return redirect(url_for("results"))
    else:
        file1 = open(os.path.join(os.path.dirname(__file__), '../knoledge_base/questions1.txt'), 'r')
        questions = file1.readlines()
        file1.close()

        for question_kw in questions:
            keyword = question_kw[:question_kw.index(':')-1]
            question = question_kw[question_kw.index(':')+2:-1]
            my_questions[keyword] = question

        return render_template('index.html', my_questions=my_questions)


@app.route('/results')
def results():
    return render_template('results.html', results=getPreferenceMethod(preferences))


def set_callback(funptr):
    global getPreferenceMethod
    getPreferenceMethod = funptr


def main_loop():
    if getPreferenceMethod is None:
        raise Exception("no function assign for callback")
    app.run()


if __name__ == '__main__':
    main_loop()
