#################################################################
from flask import Flask, redirect, request,session,url_for
from fitur_project import second2 # menerima parameter second2 dan second3 yang dikirim lewat app,register daru file fitur_project.py dan contactus.py
from contactus import second3 # ini juga
#################################################################



################################################################
app = Flask(__name__)
app.register_blueprint(second2) # menerima variabel second2 dari file dari fitur_project.py   
app.register_blueprint(second3) # menerima variabel second3 dari file dari contactus.py
################################################################

################################################################ 
# secret key to launch the session syntax 
# idk what is this key for this is just my portofolio website dawg
app.secret_key = 'lmaonigga123'
################################################################

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # parameter package hasil username dan form name uuntuuk nama 
        session['username'] = request.form['nama']
        return redirect(url_for('afterlog'))
    return f"""
    <!DOCTYPE html>
        <html>
            <head>
                <title>
                    WELCOME SAARRR
                </title>
                 <link rel="icon" href="{url_for('static',filename='Tachyon.jpg')}">
                <style>
             * {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

body {{
  font-family: 'Inter', sans-serif;
  background: #0d0d0d;
  color: #f5f5f5;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.form_user {{
  text-align: center;
  animation: fadeIn 0.6s ease-out;
}}

h1 {{
  font-size: 3rem;
  font-weight: 300;
  letter-spacing: 0.1em;
  margin-bottom: 2rem;
}}

input[type="text"] {{
  width: 100%;
  max-width: 300px;
  padding: 12px 16px;
  background: #1a1a1a;
  border: 1px solid #333;
  color: #f5f5f5;
  font-size: 1rem;
  margin-bottom: 1rem;
  transition: border-color 0.3s;
}}

input[type="text"]:focus {{
  outline: none;
  border-color: #f5f5f5;
}}

input[type="text"]::placeholder {{
  color: #666;
}}

input[type="submit"] {{
  width: 100%;
  max-width: 300px;
  padding: 12px 24px;
  background: transparent;
  border: 1px solid #333;
  color: #f5f5f5;
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.3s;
}}

input[type="submit"]:hover {{
  background: #f5f5f5;
  color: #0d0d0d;
}}

@keyframes fadeIn {{
  from {{
    opacity: 0;
    transform: translateY(10px);
  }}
  to {{
    opacity: 1;
    transform: translateY(0);
  }}
}}

                </style>
            </head>
            <body>
                <div class="form_user">
                <form method="POST">
                    <input type="text" name="nama" placeholder="Siapa Namamu Tuan?"><br>
                    <input type="submit" value="Kirim">
                </form>
                </div>
            </body>
        </html>
    """

@app.route('/afterlog')
def afterlog():
        return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portofolio</title>
        <link rel="stylesheet" href="{url_for('static', filename='index-rute.css')}">
        <link rel="icon" href="{url_for('static',filename='Tachyon.jpg')}">
    </head>
    <body>
    <script src="static/welcome.js"></script>
       
        
        <div class="content-wrapper">
            <br>
            <!-- button untuk ke rute Blurprint('second') di fitur_project dan second adalah function nya-->
            <button>
                <a href="{url_for('second.prjct')}">View Projects</a>
            </button>
            
            <!-- button untuk ke rute Blueprint('kontak') di contactus.py hubungi adalah function nya-->
            <button>
                <a href="{url_for('kontak.hubungi')}">Lets Connect</a>
            </button>

            <!-- button untuk ke ruute index '/' -->
            <button>
            <a href="{url_for("index")}">Go Back To Input?</a>
            </button>
            
            <section class="header-container">
                <h2>Hey {session['username']}! I'm Raditya</h2>
                 <img src="static/Raditya.jpeg" height="200px">
                <div class="content-text">
                    <h2>Python Backend Developer</h2>
                    
                    <section>
                    <p>This Web Is Created By Flask Framework</p>
                    </section>
                    
                    <section>
                    <p>Information About Flask U Can Check On Websites 
                    <a href="https://flask.palletsprojects.com/en/stable/">"Flask Doc"</a>
                    </p>
                    </section>
                    
                    <section>
                    <p>
                        Iam Just Loving What Iam Making With My Programming Lenguage
                        Especially Iam Love Making Backend With Python
                        For Now Iam Learning
                        Python, Javascript, Html, Git, Sql, Flask
                    </p>  
                    </section>
                </div>
            </section>
            
            <section id="projects" class="project-container">
                <h2 style="text-align: center;">Skills</h2>
                <div class="scroll-container">
                    <table>    
                        <tr> 

                            <td>
                                <div class="textcard">
                                    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python">
                                    <h4>Python</h4>
                                </div>
                            </td>

                            <td>
                                <div class="textcard">
                                    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" alt="HTML">
                                    <h4>Html</h4>
                                </div>
                            </td>


                            <td>
                                <div class="textcard">
                                    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Framework/flask.svg" alt="Flask">
                                    <h4>Flask</h4>
                                </div>
                            </td>


                            <td>
                                <div class="textcard">
                                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript">
                                    <h4>JavaScript</h4>
                                </div>
                            </td>


                            <td>
                                <div class="textcard">
                                    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/mysqlworkbench.svg" alt="MySQL">
                                    <h4>MySQL</h4>
                                </div>
                            </td>


                            <td>
                                <div class="textcard">
                                    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Devops/bash.svg" alt="Bash">
                                    <h4>Bash</h4>
                                </div>
                            </td>


                            <td>
                                <div class="textcard">
                                    <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.svg" alt="Git">
                                    <h4>Git</h4>
                                </div>
                            </td>


                            <td>
                            <div class="textcard">
                          <img 
  src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/lazyvim.svg"
  alt="LazyVim Logo"
  width="80"
  style="filter: invert(1);"
/>
                            <h4>Lazy vim</h4>
                            </div>
                            </td>


                    <td>
                    <div class="textcard">
                    <img src="https://logo.svgcdn.com/logos/lua.svg" 
     alt="Lua Logo" width="80">
                    <h4>Lua</h4>
                    </div>    
                        </td>


                        </tr>
                    </table>
                </div>
            </section>
        </div> 


        <footer id="footer">
            <div class="footer-content">
                <a href="mailto:mraditradit808@gmail.com">mraditradit808@gmail.com</a>
                <div class="social">
                    <a href="https://github.com/Raditya808" target="_blank">
                        <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Github">
                    </a>
                    <a href="https://www.instagram.com/4ku_raditya/" target="_blank">
                        <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram">
                    </a>
                    <a href="https://www.facebook.com/yourprofile" target="_blank">
                        <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook">
                    </a>
                </div>
                <div class="copyright">
                    <p>Copyright © 2025 Raditya. All rights reserved</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """
     


if __name__ == "__main__": 
    app.run(debug=True)
