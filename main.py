#################################################################
from flask import Flask,session,url_for
from fitur_project import second2 # mengirim file fitur_project sebagai parameter second2 yang dibuat app.register dibawah
from contactus import second3 # ini juga
#################################################################



################################################################
app = Flask(__name__)
app.register_blueprint(second2) #mengirim blueprint ke rute second2 di file fitur_project.py   
app.register_blueprint(second3) #memgirim blueprint ke rute second3 di file contactus.py 
################################################################
 

@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Portofolio</title>
        <link rel="stylesheet" href="{url_for('static', filename='index-rute.css')}">
    </head>
    <body>
    <script src="static/welcome.js"></script>
       
        
        <div class="content-wrapper">
            <br>
            <!-- button untuk ke rute fitur_project.py-->
            <button>
                <a href="{url_for('second.prjct')}">View Projects</a>
            </button>
            
            <!-- button untuk ke rute contactus.py-->
            <button>
                <a href="{url_for('kontak.hubungi')}">Lets Connect</a>
            </button>
            
            <section class="header-container">
                <h2>Hey Visitor! I'm Raditya</h2>
                 <img src="static/Raditya.jpeg" height="200px">
                <div class="content-text">
                    <h2>Python Backend Developer</h2>
                    <p>
                        Iam Learning Coding And The same time i learn prompting and i love making back end with Python lenguage 
And i learn Html JavaScript And Python Lenguage
                    </p>  
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
