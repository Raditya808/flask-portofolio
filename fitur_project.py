from flask import Blueprint

second2 = Blueprint('second', __name__, static_folder='static') # membuat blueprint di untuk di panggil ke main.py

@second2.route('/my-projects') # membuat route second2
def prjct(): # function menu yang di panggil di file button
    return """<!DOCTYPE html>
  <html>
  <head>
  <title>Project</title>
  <style>
  
  </style>
  </head>
  <h1>BESOK AJA MALAS GW</h1>
  <img src="static/lmao.png" width='800px'">
  </html>
  
  
  
  
  """