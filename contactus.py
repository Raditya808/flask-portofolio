from flask import Blueprint

second3 = Blueprint('kontak',__name__,static_folder='static')

@second3.route('/contactus')
def hubungi():
    return """ 
<!DOCTYPE html>
<html>
<head>
<title></title>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', 'Segoe UI', Tahoma, sans-serif;
  background: #ffffff;
  min-height: 100vh;
  color: #333;
  position: relative;
  display: flex;
  flex-direction: column;
}

/* Main Title */
h1 {
  text-align: left;
  padding: 30px 20px 10px 40px;
  font-size: 1.5em;
  font-weight: 700;
  color: #000;
  animation: fadeInDown 0.8s ease-out;
}

@keyframes fadeInDown {
  from {
    opacity: 0;
    transform: translateY(-20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Navigation Buttons */
button {
  position: absolute;
  top: 30px;
  z-index: 1000;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  animation: fadeIn 1s ease-out;
}

button:first-of-type {
  right: 160px;
}

button:nth-of-type(2) {
  right: 30px;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

button a {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 22px;
  background: #f5f5f5;
  color: #333;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 500;
  font-size: 0.85em;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  position: relative;
  overflow: hidden;
}

button a::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(0, 0, 0, 0.03), transparent);
  transition: left 0.5s ease;
}

button a:hover::before {
  left: 100%;
}

button a::after {
  content: '→';
  font-size: 1em;
  transition: transform 0.3s ease;
}

button a:hover::after {
  transform: translateX(4px);
}

button a:hover {
  background: #fff;
  border-color: #d0d0d0;
  color: #000;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transform: translateY(-2px);
}

/* Header Container */
.header-container {
  text-align: center;
  padding: 50px 20px 70px;
  max-width: 700px;
  margin: 0 auto;
  animation: fadeInUp 1s ease-out;
}

@keyframes fadeInUp {
  from { 
    opacity: 0; 
    transform: translateY(20px);
  }
  to { 
    opacity: 1; 
    transform: translateY(0);
  }
}

.header-container h2 {
  font-size: 1.8em;
  margin-bottom: 20px;
  font-weight: 400;
  padding: 0;
  color: #666;
}

.content-text h2 {
  font-size: 2.5em;
  margin-bottom: 15px;
  font-weight: 700;
  color: #000;
  animation: slideIn 1s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.content-text p {
  font-size: 1.1em;
  color: #666;
  line-height: 1.6;
}

/* Project Container */
.project-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 30px 20px 50px;
  flex: 1;
}

.division {
  height: 1px;
  background: linear-gradient(90deg, transparent, #e0e0e0, transparent);
  margin: 20px auto 30px;
  max-width: 80%;
}

.project-container .content-text h2 {
  text-align: center;
  font-size: 2.5em;
  margin-bottom: 50px;
  font-weight: 700;
  color: #000;
}

/* Scroll Container */
.scroll-container {
  overflow-x: auto;
  padding: 20px 0;
  scrollbar-width: thin;
  scrollbar-color: #d0d0d0 #f5f5f5;
}

.scroll-container::-webkit-scrollbar {
  height: 8px;
}

.scroll-container::-webkit-scrollbar-track {
  background: #f5f5f5;
  border-radius: 10px;
}

.scroll-container::-webkit-scrollbar-thumb {
  background: #d0d0d0;
  border-radius: 10px;
}

.scroll-container::-webkit-scrollbar-thumb:hover {
  background: #b0b0b0;
}

/* Table */
table {
  margin: 0 auto;
  border-collapse: separate;
  border-spacing: 0;
}

td {
  padding: 15px !important;
}

/* Text Card */
.textcard {
  background: #ffffff;
  border-radius: 12px;
  padding: 25px 20px !important;
  min-width: 110px;
  transition: all 0.3s ease;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  text-align: center;
  animation: floatIn 0.6s ease-out backwards;
}

/* Staggered Animation */
td:nth-child(1) .textcard { animation-delay: 0.1s; }
td:nth-child(2) .textcard { animation-delay: 0.2s; }
td:nth-child(3) .textcard { animation-delay: 0.3s; }
td:nth-child(4) .textcard { animation-delay: 0.4s; }
td:nth-child(5) .textcard { animation-delay: 0.5s; }
td:nth-child(6) .textcard { animation-delay: 0.6s; }

@keyframes floatIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.textcard:hover {
  transform: translateY(-6px);
  background: #fafafa;
  border-color: #d0d0d0;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12);
}

.textcard img {
  width: 50px;
  height: 50px;
  margin: 0 auto 12px;
  display: block;
  transition: all 0.3s ease;
}

.textcard:hover img {
  transform: scale(1.08);
}

.textcard h4 {
  margin-top: 0;
  font-size: 1em;
  font-weight: 600;
  color: #333;
}

/* Responsive Design */
@media (max-width: 768px) {
  h1 {
    font-size: 1.3em;
    padding: 25px 20px 10px 20px;
  }
  
  button {
    top: 20px;
  }
  
  button:first-of-type {
    right: 140px;
  }
  
  button:nth-of-type(2) {
    right: 20px;
  }
  
  button a {
    padding: 8px 16px;
    font-size: 0.8em;
  }
  
  .header-container {
    padding: 40px 20px 60px;
  }
  
  .header-container h2 {
    font-size: 1.5em;
  }
  
  .content-text h2 {
    font-size: 2em;
  }
  
  .content-text p {
    font-size: 1em;
  }
  
  .project-container .content-text h2 {
    font-size: 2em;
    margin-bottom: 40px;
  }
  
  .textcard {
    min-width: 100px;
    padding: 20px 15px !important;
  }
  
  .textcard img {
    width: 45px;
    height: 45px;
  }
  
  td {
    padding: 10px !important;
  }
}

.arrow-container {
  text-align: center;
  margin-top: 40px;
}

/* Footer - TINGGI SUDAH DIPENDEKKAN */
#footer {
  background: linear-gradient(135deg, #1a1a1a 0%, #000000 100%);
  margin-top: auto;
  padding: 35px 0 20px;
  position: relative;
  width: 100%;
}

#footer::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
}

#footer .container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  text-align: center;
}

#footer h3 {
  font-size: 1.8em;
  margin-bottom: 15px;
  font-weight: 700;
  color: #fff;
  animation: fadeIn 1s ease-out;
}

#footer .contact-info {
  margin: 12px 0;
}

#footer a {
  font-size: 1rem;
  color: #b0b0b0;
  transition: all 0.3s ease;
  display: inline-block;
}

#footer a:hover {
  color: #fff;
  transform: translateY(-2px);
}

#footer .social {
  margin: 20px 0 15px;
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

#footer .social a {
  width: 45px;
  height: 45px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50%;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 1px solid rgba(255, 255, 255, 0.1);
  position: relative;
  overflow: hidden;
}

#footer .social a::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle, rgba(255, 255, 255, 0.1), transparent);
  opacity: 0;
  transition: opacity 0.3s ease;
}

#footer .social a:hover::before {
  opacity: 1;
}

#footer .social a:hover {
  transform: translateY(-5px) scale(1.1);
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.3);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
}

#footer .social img {
  width: 22px;
  height: 22px;
  filter: brightness(0.8);
  transition: filter 0.3s ease;
}

#footer .social a:hover img {
  filter: brightness(1.2);
}

#footer .divider {
  width: 60%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  margin: 30px 0;
}

#footer p {
  font-size: 0.85rem;
  color: #808080;
  margin-top: 8px;
}

#footer .copyright {
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
  width: 100%;
}

@media (max-width: 768px) {
  #footer {
    padding: 30px 0 18px;
  }
  
  #footer h3 {
    font-size: 1.5em;
  }
  
  #footer .social {
    gap: 15px;
  }
  
  #footer .social a {
    width: 40px;
    height: 40px;
  }
  
  #footer .social img {
    width: 20px;
    height: 20px;
  }
}
</style>
</head>
<body>
<section id="projects" class="project-container container">
    <div class="content-text">
        <h2>Connect With Me</h2>
        <div class="scroll-container">
            <table style="text-align: center;">
                <tr>
                    <!-- GitHub -->
                    <td style="padding: 20px;">
                        <div class="textcard" style="padding: 20px;">
                            <a href="https://github.com/Raditya808" target="_blank">
                                <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" 
                                     alt="Github" width="55" height="55" 
                                     style="border-radius: 0px; filter: invert(1);">
                            </a>
                            <h4>GitHub</h4>
                        </div>
                    </td>
                    
                    <!-- Instagram -->
                    <td style="padding: 20px;">
                        <div class="textcard" style="padding: 20px;">
                            <a href="https://www.instagram.com/4ku_raditya/" target="_blank">
                                <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" 
                                     alt="Instagram" width="55" height="55"
                                     style="border-radius: 0px;">
                            </a>
                            <h4>Instagram</h4>
                        </div>
                    </td>
                    
                    <!-- Facebook -->
                    <td style="padding: 20px;">
                        <div class="textcard" style="padding: 20px;">
                            <a href="https://www.facebook.com/yourprofile" target="_blank">
                                <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" 
                                     alt="Facebook" width="55" height="55"
                                     style="border-radius: 0px;">
                            </a>
                            <h4>Facebook</h4>
                        </div>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</section>

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
        
        <!-- Attribution -->
        <p>Copyright © 2025 Raditya. All rights reserved</p>
    </div>
</footer>
</body>
</html>

"""