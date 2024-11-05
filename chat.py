from WPP_Whatsapp import Create
import os 

current_dir = f"{os.getcwd()}/chat"
print(current_dir)
class RenderWhatApp:
    def __init__(self):
        
        self.your_session_name = "4329de6b-8d6e-42b7-b224-93115e174369"
        self.user_data_dir = current_dir
        self.creator = Create(session=self.your_session_name, 
                        user_data_dir=self.user_data_dir,
                        headless=False)

        self.client = self.creator.start()
        # Now scan Whatsapp Qrcode in browser

        # check state of login
        if self.creator.state != 'CONNECTED':
            raise Exception(self.creator.state)


    def sendMessage(self,message,phone_number):
        # Simple message
        result = self.client.sendText(phone_number, message)
        return result


# chat = RenderWhatApp()
# print(chat.sendMessage("hello world","+923090310514"))
