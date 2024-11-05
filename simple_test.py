from WPP_Whatsapp import Create
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


current_dir = f"{os.getcwd()}/chat"
print(current_dir)
# start client with your session name
your_session_name = "4329de6b-8d6e-42b7-b224-93115e174369"
user_data_dir = current_dir
creator = Create(session=your_session_name, 
                user_data_dir=user_data_dir,
                headless=False)

client = creator.start()
# Now scan Whatsapp Qrcode in browser

# check state of login
if creator.state != 'CONNECTED':
    raise Exception(creator.state)


def new_message(message):
    print(message,".............")
    global client
    # Add your Code here
    if message and not message.get("isGroupMsg"):
        chat_id = message.get("from")
        message_id = message.get("id")
        print(message.get("body"),"...././././././")
        if "hi" in message.get("body"):
            client.reply(chat_id, "auto وعليكم السلام", message_id)
        else:
            client.reply(chat_id, "Welcome", message_id)



# creator.client.ThreadsafeBrowser.page_evaluate_sync("""
#  // Resolvenndo bug 'TypeError: i.Wid.isStatusV3 is not a function'
#     if(!WPP.whatsapp.Wid.isStatusV3) {
#       WPP.whatsapp.Wid.isStatusV3 = () => false
#     }
# """)

# Add Listen To New Message
creator.client.onMessage(new_message)
creator.loop.run_forever()