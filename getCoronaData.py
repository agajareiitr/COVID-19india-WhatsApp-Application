import requests
import time
import datetime

# latestdata() this Function collects Information on Overall Cases in India
def latestdata():
    url = "https://api.covid19india.org/data.json"
    data = requests.get(url).json()
    total = data['statewise'][0]
    # increased = data['key_values'][0]
    output = (
        "🔹 This Information is Based on https://www.covid19india.org/ 👇\n"
        f"🔹 Total confirmed cases : *{total['confirmed']}*\n"
        f"🔹 Total active cases : *{total['active']}*\n"
        f"🔹 Total Deaths : *{total['deaths']}*\n"
        f"🔹 Last updated at : *{total['lastupdatedtime']}*")
    return output


# latestStateData() This function collects the Individual Data of State using  State Codes
def latestStateData(code):
    url = "https://api.covid19india.org/data.json"
    data = requests.get(url).json()
    statedata = data['statewise']
    statecodes = [f"{statedata[i]['statecode']}" for i in range(len(statedata))]
    indexofstate = statecodes.index(code)
    statewisedata = statedata[indexofstate]
    output = (
        "🔹 This Information is Based on https://www.covid19india.org/ 👇\n"
        f"🔹 State : *{statewisedata['state']}*\n"
        f"🔹 Total confirmed cases : *{statewisedata['confirmed']}*\n"
        f"🔹 Total active cases : *{statewisedata['active']}*\n"
        f"🔹 Total Deaths : *{statewisedata['deaths']}*\n"
        f"🔹 Last updated at : *{statewisedata['lastupdatedtime']}*")

    return output


# top5states() this function collects the most Affected states in India
def top5states():
    url = "https://api.covid19india.org/data.json"
    data = requests.get(url).json()
    statedata = data['statewise']
    statedatalist = [[i['state'],int(i['confirmed']),i['deaths']] for i in statedata]
    statedatalist=sorted(statedatalist,key=lambda t:t[1],reverse=True)
    output = (
        "🔹 This Information is Based on https://www.covid19india.org/ 👇\n"
        f"🔹 *5* Most Affected States with Confirmed / Deaths : \n"
        f"🔹 *{statedatalist[1][0]}* : *{statedatalist[1][1]}* / *{statedatalist[1][2]}*\n"
        f"🔹 *{statedatalist[2][0]}* : *{statedatalist[2][1]}* / *{statedatalist[2][2]}*\n"
        f"🔹 *{statedatalist[3][0]}* : *{statedatalist[3][1]}* / *{statedatalist[3][2]}*\n"
        f"🔹 *{statedatalist[4][0]}* : *{statedatalist[4][1]}* / *{statedatalist[4][2]}*\n"
        f"🔹 *{statedatalist[5][0]}* : *{statedatalist[5][1]}* / *{statedatalist[5][2]}*")
    return output


# districtwisedata() this function collects the most affected districts data in a Particular state
def districtwisedata(msg):
    url = "https://api.covid19india.org/v2/state_district_wise.json"
    data = requests.get(url).json()
    district_list = [i['state'] for i in data]
    if msg.title() in district_list:
        index_of_state = district_list.index(msg.title())
        x = data[index_of_state]['districtData']  # this is all District data of particular state
        x = [[i['district'], i['confirmed']] for i in x]  # updated x to just all district and its confirmed cases
        x = sorted(x, key=lambda t: t[1], reverse=True)
        output = (
            "🔹 This Information is Based on https://www.covid19india.org/ 👇\n"
            f"🔹 *5* Most Affected Districts in *{msg.title()}* : \n"
            f"🔹 *{x[0][0]}* : *{x[0][1]}*\n"
            f"🔹 *{x[1][0]}* : *{x[1][1]}*\n"
            f"🔹 *{x[2][0]}* : *{x[2][1]}*\n"
            f"🔹 *{x[3][0]}* : *{x[3][1]}*\n"
            f"🔹 *{x[4][0]}* : *{x[4][1]}*")
    # district_in_state = latestStateData(msg.title())
    return output
#this function converts time of latest News Data to simple time
def converttime(seconds):
    if seconds<3600:
        return f"{int(seconds/60)} min ago"
    else:
        return f"{int(seconds/3600)} hour ago"

# latestnews() function gives the latest news of coronacirus cases based on website data
def latestnews():
    url ="https://raw.githubusercontent.com/covid19india/api/master/updatelog/log.json"
    data = requests.get(url).json()
    output = (
                "🔹 This Latest News Data is Based on https://www.covid19india.org/ 👇\n"
                f"🔹 {converttime(int(time.time())-data[-1]['timestamp'])} : {data[-1]['update']}"
                f"🔹 {converttime(int(time.time())-data[-2]['timestamp'])} : {data[-2]['update']}"
                f"🔹 {converttime(int(time.time())-data[-3]['timestamp'])} : {data[-3]['update']}"
                f"🔹 {converttime(int(time.time())-data[-4]['timestamp'])} : {data[-4]['update']}"
                f"🔹 {converttime(int(time.time())-data[-5]['timestamp'])} : {data[-5]['update']}")
    return output