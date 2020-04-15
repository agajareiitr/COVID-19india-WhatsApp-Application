from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import getCoronaData

app = Flask(__name__)
stateslist = ['Kerala', 'Delhi', 'Telangana', 'Rajasthan', 'Haryana', 'Uttar Pradesh', 'Ladakh', 'Tamil Nadu',
              'Jammu and Kashmir', 'Karnataka', 'Maharashtra', 'Punjab', 'Andhra Pradesh', 'Uttarakhand', 'Odisha',
              'Puducherry', 'West Bengal', 'Chandigarh', 'Chhattisgarh', 'Gujarat', 'Himachal Pradesh',
              'Madhya Pradesh', 'Bihar', 'Manipur', 'Mizoram', 'Goa', 'Andaman and Nicobar Islands', 'Jharkhand',
              'Assam', 'Arunachal Pradesh', 'Dadra and Nagar Haveli', 'Tripura']
workmessage = "Hey welcome I am\n*Deva ~ Akash Gajare*\n\nI made this using following things :\n*1.* Python\n*2.* Twilio\n*3.* ngrok\n\nStep 1: Using Python I collected The data from the Website\nStep 2 : Using Flask and Twilio python Libraries I hosted it on localhost and arranged 'POST','GET' methods\nStep 3 : using ngrok i converted my localhost into 'http' server\nStep 4 :Added 'http' server into Twilio for sending WhatsApp Messages\n\nFor Further Information checkout my Github :\nhttps://github.com/agajareiitr/COVID-19india-WhatsApp-Application"
intromessage = "Hey I am *Deva*\nHere to give you updates on Corona Virus cases\n\nPlease choose from the following 👇\n*1.* Latest Corona Virus Updates\n*2.* Individual State Data\n*3. 5* Most Afffected States\n*4.* Latest News on Corona virus cases\n*5.* How I Made this bot\n*6.* Share this Bot with a Link\n\n*New update* 😁 : Type your State Name to get most Afffected districts in your State\n\nRemember the Data is taken from https://www.covid19india.org/\n\nShare this to all your friends and Family\n*NOTE :* send '*join second-previous*' to +14155238886 number to Join\nThis step is necessary as this script is on free hosting\nThanks for understanding"
intro = ['hi', 'Hi', 'Hii', 'hii', 'hello', 'Hello', 'Hola', 'corona', 'Corona', 'updates', 'hey', 'Hey']
stateintro = "Send The State Code to Get Individual State Data 👇\nMH-Maharashtra\nTN-Tamil Nadu\nDL-Delhi\nTG-Telangana\nRJ-Rajasthan\nKL-Kerala\nUP-Uttar Pradesh\nAP-Andhra Pradesh\nMP-Madhya Pradesh\nKA-Karnataka\nGJ-Gujarat\nHR-Haryana\nJK-Jammu and Kashmir\nPB-Punjab\nWB-West Bengal\nOR-Odisha\nBR-Biha\nUT-Uttarakhand\nAS-Assam\nCH-Chandigarh\nHP-Himachal Pradesh\nLA-Ladakh\nAN-Andaman and Nicobar Islands\nCT-Chhattisgarh\nGA-Goa\nPY-Puducherry\nJH-Jharkhand\nMN-Manipur\nMZ-Mizoram\nAR-Arunachal Pradesh\nDN-Dadra and Nagar Haveli\nTR-TripuranDD-Daman and Diu\nLD-Lakshadweep\nML-Meghalaya\nNL-Nagaland\nSK-Sikkim"
share_message="🔹Want Coronavirus Case updates then click on this link\nhttps://wa.me/14155238886?text=join%20second-previous\nand send it to get latest updates any time you want, also there’s more to discover\n\n🔹All the Data is coming through\nhttps://www.covid19india.org/\nand is most updated and accurate\n\n🔹Send this to Your family ,friends and other WhatsApp Groups 🙏🙏"

@app.route("/")
def hello():
    return "hello world"


@app.route("/sms", methods=['GET', 'POST', 'DELETE'])
def sms_reply():
    msg = request.form.get('Body')
    user = request.form.get('From')
    with open('user_names.txt','r') as f:
        data = f.read()
        if user in data:
            print(f"{user} sent: {msg}")
        else:
            with open('user_names.txt','a') as file:
                file.write(f"\n{user}")
                print(f"New User :- {user} added and sent: {msg}")
    if msg.title() in stateslist:
        resp = MessagingResponse()
        resp.message(getCoronaData.districtwisedata(msg))
    elif msg == '1':
        resp = MessagingResponse()
        resp.message(getCoronaData.latestdata())
    elif msg == '2':
        resp = MessagingResponse()
        resp.message(stateintro)
    elif msg == '3':
        resp = MessagingResponse()
        resp.message(getCoronaData.top5states())
    elif msg == '4':
        resp = MessagingResponse()
        resp.message(getCoronaData.latestnews())    
    elif msg == '5':
        resp = MessagingResponse()
        resp.message(workmessage)
    elif msg == '6':
        resp = MessagingResponse()
        resp.message(share_message)
    elif msg.isupper():
        resp = MessagingResponse()
        resp.message(getCoronaData.latestStateData(msg))
    elif msg:
        resp = MessagingResponse()
        resp.message(intromessage)
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
