from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')

@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/class_select', methods = ['GET','POST'])
def class_select():
    userdata = request.form
    race = userdata['race']
    job = userdata['job']
    level = int(userdata['level'])
    background = userdata['background']
    raceStats = model.races[race]
    jobStats = model.classes[job]
    backStats = model.backgrounds[background]
    barbTable = model.barbTable
    bardTable = model.bardTable
    return render_template('/class_select.html', level=level, race=race, job=job, background=background, raceStats=raceStats, jobStats=jobStats, backStats=backStats, barbTable = barbTable, bardTable = bardTable)