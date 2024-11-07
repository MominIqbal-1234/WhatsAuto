from WPP_Whatsapp import Create
import os 
import json
from engine import read,write




def catchQR(qrCode: str, asciiQR: str, attempt: int, urlCode: str):
    os.environ['base64'] = str(qrCode)
    os.environ['image_state'] = "True"
    
    print("Saving QR code image from base64 data...")

current_dir = f"{os.getcwd()}/chat"
print(current_dir)
class RenderWhatApp:
    def __init__(self):
        self.state = None
        self.your_session_name = "4329de6b-8d6e-42b7-b224-93115e174369"
        self.user_data_dir = current_dir
        self.creator = Create(session=self.your_session_name, browser="firefox",
                        user_data_dir=self.user_data_dir,
                        headless=True,
                        catchQR=catchQR,
                        logQR=True
                        )
        
        self.client = self.creator.start()
        
        # Now scan Whatsapp Qrcode in browser

        # check state of login
        
        print(type(self.creator.state),"....Conted......")
        if self.creator.state != 'CONNECTED':
            raise Exception(self.creator.state)
        print("after connect")
        os.environ['is_connected'] = "True"


    def sendMessage(self,phone_number,message):
        # Simple message
        result = self.client.sendText(phone_number, message)
        return result

    def getContacts(self):
        result = self.client.getAllContacts()
        with open('contact.json','w') as file:
            file.write(str(json.dumps(result,indent=2)))
        print(".....")

    def getMessage(self,phone_number):
        messages = self.client.getMessages(phone_number)
        # print(messages)
        with open('message.json','w') as file:
            file.write(str(json.dumps(messages,indent=2)))
        print(".....")
   

    def sendImage(self,phone_number,message,image_path):
        result = self.client.sendImage(phone_number, filePath=image_path, caption=message)
        return result

    def sendGif(self,phone_number,image_path):
        result = self.client.sendGif(phone_number, image_path)
        return result
        

# chat = RenderWhatApp()
# print(chat.getContacts())
# print(chat.sendMessage("+923090310514","hello world"))
# print(chat.getMessage("+923090310514"))
# print(chat.sendImage("+923060149015","auto image send","/home/momin/Desktop/download.jpeg"))
# print(chat.sendGif("+923060149015","/home/momin/Downloads/file_example_MP4_480_1_5MG.mp4"))
