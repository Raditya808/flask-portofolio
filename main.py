from flask import Flask,session,url_for

app = Flask(__name__)


@app.route("/")
def index():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>Portofolio</title>
    <link rel="stylesheet" href="{url_for('static', filename='index-rute.css')}">
    </head>
    <body>
    
    <!-- rute ke function project-->
    <button>
        <a href="{url_for('project_route')}">View Projects</a>
    </button>

    <h1>Flask Portofolio</h1>
   <section class="header-container">
  <h2>Hey Visitor! I'm Raditya</h2>
  <div class="content-text">
    <h2>Python Backend Developer</h2>
    <p>
      Expertise in Python
    </p>
  </div>
</section>
<section id="projects" class="project-container container">
  <div class="division"></div>

  <div class="content-text">
    <h2>Skills</h2>
    <div class="scroll-container">
      <table style="text-align: center;">
        <tr>
          <td  style="padding: 20px;">
            <div class="textcard"  style="padding: 20px;">
              <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
              <h4>Python</h4>
            </div>
          </td>
          <td  style="padding: 20px;">
            <div class="textcard"  style="padding: 20px;">
              <img class="github-icon" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Framework/flask.svg"
              alt="Flask" width="50" height="50">
              <h4>Flask</h4>
            </div>
          </td>
          <td  style="padding: 20px;">
            <div class="textcard"  style="padding: 15px;">
              <img src="https://cdn.worldvectorlogo.com/logos/django.svg"
              alt="Django" width="50" height="50">
              <h4>Django</h4>
            </div>
          </td>
          <td  style="padding: 20px;">
            <div class="textcard"  style="padding: 20px;">
              <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/mysqlworkbench.svg"
              alt="MySQL" width="55" height="55">
              <h4>MySQL</h4>
            </div>
          </td>
          <td  style="padding: 20px;">
            <div class="textcard"  style="padding: 20px;">
              <img class="github-icon"  src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Devops/bash.svg"
              alt="bash" width="55" height="55">
              <h4>Bash</h4>
            </div>
          </td>
          <td  style="padding: 20px;">
            <div class="textcard"  style="padding: 20px;">
              <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.svg"
              alt="git" width="55" height="55">
              <h4>Git</h4>
            </div>
          </td>
          <td  style="padding: 20px;">
          </td>
        </tr>
      </table>
    </div>
    <div class="arrow-container">
    </div>
  </div>
</section>
</body>
    </html>
    """
    
    
@app.route("/prjct")
def project_route():
    return f"""


"""

if __name__ == "__main__": 
    app.run(debug=True)