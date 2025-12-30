from flask import Flask,session,url_for
from fitur_project import second2
from contactus import second3

app = Flask(__name__)
app.register_blueprint(second2)
app.register_blueprint(second3)

@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portofolio</title>
    <link rel="stylesheet" href="{url_for('static', filename='index-rute.css')}">
    </head>
    <body>
    <br>
    <!-- Navigation Buttons -->
    <button>
        <a href="{url_for('second.prjct')}">View Projects</a>
    </button>
    
    <button>
        <a href="{url_for('kontak.hubungi')}">Lets Connect</a>
    </button>
    
    
    <!-- Header Section -->
    <section class="header-container">
        <h2>Hey Visitor! I'm Raditya</h2>
        <div class="content-text">
            <h2>Python Backend Developer</h2>
            <p>
                Iam Doing Coding And Prompting 
                And Iam Love Making Backend With Python Lenguage
            </p>  
        </div>
    </section>
    
    <!-- Skills Section -->
    <section id="projects" class="project-container">
    <h2 align="center">Skills</h2>
            <div class="scroll-container">
                <table style="text-align: center;">    
                    <tr> 
                        <!-- Python icon -->
                        <td>
                            <div class="textcard">
                                <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="Python">
                                <h4>Python</h4>
                            </div>
                        </td>
                        
                        <!-- HTML icon -->
                        <td>
                            <div class="textcard">
                                <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" alt="HTML">
                                <h4>Html</h4>
                            </div>
                        </td>
                        
                        <!-- Flask icon -->
                        <td>
                            <div class="textcard">
                                <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Framework/flask.svg" alt="Flask">
                                <h4>Flask</h4>
                            </div>
                        </td>
                        
                        <!-- JavaScript icon -->
                        <td>
                            <div class="textcard">
                                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript">
                                <h4>JavaScript</h4>
                            </div>
                        </td>
                        
                        <!-- MySQL icon -->
                        <td>
                            <div class="textcard">
                                <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/mysqlworkbench.svg" alt="MySQL">
                                <h4>MySQL</h4>
                            </div>
                        </td>
                        
                        <!-- Bash icon -->
                        <td>
                            <div class="textcard">
                                <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Devops/bash.svg" alt="Bash">
                                <h4>Bash</h4>
                            </div>
                        </td>
                        
                        <!-- Git icon -->
                        <td>
                            <div class="textcard">
                                <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.svg" alt="Git">
                                <h4>Git</h4>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>
    </section>

    <!-- Footer -->
    <footer id="footer">
        <div class="footer-content">
            <a href="mailto:mraditradit808@gmail.com">mraditradit808@gmail.com</a>
            
            <!-- Social links -->
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
            
            <!-- Copyright -->
            <p>Copyright © 2025 Raditya. All rights reserved</p>
        </div>
    </footer>
    
    </body>
    </html>
    """

if __name__ == "__main__": 
    app.run(debug=True)