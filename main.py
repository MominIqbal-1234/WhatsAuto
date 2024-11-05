
from chat import RenderWhatApp
import webview
from flask import Flask,render_template,request,jsonify,url_for,redirect,flash,session,Response
import os


chat = RenderWhatApp()

res = chat.sendMessage("hello world","+923090310514")
print(res)




static = os.path.abspath("static")
templete = os.path.abspath("templete")

app = Flask(__name__, static_folder=static,template_folder=templete)
app.secret_key = "__secret_key__" 

@app.route('/' , methods =["GET", "POST"])
def login():
    window.minimize()
    try:
        return render_template("idex.html")
    except:
        return render_template('404.html')



if __name__ == '__main__':
    window = webview.create_window('WhatsAuto',
                                   app,text_select=True,width=1400, 
                                   height=700,min_size=(1400,700),
                                   focus=True) # min_size=(1200,700)
    
    webview.start(window,
        debug=False,
        http_server=True,
        http_port=9000,
        icon='./static/icon/logo.png'
                  )