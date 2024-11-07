from flask import Flask,render_template,request,jsonify,url_for,redirect,flash,session,Response
import webview
from tkinter import *
import threading
import webview.menu as wm
import os
import django
from tkinter import messagebox
import tkinter as tk
import time
from chat import RenderWhatApp
import sys
import subprocess
import shutil
import tkinter as tk
from spin_templete.templete import Render



software_id = 1214
software_version = 1.0
software_name = "Hadi-Attendence-Tracking"

static = os.path.abspath("static")
templete = os.path.abspath("templete")


stop_event = threading.Event()

os.environ['image_state'] = "False"
os.environ['is_connected'] = "False"


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weborm.settings")
django.setup()

from weborm.models import Contacts,WhatsappConnect,FirstTime

# Messages to display in sequence

html = Render("templete")







app = Flask(__name__, static_folder=static,template_folder=templete)
app.secret_key = "__secret_key__" 



# StartChat = None


def restart_program():
    print("Restarting program via batch script...")
    # subprocess.Popen("restart.bat", shell=True)
    os.execv(sys.executable, [sys.executable] + sys.argv)
    # sys.exit()



def background():
    RenderWhatApp()
    

    



def messageBox(title,message,option):
        result =""
        root = Tk()
        root.attributes('-topmost', True)
        root.withdraw()

        if option == "ask":
            result = messagebox.askyesno(title, message)

        elif option == 'messagebox':
            result = messagebox.showinfo(title, message)
        
        elif option == 'error':
            result = messagebox.showerror(title, message)

        root.destroy()
        # root.mainloop()
        return result
 


@app.route('/' , methods =["GET", "POST"])
def home():
    global StartChat
    islogin = WhatsappConnect.objects.all().first()
    print(islogin)
    if islogin != None:
        html = render_template('waite_page.html')
        new_window =webview.create_window('Connect', html=html,maximized=False,minimized=False,
                                          min_size=(200,300),on_top=True,confirm_close=True,
                                          height=200,width=300,shadow=True,
                                          text_select=False
                                          )

        StartChat = RenderWhatApp()
        new_window.confirm_close = False
        new_window.destroy()
        
    return render_template('index.html')


@app.route('/save_contact' , methods =["GET", "POST","PATCH"])
def save_contact():
    if request.method == 'POST':
        name = request.form['name'].strip()
        phone_number = request.form['phone_number'].strip()
        company_name = request.form['company_name'].strip()
        email = request.form['email'].strip()
        address = request.form['address'].strip()
        Contacts(name=name,phone_number=phone_number,company_name=company_name,email=email,address=address).save()

    return redirect(request.referrer)


@app.route('/contact' , methods =["GET", "POST"])
def contact():
    all_contact = Contacts.objects.all()
    return render_template('contact.html',all_contact=all_contact)

@app.route('/edit_contact/<id>' , methods =["GET","POST"])
def edit_contact(id):
    if request.method == 'POST':
        
        id = request.form['id'].strip()
        name = request.form['name'].strip()
        phone_number = request.form['phone_number'].strip()
        company_name = request.form['company_name'].strip()
        email = request.form['email'].strip()
        address = request.form['address'].strip()

        print(id)

        update_contact = Contacts.objects.get(id=id)
        update_contact.name = name
        update_contact.phone_number = phone_number
        update_contact.company_name = company_name
        update_contact.email = email
        update_contact.address = address
        update_contact.save()
        
    
    contact = Contacts.objects.get(id=id) 
    return render_template('edit_contact.html',contact=contact)



@app.route('/delete/<id>' , methods =["GET"])
def delete(id):
    result = messageBox("Delete","Are You Sure!","ask")
    print(type(result))
    if result == True:
        Contacts.objects.filter(id=id).delete()
    
    return redirect('/contact')

@app.route('/connect_whats_auto' , methods =["GET"])
def connect_whats_auto():
    is_login = WhatsappConnect.objects.all().first()
    is_first_time = FirstTime.objects.all().first()
    print(is_first_time)
    return render_template('connect_whats_auto.html',
                           is_login=is_login,
                           is_first_time=is_first_time
                           )

@app.route('/logout' , methods =["GET"])
def logout():

    shutil.rmtree(f"{os.getcwd()}/chat")
    WhatsappConnect.objects.all().delete()
    restart_program()
    return redirect('connect_whats_auto')

@app.route('/connect_whatsapp' , methods =["GET"])
def connect_whatsapp():
    
    image_base64 = None
    
    thread = threading.Thread(target=background)
    thread.start()
   
    while True:
        time.sleep(1)
    
        if os.getenv('image_state') == "True":
            image_base64 = os.getenv('base64')
            
            break

    
    html = render_template('connect_whatsapp.html',image_base64=image_base64)
    new_window =webview.create_window('Connect', html=html,maximized=False,minimized=False,min_size=(500,700))
    
    while True:
        time.sleep(1)
        is_connected = os.getenv('is_connected')
        print(is_connected,"is_connected")
        if is_connected == "True":
            WhatsappConnect(is_login=True).save()
            new_window.destroy()
            restart_program()
            break
        else:
            print("no connect")
            
    return jsonify(message="Webview window should open soon")



def file_dialog(window):
    file_types = ('Image Files (*.bmp;*.jpg;*.gif)', 'All files (*.*)')

    result = window.create_file_dialog(
        webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types
    )
    return result


@app.route('/open_file_dialog' , methods =["GET"])
def open_file_dialog():
    image_path = file_dialog(window)
    print(type(image_path))
    if os.name == "posix":
        return jsonify({
            "path":image_path[0]
        })
        
    else:
        return jsonify({
            "path":image_path
        })


    


@app.route('/send_message' , methods =["GET","POST"])
def send_message():
    if request.method == 'POST':
        
        message = request.form['message'].strip()
        image = request.form['image'].strip()
        if image != "":
            print(message)
            print(image)
        print(message,"message")
    print(StartChat.sendMessage("+923090310514","hello world"))
    return render_template('send_message.html')



if __name__ == '__main__':





    webview.settings['ALLOW_DOWNLOADS'] = True
    window = webview.create_window('HAT (Hadi Attendance Tracking)',
                                   app,text_select=True,width=1400, 
                                   height=700,min_size=(1400,700),confirm_close=True
                                   ) # min_size=(1200,700)
    
    webview.start(window,
        debug=False,
                  http_server=True,
                  http_port=9000
                  )