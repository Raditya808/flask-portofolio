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
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>WELCOME SAARRR</title>
        <link rel="icon" href="{url_for('static', filename='Tachyon.jpg')}">
        <style>
           /* ===================================
   90s PROFESSIONAL PORTFOLIO THEME
   Clean · Classic · Timeless
   =================================== */

@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Code+Pro:wght@400;600&display=swap');

:root {{
  --navy:    #1a2744;
  --navy2:   #243356;
  --slate:   #4a5568;
  --cream:   #f5f0e8;
  --cream2:  #ede8de;
  --gold:    #b8972a;
  --gold2:   #d4af37;
  --red:     #8b1a1a;
  --white:   #ffffff;
  --border:  #a09070;
  --shadow:  rgba(26,39,68,0.18);
  --text:    #1a1a2e;
  --muted:   #5a5a6a;
}}

*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}

body {{
  background-color: var(--cream);
  background-image:
    linear-gradient(rgba(180,165,140,0.15) 1px, transparent 1px),
    linear-gradient(90deg, rgba(180,165,140,0.15) 1px, transparent 1px);
  background-size: 40px 40px;
  color: var(--text);
  font-family: 'Libre Baskerville', Georgia, serif;
  font-size: 1rem;
  line-height: 1.7;
  animation: pageFade 0.6s ease both;
}}

@keyframes pageFade {{
  from {{ opacity: 0; }}
  to   {{ opacity: 1; }}
}}

::-webkit-scrollbar {{ width: 8px; }}
::-webkit-scrollbar-track {{ background: var(--cream2); }}
::-webkit-scrollbar-thumb {{ background: var(--navy); }}

h1 {{
  font-family: 'Libre Baskerville', Georgia, serif;
  font-size: 2.6rem;
  font-weight: 700;
  color: var(--navy);
  letter-spacing: 2px;
  text-align: center;
  border-bottom: 3px double var(--gold);
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
  animation: slideDown 0.7s cubic-bezier(0.22,1,0.36,1) both;
}}

h2 {{
  font-family: 'Libre Baskerville', Georgia, serif;
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--navy);
  letter-spacing: 1px;
  border-left: 4px solid var(--gold);
  padding-left: 12px;
  margin: 1.5rem 0 0.8rem;
  animation: slideRight 0.6s cubic-bezier(0.22,1,0.36,1) both;
  animation-delay: 0.1s;
}}

h4 {{
  font-family: 'Source Code Pro', monospace;
  font-size: 0.78rem;
  color: var(--navy);
  text-align: center;
  margin-top: 8px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}}

p {{
  font-size: 0.95rem;
  color: var(--slate);
  line-height: 1.8;
  margin-bottom: 0.6rem;
}}

a {{
  color: var(--red);
  text-decoration: underline;
  text-underline-offset: 3px;
  font-size: inherit;
  transition: color 0.2s, opacity 0.2s;
}}
a:hover {{
  color: var(--gold);
  opacity: 0.85;
}}

@keyframes slideDown {{
  from {{ opacity: 0; transform: translateY(-22px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes slideRight {{
  from {{ opacity: 0; transform: translateX(-18px); }}
  to   {{ opacity: 1; transform: translateX(0); }}
}}
@keyframes slideUp {{
  from {{ opacity: 0; transform: translateY(24px); }}
  to   {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes fadeIn {{
  from {{ opacity: 0; }}
  to   {{ opacity: 1; }}
}}
@keyframes cardPop {{
  from {{ opacity: 0; transform: scale(0.93) translateY(10px); }}
  to   {{ opacity: 1; transform: scale(1) translateY(0); }}
}}

.form_user {{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 5rem 1rem 1rem;
  animation: slideDown 0.7s ease both;
}}

.form-input {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding: 1rem;
  animation: slideUp 0.7s ease both;
  animation-delay: 0.15s;
}}

input[type="text"] {{
  font-family: 'Libre Baskerville', Georgia, serif;
  font-size: 1rem;
  background: var(--white);
  color: var(--text);
  border: 2px solid var(--navy);
  border-top-color: var(--border);
  border-left-color: var(--border);
  padding: 10px 16px;
  outline: none;
  width: 300px;
  transition: border-color 0.2s, box-shadow 0.2s;
  box-shadow: inset 2px 2px 4px rgba(0,0,0,0.08);
}}
input[type="text"]:focus {{
  border-color: var(--gold);
  box-shadow: inset 2px 2px 4px rgba(0,0,0,0.08), 0 0 0 3px rgba(184,151,42,0.15);
}}
input[type="text"]::placeholder {{
  color: var(--muted);
  font-style: italic;
}}

input[type="submit"],
button {{
  font-family: 'Source Code Pro', monospace;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  background: var(--navy);
  color: var(--cream);
  border: 2px solid var(--navy);
  padding: 10px 28px;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.15s;
  box-shadow: 3px 3px 0 var(--gold);
  position: relative;
  overflow: hidden;
}}
input[type="submit"]::after,
button::after {{
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(120deg, transparent 30%, rgba(255,255,255,0.12) 50%, transparent 70%);
  transform: translateX(-100%);
  transition: transform 0.4s;
}}
input[type="submit"]:hover::after,
button:hover::after {{
  transform: translateX(100%);
}}
input[type="submit"]:hover,
button:hover {{
  background: var(--gold);
  color: var(--navy);
  border-color: var(--navy);
  box-shadow: 3px 3px 0 var(--navy);
  transform: translate(-1px, -1px);
}}
input[type="submit"]:active,
button:active {{
  transform: translate(2px, 2px);
  box-shadow: 1px 1px 0 var(--navy);
}}

button a {{
  color: inherit;
  text-decoration: none;
  font-family: 'Source Code Pro', monospace;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}}

.content-wrapper {{
  max-width: 860px;
  margin: 0 auto;
  padding: 2rem 2.5rem;
  animation: fadeIn 0.5s ease both;
}}

.content-wrapper > button {{
  margin: 0 10px 10px 0;
}}

.header-container {{
  background: var(--white);
  border: 1px solid var(--border);
  border-top: 5px solid var(--navy);
  padding: 2.5rem;
  margin: 2rem 0;
  box-shadow: 4px 4px 0 var(--cream2), 5px 5px 0 var(--border);
  animation: slideUp 0.7s cubic-bezier(0.22,1,0.36,1) both;
  animation-delay: 0.1s;
  position: relative;
}}
.header-container::after {{
  content: '';
  display: block;
  height: 3px;
  background: linear-gradient(90deg, var(--gold), var(--navy), var(--gold));
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
}}

.header-container img {{
  border: 3px solid var(--navy);
  outline: 2px solid var(--gold);
  outline-offset: 3px;
  display: block;
  margin: 1.2rem auto;
  transition: outline-color 0.3s, transform 0.3s;
}}
.header-container img:hover {{
  outline-color: var(--red);
  transform: scale(1.02);
}}

.content-text section {{
  border-left: 3px solid var(--cream2);
  padding-left: 14px;
  margin: 10px 0;
  transition: border-color 0.3s;
}}
.content-text section:hover {{
  border-left-color: var(--gold);
}}

.project-container {{
  background: var(--white);
  border: 1px solid var(--border);
  border-top: 5px solid var(--gold);
  padding: 2.5rem;
  margin: 2rem 0;
  box-shadow: 4px 4px 0 var(--cream2), 5px 5px 0 var(--border);
  animation: slideUp 0.7s cubic-bezier(0.22,1,0.36,1) both;
  animation-delay: 0.2s;
}}

.scroll-container {{
  overflow-x: auto;
  padding-bottom: 8px;
}}

table {{
  border-collapse: separate;
  border-spacing: 10px;
}}

.textcard {{
  background: var(--cream);
  border: 1px solid var(--border);
  border-bottom: 3px solid var(--navy);
  padding: 14px 10px;
  text-align: center;
  width: 95px;
  cursor: default;
  transition: all 0.22s cubic-bezier(0.22,1,0.36,1);
  animation: cardPop 0.5s ease both;
}}
.textcard:hover {{
  background: var(--navy);
  border-color: var(--navy);
  border-bottom-color: var(--gold);
  transform: translateY(-5px);
  box-shadow: 0 10px 24px var(--shadow);
}}
.textcard:hover h4 {{
  color: var(--cream);
}}
.textcard img {{
  width: 44px;
  height: 44px;
  object-fit: contain;
  display: block;
  margin: 0 auto;
  transition: transform 0.22s;
}}
.textcard:hover img {{
  transform: scale(1.12);
}}

td:nth-child(1) .textcard {{ animation-delay: 0.05s; }}
td:nth-child(2) .textcard {{ animation-delay: 0.10s; }}
td:nth-child(3) .textcard {{ animation-delay: 0.15s; }}
td:nth-child(4) .textcard {{ animation-delay: 0.20s; }}
td:nth-child(5) .textcard {{ animation-delay: 0.25s; }}
td:nth-child(6) .textcard {{ animation-delay: 0.30s; }}
td:nth-child(7) .textcard {{ animation-delay: 0.35s; }}
td:nth-child(8) .textcard {{ animation-delay: 0.40s; }}
td:nth-child(9) .textcard {{ animation-delay: 0.45s; }}

footer {{
  background: var(--navy);
  border-top: 4px double var(--gold);
  padding: 2.5rem 2rem;
  margin-top: 2.5rem;
  animation: fadeIn 0.8s ease both;
  animation-delay: 0.3s;
}}

.footer-content {{
  max-width: 860px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}}

.footer-content > a {{
  font-family: 'Source Code Pro', monospace;
  font-size: 0.88rem;
  color: var(--gold2);
  text-decoration: none;
  letter-spacing: 0.5px;
  transition: color 0.2s;
}}
.footer-content > a:hover {{
  color: var(--cream);
}}

.social {{
  display: flex;
  gap: 18px;
}}
.social a img {{
  width: 28px;
  height: 28px;
  filter: brightness(0) invert(1);
  opacity: 0.7;
  transition: opacity 0.2s, transform 0.2s;
}}
.social a:hover img {{
  opacity: 1;
  transform: translateY(-3px);
}}

.copyright p {{
  font-family: 'Source Code Pro', monospace;
  font-size: 0.75rem;
  color: rgba(245,240,232,0.45);
  text-align: center;
  letter-spacing: 1px;
}}

@media (max-width: 600px) {{
  h1 {{ font-size: 1.7rem; }}
  h2 {{ font-size: 1.1rem; }}
  .content-wrapper {{ padding: 1rem 1.2rem; }}
  .header-container,
  .project-container {{ padding: 1.5rem 1rem; }}
  input[type="text"] {{ width: 240px; }}
  .textcard {{ width: 78px; padding: 10px 6px; }}
  .textcard img {{ width: 34px; height: 34px; }}
}}
        </style>
    </head>
    <body>
            <div class="form_user">
                <h1>WELCOME</h1>
            </div>
                <div class="form-input">
                    <form method="POST">
                        <input type="text" name="nama" placeholder="Siapa Namamu Tuan?" required>
                        <input type="submit" value="Masuk">
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
            
            <div class="nav-buttons">
                <!-- button untuk ke rute Blurprint('second') di fitur_project dan second adalah function nya-->
                <button><a href="{url_for('second.prjct')}">View Projects</a></button>
            
                <!-- button untuk ke rute Blueprint('kontak') di contactus.py hubungi adalah function nya-->
                <button><a href="{url_for('kontak.hubungi')}">Lets Connect</a></button>

                <!-- button untuk ke ruute index '/' -->
                <button><a href="{url_for("index")}">Go Back To Input?</a></button>
            </div>


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
                    <p>Copyright &copy; 2025 Raditya. All rights reserved</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """
     


if __name__ == "__main__": 
    app.run(debug=True)
