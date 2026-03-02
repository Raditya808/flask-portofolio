from flask import Blueprint, url_for

# membuat app dan menjadikan nya @route() bernama second3 
second3 = Blueprint('kontak',__name__,static_folder='static')
# menerima parameter second3 dari file main.py lewat 
# app.register.blueprint lalu membuat syntax 
# blueprint menerima kontak sebagai parameter 
# yang nantinya file main.py akan membuat button 
# sehingga kontak dan hubungi akan dikirim sebagai button di file main.py 


@second3.route('/contactus')
def hubungi():
      # make format string biar bisa menggunakan package url_for untuk menggunakan blueprint
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>Lets Connect</title>
 <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="{url_for('static',filename='contactus.css')}">
 <link rel="icon" href="{url_for('static',filename='Tachyon.jpg')}">
</head>
<body>

    <div class="nav-container">
      <button><a href="{url_for('afterlog')}">Home</a></button>
       <!-- ke rute main.py -->
  </div>


  <!-- Header Section -->
  <section class="header-container">
    <div class="content-text">
      <h2>Contact Me</h2>
    </div>
  </section>

  <!-- Social Media Cards Section -->
  <section id="projects" class="project-container container">
    <div class="scroll-container">
      <table style="text-align: center;">
        <tr>
          <td style="padding: 20px;">
            <div class="textcard" style="padding: 20px;">
              <a href="https://github.com/Raditya808" target="_blank">
                <img alt="Github" width="55" height="55"
                     src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg"
                     style="border-radius: 0px; filter: invert(1);">
              </a>
              <h4>GitHub</h4>
            </div>
          </td>
          <td style="padding: 20px;">
            <div class="textcard" style="padding: 20px;">
              <a href="https://www.instagram.com/4ku_raditya/" target="_blank">
                <img alt="Instagram" width="55" height="55"
                     src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg"
                     style="border-radius: 0px;">
              </a>
              <h4>Instagram</h4>
            </div>
          </td>
          <td style="padding: 20px;">
            <div class="textcard" style="padding: 20px;">
              <a href="https://www.facebook.com/yourprofile" target="_blank">
                <img alt="Facebook" width="55" height="55"
                     src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg"
                     style="border-radius: 0px;">
              </a>
              <h4>Facebook</h4>
            </div>
          </td>
        </tr>
      </table>
    </div>
  </section>

  <!-- Footer -->
  <footer id="footer">
    <div class="container">
      <a href="mailto:mraditradit808@gmail.com">mraditradit808@gmail.com</a>
        
      <!-- Social links -->
      <div class="social">
        <a href="https://github.com/Raditya808" target="_blank">
          <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" 
               alt="Github"
               style="border-radius: 0px;">
        </a>
        <a href="https://www.instagram.com/4ku_raditya/" target="_blank">
          <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" 
               alt="Instagram"
               style="border-radius: 0px;">
        </a>
        <a href="https://www.facebook.com/yourprofile" target="_blank">
          <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" 
               alt="Facebook"
               style="border-radius: 0px;">
        </a>
      </div>
        
      <!-- Copyright -->
      <p>Copyright © 2025 Raditya. All rights reserved</p>
    </div>
  </footer>
</body>
</html>

"""
