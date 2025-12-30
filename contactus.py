from flask import Blueprint, url_for

second3 = Blueprint('kontak',__name__,static_folder='static')


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
<style>
/* ================= RESET ================= */
* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

html, body {{
  width: 100%;
  overflow-x: hidden;
}}

body {{
  font-family: 'Inter', 'Segoe UI', Tahoma, sans-serif;
  background: #ffffff;
  min-height: 100vh;
  color: #333;
  display: flex;
  flex-direction: column;
  animation: pageFade 0.8s ease-in-out;
}}

@keyframes pageFade {{
  from {{ opacity: 0; }}
  to {{ opacity: 1; }}
}}

/* ================= HEADER ================= */
h1 {{
  padding: 28px 20px;
  font-size: 1.4em;
  font-weight: 700;
  animation: slideDown 0.8s ease;
}}

@keyframes slideDown {{
  from {{ transform: translateY(-20px); opacity: 0; }}
  to {{ transform: translateY(0); opacity: 1; }}
}}

/* ================= NAV BUTTON (SYNCED) ================= */
button {{
  position: absolute;
  top: 32px;
  z-index: 1000;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  animation: fadeIn 1s ease-out;
}}

button:first-of-type {{
  right: 160px;
}}

button:nth-of-type(2) {{
  right: 30px;
}}

@keyframes fadeIn {{
  from {{ opacity: 0; }}
  to {{ opacity: 1; }}
}}

button a {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 22px;
  background: #f5f5f5;
  color: #333;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 500;
  font-size: 0.75em;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: relative;
  overflow: hidden;
}}

button a::before {{
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(0, 0, 0, 0.03),
    transparent
  );
  transition: left 0.5s ease;
}}

button a:hover::before {{
  left: 100%;
}}

button a::after {{
  content: '→';
  font-size: 1em;
  transition: transform 0.3s ease;
}}

button a:hover::after {{
  transform: translateX(4px);
}}

button a:hover {{
  background: #fff;
  border-color: #d0d0d0;
  color: #000;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}}

/* ================= CONTENT ================= */
.header-container {{
  text-align: center;
  padding: 60px 20px 40px;
}}

.content-text h2 {{
  font-size: 2.4em;
  font-weight: 700;
  animation: fadeUp 0.9s ease;
}}

@keyframes fadeUp {{
  from {{ transform: translateY(20px); opacity: 0; }}
  to {{ transform: translateY(0); opacity: 1; }}
}}

/* ================= SOCIAL CARDS ================= */
.project-container {{
  flex: 1;
  padding: 20px;
}}

.scroll-container {{
  overflow-x: auto;
}}

table {{
  margin: 0 auto;
}}

td {{
  padding: 16px;
}}

.textcard {{
  background: #ffffff;
  border-radius: 12px;
  padding: 22px;
  border: 1px solid #e0e0e0;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  transition: all 0.35s ease;
  animation: cardFloat 0.7s ease backwards;
}}

td:nth-child(1) .textcard {{ animation-delay: 0.1s; }}
td:nth-child(2) .textcard {{ animation-delay: 0.25s; }}
td:nth-child(3) .textcard {{ animation-delay: 0.4s; }}

@keyframes cardFloat {{
  from {{ transform: translateY(25px); opacity: 0; }}
  to {{ transform: translateY(0); opacity: 1; }}
}}

.textcard:hover {{
  transform: translateY(-6px) scale(1.02);
  box-shadow: 0 10px 25px rgba(0,0,0,0.14);
}}

.textcard img {{
  width: 50px;
  height: 50px;
  margin-bottom: 10px;
  transition: transform 0.3s ease;
}}

.textcard:hover img {{
  transform: scale(1.12);
}}

.textcard h4 {{
  font-size: 1em;
  font-weight: 600;
}}

/* ================= FOOTER ================= */
#footer {{
  background: linear-gradient(135deg, #111111, #000000);
  padding: 25px 0 15px;
  width: 100%;
  margin-top: auto;
}}

#footer .container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 16px;
  text-align: center;
}}

#footer a {{
  color: #b0b0b0;
  font-size: 0.95em;
  text-decoration: none;
  display: inline-block;
  margin-bottom: 12px;
  transition: color 0.3s ease;
}}

#footer a:hover {{
  color: #ffffff;
}}

#footer .social {{
  display: flex;
  justify-content: center;
  gap: 14px;
  margin: 12px 0;
}}

#footer .social a {{
  width: 38px;
  height: 38px;
  background: rgba(255,255,255,0.08);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}}

#footer .social a:hover {{
  transform: translateY(-4px) scale(1.12);
  background: rgba(255,255,255,0.15);
}}

#footer .social img {{
  width: 20px;
  height: 20px;
}}

#footer p {{
  font-size: 0.75em;
  color: #777;
  margin-top: 10px;
}}

/* ================= MOBILE ================= */
@media (max-width: 768px) {{
  button {{
    top: 20px;
  }}

 button:first-of-type {{
  right: 141px;
}}


  button:nth-of-type(2) {{
    right: 20px;
  }}

  button a {{
    padding: 8px 16px;
    font-size: 0.8em;
  }}

  .content-text h2 {{
    font-size: 2em;
  }}

  td {{
    padding: 10px;
  }}
}}
</style>
</head>
<body>
  <!-- Navigation Header -->
  <button><a href="/">Home</a></button>
  <!-- ke rute main.py -->
  
 <button><a href="{url_for('second.prjct')}">View Projects</a></button>
  <!-- ke rute blueprint second di file fitur-project-->

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
