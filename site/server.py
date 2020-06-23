from flask import Flask, request, render_template, redirect, url_for, send_from_directory

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
    return send_from_directory('assets', path)

# /***********************************************************************
# *
# *  $FC Função: home()
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
# *     Existe um arquivo dentro do projeto com o seguinte path /templates/index.html
# *                    
# *  Assertiva de Saída: 
# *		A rota '/' entrega o arquivo index.html montado
# *
# ***********************************************************************/
@app.route("/")
def home():
    return render_template("index.html")

# /***********************************************************************
# *
# *  $FC Função: about()
# *
# *  $ED Descrição da função
# *     Entrega a página de bio do dono do site
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo about.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/about' do site foi chamada
# *    
# *  Verificação:
# *     Existe um arquivo dentro do projeto com o seguinte path /templates/about.html
# *                    
# *  Assertiva de Saída: 
# *		A rota '/about' entrega o arquivo about.html montado
# *
# ***********************************************************************/
@app.route("/about")
def about():
    return render_template("about.html")

# /***********************************************************************
# *
# *  $FC Função: blog()
# *
# *  $ED Descrição da função
# *     Entrega a página do blog do site
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo blog.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/blog' do site foi chamada
# *    
# *  Verificação:
# *     Existe um arquivo dentro do projeto com o seguinte path /templates/blog.html
# *                    
# *  Assertiva de Saída: 
# *		A rota '/blog' entrega o arquivo blog.html montado
# *
# ***********************************************************************/
@app.route("/blog")
def blog():
    return render_template("blog.html")

# /***********************************************************************
# *
# *  $FC Função: contract()
# *
# *  $ED Descrição da função
# *     Entrega a página de contatos do site
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo contact.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/contact' do site foi chamada
# *    
# *  Verificação:
# *     Existe um arquivo dentro do projeto com o seguinte path /templates/contact.html
# *                    
# *  Assertiva de Saída: 
# *		A rota '/contact' entrega o arquivo contact.html montado
# *
# ***********************************************************************/
@app.route("/contact")
def contract():
    return render_template("contact.html")

# /***********************************************************************
# *
# *  $FC Função: elements()
# *
# *  $ED Descrição da função
# *     Entrega a página de serviços do site
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo elements.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/elements' do site foi chamada
# *    
# *  Verificação:
# *     Existe um arquivo dentro do projeto com o seguinte path /templates/elements.html
# *                    
# *  Assertiva de Saída: 
# *		A rota '/elements' entrega o arquivo elements.html montado
# *
# ***********************************************************************/
@app.route("/elements")
def elements():
    return render_template("elements.html")

# /***********************************************************************
# *
# *  $FC Função: services()
# *
# *  $ED Descrição da função
# *     Entrega a página de serviços do site
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo services.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/services' do site foi chamada
# *    
# *  Verificação:
# *     Existe um arquivo dentro do projeto com o seguinte path /templates/services.html
# *                    
# *  Assertiva de Saída: 
# *		A rota '/services' entrega o arquivo index.html montado
# *
# ***********************************************************************/
@app.route("/services")
def services():
    return render_template("services.html")

# /***********************************************************************
# *
# *  $FC Função: singleBlog()
# *
# *  $ED Descrição da função
# *     Entrega a página do post do blog
# *
# *  $EP Parâmetros --
# *						
# *  $FV Valor retornado
# *     Entrega o arquivo single-blog.html com todas as referências montadas 
# *
# *  Assertiva de Entrada: 
# *		A rota '/single-blog' do site foi chamada
# *    
# *  Verificação:
# *     Existe um arquivo dentro do projeto com o seguinte path /templates/single-blog.html
# *                    
# *  Assertiva de Saída: 
# *		A rota '/single-blog' entrega o arquivo single-blog.html montado
# *
# ***********************************************************************/
@app.route("/single-blog")
def singleBlog():
    return render_template("single-blog.html")

if __name__ == "__main__":
    app.run(host= '0.0.0.0')