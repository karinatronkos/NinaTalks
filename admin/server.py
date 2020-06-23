import os

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from os import listdir
from os.path import isfile, join

app = Flask(__name__, static_url_path='')
# /***********************************************************************
# *
# *  $FC Função: send_js()
# *
# *  $ED Descrição da função
# *     Entrega as páginas de dados estáticos do site
# *
# *  $EP Parâmetros 
# *	    path --> String
# *						
# *  $FV Valor retornado
# *     Arquivo armazendo dentro do diretório /assets
# *
# *  Assertiva de Entrada: 
# *		A rota '/assets' do site foi chamada
# *    
# *  Verificação:
# *     Existe um arquivo dentro do projeto com o seguinte path /assets/<path>
# *                    
# *  Assertiva de Saída: 
# *		A rota '/assets' entrega o arquivo que corresponde ao <path> existente dentro de /assests
# *
# ***********************************************************************/
@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('/assets', path)

# /***********************************************************************
# *
# *  $FC Função: posts()
# *
# *  $ED Descrição da função
# *     Entrega as páginas de blogs do site
# *
# *  $EP Parâmetros 
# *	    path --> String
# *						
# *  $FV Valor retornado
# *     Arquivo armazendo dentro do diretório /post
# *
# *  Assertiva de Entrada: 
# *		A rota '/post' do site foi chamada
# *    
# *  Verificação:
# *     Existe um arquivo dentro do projeto com o seguinte path /opt/<path>
# *                    
# *  Assertiva de Saída: 
# *		A rota '/post' entrega o arquivo que corresponde ao <path> existente dentro de /post
# *
# ***********************************************************************/
@app.route('/post/<path:path>')
def posts(path):
    return send_from_directory(os.environ['STATIC_PATH'], path)

# /***********************************************************************
# *
# *  $FC Função: login()
# *
# *  $ED Descrição da função
# *     Entrega a página de início do site
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo index.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/' do site foi chamada
# *    
# *  Verificação:
# *     - Existe um arquivo dentro do projeto com o seguinte path /templates/index.html
# *     - Em caso method de Post, existe uma rota para o /home
# *             
# *  Assertiva de Saída: 
# *		A rota '/' entrega o arquivo index.html montado e após o login ele redireciona para o /home
# *
# ***********************************************************************/
@app.route("/", methods=['GET','POST'])
def login():
    if request.method == "POST":
        return redirect(url_for('home'))
    return render_template("login.html")

# /***********************************************************************
# *
# *  $FC Função: home()
# *
# *  $ED Descrição da função
# *     Entrega a página de gerencia de posts
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo index.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/home' do site foi chamada
# *    
# *  Verificação:
# *     - Existe um arquivo dentro do projeto com o seguinte path /templates/index.html
# *     - Em caso method de Post, existe uma rota para o '/home'
# *             
# *  Assertiva de Saída: 
# *		A rota '/home' entrega o arquivo index.html montado e após o login ele redireciona para o '/home'
# *
# ***********************************************************************/
@app.route("/home", methods=['GET','POST'])
def home():
    if request.method == "POST":
        rota = request.form["action"]
        if rota == "New Post":
            return redirect(url_for('editor'))
        rota_post = request.form["file_link"]
        return redirect(rota_post)
    onlyfiles = [f for f in listdir(os.environ['STATIC_PATH']) if isfile(join(os.environ['STATIC_PATH'], f))]
    thislist = []
    for f in onlyfiles:
        internal_dic = {
            "name": f,
            "file_link": "/post/"+f
        }
        thislist.append(internal_dic)
    print(thislist, flush=True)
    return render_template("home.html", archive=thislist)

# /***********************************************************************
# *
# *  $FC Função: editor()
# *
# *  $ED Descrição da função
# *     Entrega a página de edição de posts
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo editor.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/editor' do site foi chamada
# *    
# *  Verificação:
# *     - Existe um arquivo dentro do projeto com o seguinte path /templates/index.html
# *     - Em caso method de Post, existe uma rota para o /home
# *             
# *  Assertiva de Saída: 
# *		A rota '/' entrega o arquivo editor.html montado e após a criação do post redireciona para o /home
# *
# ***********************************************************************/
@app.route("/editor", methods=['GET','POST'])
def editor():
    if request.method == "POST":
        title = request.form['post_title']
        text = request.form['post_text']

        new_data = "<!doctype html><html class='no-js' lang='zxx'><head> <meta charset='utf-8'> <meta http-equiv='x-ua-compatible' \
                    content='ie=edge'> <title>SEO HTML-5 Template </title> <meta name='description' content=''> <meta name='viewport' content='width=device-width, \
                    initial-scale=1'> <!-- <link rel='manifest' href='site.webmanifest'> --> <link rel='shortcut icon' type='image/x-icon' href='/assets/img/favicon.ico'> \
                    <!-- Place favicon.ico in the root directory --> <!-- CSS here --> <link rel='stylesheet' href='/assets/css/bootstrap.min.css'> <link rel='stylesheet' \
                    href='/assets/css/owl.carousel.min.css'> <link rel='stylesheet' href='/assets/css/slicknav.css'> <link rel='stylesheet' href='/assets/css/animate.min.css'> \
                    <link rel='stylesheet' href='/assets/css/magnific-popup.css'> <link rel='stylesheet' href='/assets/css/fontawesome-all.min.css'> <link rel='stylesheet' \
                    href='/assets/css/themify-icons.css'> <link rel='stylesheet' href='/assets/css/slick.css'> <link rel='stylesheet' href='/assets/css/nice-select.css'> \
                    <link rel='stylesheet' href='/assets/css/style.css'> <link rel='stylesheet' href='/assets/css/responsive.css'></head><body> <!-- Preloader Start --> \
                    <div id='preloader-active'> <div class='preloader d-flex align-items-center justify-content-center'> <div class='preloader-inner position-relative'> \
                    <div class='preloader-circle'></div> <div class='preloader-img pere-text'> <img src='/assets/img/logo/logo.png' alt=''> </div> </div> </div> </div> \
                    <!-- Preloader Start--> <header> <!-- Header Start --> <div class='header-area header-transparrent '> <div class='main-header header-sticky'> \
                    <div class='container'> <div class='row align-items-center'> <!-- Logo --> <div class='col-xl-2 col-lg-2 col-md-1'> <div class='logo'> \
                    <a href='/'><img src='/assets/img/logo/logo.png' alt=''></a> </div> </div> <div class='col-xl-8 col-lg-8 col-md-8'> <!-- Main-menu --> \
                    <div class='main-menu f-right d-none d-lg-block'> <nav> <ul id='navigation'> <li><a href='/'> Home</a></li> <li><a href='/about'>About Us</a></li> \
                    <li><a href='/services'>Services</a></li> <li><a href='/contact'>Contact</a></li> <li><a href='/blog'>Blog</a> <ul class='submenu'> \
                    <li><a href='/blog'>Blog</a></li> <li><a href='/single-blog'>Blog Details</a></li> </ul> </li> <li><a href='#'>Pages</a> \
                    <ul class='submenu'> <li><a href='/elements'>Element</a></li> </ul> </li> </ul> </nav> </div> </div> <div class='col-xl-2 col-lg-2 col-md-3'> \
                    <div class='header-right-btn f-right d-none d-lg-block'> <a href='#' class='btn header-btn'>Contact Us</a> </div> </div> <!-- Mobile Menu --> \
                    <div class='col-12'> <div class='mobile_menu d-block d-lg-none'></div> </div> </div> </div> </div> </div> <!-- Header End --> </header> \
                    <!-- Slider Area Start--> <div class='services-area'> <div class='container'> <!-- Section-tittle --> \
                    <div class='row d-flex justify-content-center'> <div class='col-lg-8'> <div class='section-tittle text-center mb-80'> \
                    <span>Nina Talks</span> <h2>My Blog​</h2> </div> </div> </div> </div> </div> <!-- Slider Area End--> <!--================Blog Area =================--> \
                    <section class='blog_area single-post-area section-padding'> <div class='container'> <div class='row'> <div class='col-lg-8 posts-list'> \
                    <div class='single-post'> <div class='feature-img'> <img class='img-fluid' src='/assets/img/blog/single_blog_1.png' alt=''> </div> \
                    <div class='blog_details'> <h2>{}</h2> <ul class='blog-info-link mt-3 mb-4'> <li><a href='#'><i class='fa fa-user'></i> UX, Technology</a></li> \
                    </ul> <p class='excert'>{}</p> </div> </div> <div class='navigation-top'> <div class='d-sm-flex justify-content-between text-center'> <p class='like-info'> \
                    <span class='align-middle'><i class='fa fa-heart'></i></span> Lily and 4 people like this</p> <div class='col-sm-4 text-center my-2 my-sm-0'> <!-- <p class='comment-count'><span class='align-middle'> \
                    <i class='fa fa-comment'></i></span> 06 Comments</p> --> </div> <ul class='social-icons'> <li><a href='#'><i class='fab fa-facebook-f'></i></a></li> <li><a href='#'><i class='fab fa-twitter'></i></a> \
                    </li> <li><a href='#'><i class='fab fa-instagram'></i></a></li> </ul> </div> </div> <div class='blog-author'> <div class='media align-items-center'> <img src='/assets/img/blog/author.png' alt=''> \
                    <div class='media-body'> <a href='#'> <h4>Harvard milan</h4> </a> <p>Second divided from form fish beast made. Every of seas all gathered use saying you're, he our dominion twon Second divided from</p> \
                    </div> </div> </div> </div> <div class='col-lg-4'> <div class='blog_right_sidebar'> <aside class='single_sidebar_widget search_widget'> <form action='#'> <div class='form-group'> <div class='input-group mb-3'> \
                    <input type='text' class='form-control' placeholder='Search Keyword' onfocus='this.placeholder = ''' onblur='this.placeholder = 'Search Keyword''> <div class='input-group-append'> <button class='btns' type='button'> \
                    <i class='ti-search'></i></button> </div> </div> </div> <button class='button rounded-0 primary-bg text-white w-100 btn_1 boxed-btn' type='submit'>Search</button> </form> </aside> </div> </div> </div> </div> \
                    </section> <!--================ Blog Area end =================--> <footer> <!-- Footer Start--> <div class='footer-main' data-background='/assets/img/shape/footer_bg.png'> <div class='footer-area footer-padding'> \
                    <div class='container'> <div class='row d-flex justify-content-between'> <div class='col-lg-3 col-md-4 col-sm-8'> <div class='single-footer-caption mb-50'> <div class='single-footer-caption mb-30'> <!-- logo --> \
                    <div class='footer-logo'> <a href='/'><img src='/assets/img/logo/logo2_footer.png' alt=''></a> </div> <div class='footer-tittle'> <div class='footer-pera'> <p class='info1'>221B Baker Street, P.O Box 353 Park <br> Road, USA - 215431</p> \
                    <p class='info2'>info@yourdomain.com</p> </div> </div> <div class='footer-social'> <a href='#'><i class='fab fa-facebook-f'></i></a> <a href='#'><i class='fab fa-twitter'></i></a> <a href='#'><i class='fas fa-globe'></i></a> <a href='#'><i class='fab fa-behance'> \
                    </i></a> </div> </div> </div> </div> <div class='col-lg-2 col-md-4 col-sm-5'> <div class='single-footer-caption mb-50'> <div class='footer-tittle'> <h4>Quick Links</h4> <ul> <li><a href='/about'>About</a></li> <li><a href='/single-blog'>Pricing</a></li> <li><a href='/blog'>Blog</a></li> \
                    <li><a href='/contact'>Contact</a></li> </ul> </div> </div> </div> <div class='col-lg-2 col-md-4 col-sm-7'> <div class='single-footer-caption mb-50'> <div class='footer-tittle'> <h4>Support</h4> <ul> <li><a href='#'>Privacy Policy</a></li> \
                    <li><a href='#'>Terms & Conditions</a></li> <li><a href='#'> Sitemap</a></li> <li><a href='#'>FAQs</a></li> <li><a href='#'>Report a bugb</a></li> </ul> </div> </div> </div> <div class='col-lg-3 col-md-4 col-sm-5'> \
                    <div class='single-footer-caption mb-50'> <div class='footer-tittle'> <h4>Core Features</h4> <ul> <li><a href='#'>Email Marketing</a></li> <li><a href='#'> Offline SEO</a></li> <li><a href='#'>Social Media Marketing</a></li> \
                    <li><a href='#'>Lead Generation</a></li> <li><a href='#'> 24/7 Support</a></li> </ul> </div> </div> </div> </div> </div> </div> <!-- footer-bottom aera --> <div class='footer-bottom-area footer-bg'> <div class='container'> \
                    <div class='footer-border'> <div class='row d-flex align-items-center'> <div class='col-xl-12 '> <div class='footer-copy-right text-center'> <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --> Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class='ti-heart' aria-hidden='true'></i> by <a href='https://colorlib.com' target='_blank'>Colorlib</a> \
                    <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p> </div> </div> </div> </div> </div> </div> </div> <!-- Footer End--> </footer> <!-- JS here --><!-- All JS Custom Plugins Link Here here --> \
                    <script src='/assets/js/vendor/modernizr-3.5.0.min.js'></script><!-- Jquery, Popper, Bootstrap --><script src='/assets/js/vendor/jquery-1.12.4.min.js'></script> <script src='/assets/js/popper.min.js'></script> <script src='/assets/js/bootstrap.min.js'></script> \
                    <!-- Jquery Mobile Menu --> <script src='/assets/js/jquery.slicknav.min.js'></script><!-- Jquery Slick , Owl-Carousel Plugins --> <script src='/assets/js/owl.carousel.min.js'></script> <script src='/assets/js/slick.min.js'></script> \
                    <!-- Date Picker --> <script src='/assets/js/gijgo.min.js'></script><!-- One Page, Animated-HeadLin --> <script src='/assets/js/wow.min.js'></script><script src='/assets/js/animated.headline.js'></script> <script src='/assets/js/jquery.magnific-popup.js'> \
                    </script><!-- Scrollup, nice-select, sticky --> <script src='/assets/js/jquery.scrollUp.min.js'></script> <script src='/assets/js/jquery.nice-select.min.js'></script><script src='/assets/js/jquery.sticky.js'></script> <!-- contact js --> \
                    <script src='/assets/js/contact.js'></script> <script src='/assets/js/jquery.form.js'></script> <script src='/assets/js/jquery.validate.min.js'></script> <script src='/assets/js/mail-script.js'></script> <script src='/assets/js/jquery.ajaxchimp.min.js'></script> \
                    <!-- Jquery Plugins, main Jquery --> <script src='/assets/js/plugins.js'></script> <script src='/assets/js/main.js'></script> </body></html>".format(title, text)
        
        file_title = title.lower().replace(" ","_") + ".html"

        f = open(os.environ['STATIC_PATH']+file_title, 'w')
        f.write(new_data)
        f.close()
        print("teste", flush=True)
        return redirect(url_for('home'))
    return render_template("editor.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0')