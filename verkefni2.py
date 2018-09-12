from sys import argv

import bottle
from bottle import *
bottle.debug(True)

@route("/")
def index():
    return """ <h2>Verkefni2</h2> 
     <a href=/a> Liður A </a>
     <a href=/b> Liður B </a>"""


@route("/a")
def a():
    return """
    <h2> Verkefni 2 - A liður </h2>
    <a href="/sida/1"> síða 1 </a>
    <a href="/sida/2"> síða 2 </a>
    <a href="/sida/3"> síða 3 </a>
    <a href="/"> Forsíða </a>"""

@route("/sida/<id>")
def page(id):
    if id == "1":
        return "Þetta er síða 1 <br> <a href=/a> Til baka </a>"
    if id == "2":
        return "Þetta er síða 2 <br> <a href=/a> Til baka </a>"
    if id == "3":
        return "Þetta er síða 3 <br> <a href=/a> Til baka </a>"
    else:
        return """<h2> Þessi síða finnst ekki </h2>
    <a href=/> Smelltu hér til að fara á forsíðu </a>"""

@route("/b")
def b():
    return """
    <h2> Verkefni 2 - B liður </h2>
    <h3> Veldu uppáhalds bókstafinn þinn </h3>
    <a href="/sida2?bokstafur=a"> <img src="myndir/a.jpg"> </a>
    <a href="/sida2?bokstafur=b"> <img src="myndir/b.jpg"> </a>
    <a href="/sida2?bokstafur=c"> <img src="myndir/c.jpg"> </a>
    <a href="/"> Forsíða </a>
    """
@route("/sida2")
def page():
    I = request.query.bokstafur
    if I == "a":
        return """<h3> Þú valdir bókstafinn A </h> <br>
         <img src="myndir/a.jpg">
         <a href=/b> Til baka </a>"""
    if I == "b":
        return """<h3> Þú valdir bókstafinn B </h> <br>
         <img src="myndir/b.jpg">
         <a href=/b> Til baka </a>"""
    if I == "c":
        return """<h3> Þú valdir bókstafinn C </h> <br>
         <img src="myndir/c.jpg">
         <a href=/b> Til baka </a>"""

@route('/myndir/<skra>')
def static_skrar(skra):
    return static_file(skra, root='myndir')

@error(404)
def villa(error):
    return """<h2> Þessi síða finnst ekki </h2>
    <a href=/> Smelltu hér til að fara á forsíðu </a>"""



#run(host='localhost', port=8080, reloader=True, debug=True)

bottle.run(host='0.0.0.0', port=argv[1])
