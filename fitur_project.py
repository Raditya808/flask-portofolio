from flask import Blueprint,url_for

# membuat app dan menjadikan nya @route() bernama second2
second2 = Blueprint('second', __name__, static_folder='static') # menerima parameter dari file main.py 
# lewat app.register lalu membaut syntax blueprint menerima second 
# sebagai parameter yang nantinya file main.py akan membuat button 
# sehingga second dan function prjct akan di kirim sebagai button

@second2.route('/my-projects') # membuat route second2
def prjct(): # function menu yang di panggil di file button
    return f"""
<!DOCTYPE html>
  <html>
  <head>
  <title>Project</title>
  <style>
    *{{
    text-align:center;
    }}
  </style>
  </head>
  <body>
  <h1 style="text-align:center;">ERROR 404</h1>
  <img src="static/lmao.png" width='800px'">
    <button>
    <!-- ke  rute main.py-->
    <a href="{url_for('afterlog')}">Balik gih</a>

    </button>
    </body>
  </html>
  
  
  
  
  """
