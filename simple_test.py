from WPP_Whatsapp import Create

# start client with your session name
your_session_name = "test"
creator = Create(session=your_session_name)
client = creator.start()
# Now scan Whatsapp Qrcode in browser

# check state of login
if creator.state != 'CONNECTED':
    raise Exception(creator.state)

phone_number = "+923090310514"  # or "+*********"
message = "hello from wpp"

# Simple message
result = client.sendText(phone_number, message)