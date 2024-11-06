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



stop_event = threading.Event()
render_whatApp = None
os.environ['image_state'] = "False"
os.environ['is_connected'] = "False"


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weborm.settings")
django.setup()

from weborm.models import Contacts

software_id = 1214
software_version = 1.0
software_name = "Hadi-Attendence-Tracking"




DEBUG = True


static = os.path.abspath("static")
templete = os.path.abspath("templete")



app = Flask(__name__, static_folder=static,template_folder=templete)
app.secret_key = "__secret_key__" 


def restart_program():
    if DEBUG == True:
        print("Restarting program...")
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        print("Restarting program via batch script...")
        subprocess.Popen("restart.bat", shell=True)
        sys.exit()



def background():
    global render_whatApp
    render_whatApp = RenderWhatApp()
    

    



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
    # task_thread = threading.Thread(target=background_task).start()
    return render_template('connect_whats_auto.html')

@app.route('/connect_whatsapp' , methods =["GET"])
def connect_whatsapp():
    print("start connect //////////")
    image_base64 = None
    
    thread = threading.Thread(target=background)
    thread.start()
    # render_whatApp = RenderWhatApp()
    # print(render_whatApp.state,"chat.creator")
    
    while True:
        time.sleep(1)
    
        if os.getenv('image_state') == "True":
            # stop_event.set()  
            # thread.join() 
            image_base64 = os.getenv('base64')
            
            break

    print(render_whatApp,"........")
    html = render_template('connect_whats_auto.html',image_base64=image_base64)
    new_window =webview.create_window('View In and Out Time', html=html, width=500, height=700,maximized=False,minimized=False,min_size=(500,700))
    
    is_connected = os.getenv('is_connected')
    while True:
        print(is_connected,"is_connected")
        if is_connected:
            new_window.destroy()
            restart_program()
            break
            
    return jsonify(message="Webview window should open soon")

if __name__ == '__main__':
    webview.settings['ALLOW_DOWNLOADS'] = True
    window = webview.create_window('HAT (Hadi Attendance Tracking)',
                                   app,text_select=True,width=1400, 
                                   height=700,min_size=(1400,700),
                                   ) # min_size=(1200,700)
    
    webview.start(window,
        debug=False,
                  http_server=True,
                  http_port=9000
                  )