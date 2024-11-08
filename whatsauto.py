from flask import Flask,render_template,request,jsonify,url_for,redirect,flash,session,Response
import webview
from tkinter import *
import threading
import webview.menu as wm
import django
from tkinter import messagebox
import tkinter as tk
import time
from chat import RenderWhatApp
import subprocess
import shutil
import tkinter as tk
import psutil
import sys
import os

DEGUG = False


software_id = 1015
software_version = 1.0
software_name = "WhatsAuto (Take Easy)"




stop_event = threading.Event()

os.environ['image_state'] = "False"
os.environ['is_connected'] = "False"
os.environ['now_login'] = "False"


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weborm.settings")
django.setup()

from weborm.models import Contacts,WhatsappConnect,FirstTime

# Messages to display in sequence


is_first_time = FirstTime.objects.all().first()




def resource_path(relative_path):
    
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS  # Temporary folder created by PyInstaller
    else:
        base_path = os.path.abspath(".")  # Base path when running normally

    return os.path.join(base_path, relative_path)



static = os.path.abspath(resource_path("static"))
templete = os.path.abspath(resource_path("templete"))

app = Flask(__name__, static_folder=static,template_folder=templete)
app.secret_key = "__secret_key__" 






def restart_program():
    os.execv(sys.executable, [sys.executable] + sys.argv)
    



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
    
    now_login = os.getenv('now_login')
    if islogin != None and now_login == "False" and DEGUG == False:
        html = render_template('waite_page.html')
        new_window =webview.create_window('Connect', html=html,resizable=False,
                                          min_size=(200,300),on_top=True,confirm_close=True,
                                          height=200,width=300,shadow=True,
                                          text_select=False
                                          )

        StartChat = RenderWhatApp()
        new_window.confirm_close = False
        new_window.destroy()
        os.environ['now_login'] = "True"
        
    
    return render_template('index.html',islogin=islogin)


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
    
    if result == True:
        Contacts.objects.filter(id=id).delete()
    
    return redirect('/contact')

@app.route('/connect_whats_auto' , methods =["GET"])
def connect_whats_auto():
    is_login = WhatsappConnect.objects.all().first()
    
    
    return render_template('connect_whats_auto.html',
                           is_login=is_login,
                           is_first_time=is_first_time
                           )

# @app.route('/logout' , methods =["GET"])
# def logout():

#     shutil.rmtree(f"{os.getcwd()}/chat")
#     WhatsappConnect.objects.all().delete()
#     restart_program()
#     return redirect('connect_whats_auto')

@app.route('/logout' , methods =["GET"])
def logout():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if proc.info['name'] == "firefox.exe":
                process = psutil.Process(proc.info['pid']) 
                process.terminate() 
                process.wait()
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass  #
    WhatsappConnect.objects.all().delete()
    shutil.rmtree(f"{os.getcwd()}/chat")
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
    new_window =webview.create_window('Connect', html=html,resizable=False,min_size=(500,700))
    
    while True:
        time.sleep(1)
        is_connected = os.getenv('is_connected')
        
        if is_connected == "True":
            WhatsappConnect(is_login=True).save()
            if is_first_time == None:
                FirstTime(is_first_time=True).save()
            new_window.destroy()
            restart_program()
            break
        else:
            pass
            
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
    
    if os.name == "posix":
        return jsonify({
            "path":image_path[0]
        })
        
    else:
        return jsonify({
            "path":image_path
        })


    


# @app.route('/send_message', methods=["GET", "POST"])
# def send_message():
    
#     all_contact = Contacts.objects.all()
#     if request.method == 'POST':
        
#         message = request.form['message'].strip()
#         image_path = request.form.get('image_path',"").strip() 
        
        
#         selected_contacts = request.form.getlist('selected_contacts')
        
        
        
#         if not selected_contacts:
#             messageBox("Error","Contact Not Select","error")
#         else:
#             for id in selected_contacts:
#                 time.sleep(2)
#                 phone_number = all_contact.get(id=id)
#                 if image_path != "":
#                     response = StartChat.sendImage(str(phone_number.phone_number),str(message),str(image_path))
                                   
#                 else:
#                     response = StartChat.sendMessage(str(phone_number.phone_number),str(message))
                    
                                   


    
    
    
#     return render_template('send_message.html', all_contact=all_contact)


@app.route('/send_message', methods=["GET","POST"])
def send_message():
    
    if request.method == 'POST':
        contact_id = request.form.get('contact_id')
        message = request.form.get('message')
        image_path = request.form.get('image_path', "")

        try:
            
            contact = Contacts.objects.get(id=contact_id)
            if not contact:
                return jsonify({"status": "error", "message": "Contact not found"}), 404

            
            if image_path:
                response = StartChat.sendImage(contact.phone_number, message, image_path)
            else:
                response = StartChat.sendMessage(contact.phone_number, message)

            
            if response:
                return jsonify({"status": "success", "message": "Message sent"})
            else:
                return jsonify({"status": "failed", "message": "Message failed to send"})
        except Exception as e:
            print(f"Error sending message: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

    all_contact = Contacts.objects.all()
    return render_template('send_message.html', all_contact=all_contact)




def show_about():
    root = Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    messagebox.showinfo("About", f"{software_name}\n\n"
                        "WhatsAuto automate you WhatsApp Message Take Easy "
                        "Developer:\n"
                        "WhatsAPP - Momin Iqbal : +923058632914 ")
    
    root.destroy()
    root.mainloop()



def on_closed():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            if proc.info['name'] == "firefox.exe":
                process = psutil.Process(proc.info['pid']) 
                process.terminate() 
                process.wait()
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


if __name__ == '__main__':


    menu_items = [
        wm.Menu(
            'About',
            [
                wm.MenuAction('About Developer', show_about),
                
            ],
        ),
    ]



    webview.settings['ALLOW_DOWNLOADS'] = True
    window = webview.create_window(software_name,
                                   app,text_select=True,width=1000, 
                                   height=700,min_size=(1000,700),confirm_close=True
                                   ) # min_size=(1200,700)
    window.events.closed += on_closed
    webview.start(window,
        debug=False,
                  http_server=True,
                  http_port=9000,
                  icon=f"{static}/icon/logo.ico",
                   menu=menu_items,
                  )