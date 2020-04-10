import requests
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
	statecodes=[f"{statedata[i]['statecode']}" for i in range(len(statedata))]
	indexofstate = statecodes.index(code)
	statewisedata=statedata[indexofstate]
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
	output = (
	    "🔹 This Information is Based on https://www.covid19india.org/ 👇\n"
	    f"🔹 *5* Most Affected States with *Confirmed / Deaths* : \n"
	    f"🔹 *{statedata[1]['state']}*  : *{statedata[1]['confirmed']}* / *{statedata[1]['deaths']}*\n"
	    f"🔹 *{statedata[2]['state']}*  : *{statedata[2]['confirmed']}* / *{statedata[2]['deaths']}*\n"
	    f"🔹 *{statedata[3]['state']}*  : *{statedata[3]['confirmed']}* / *{statedata[3]['deaths']}*\n"
	    f"🔹 *{statedata[4]['state']}*  : *{statedata[4]['confirmed']}* / *{statedata[4]['deaths']}*\n"
	    f"🔹 *{statedata[5]['state']}*  : *{statedata[5]['confirmed']}* / *{statedata[5]['deaths']}*")
	return output

# districtwisedata() this function collects the most affected districts data in a Particular state
def districtwisedata(msg):
	url = "https://api.covid19india.org/v2/state_district_wise.json"
	data = requests.get(url).json()
	district_list=[i['state'] for i in data]
	if msg.title() in district_list:
		index_of_state = district_list.index(msg.title())
		x = data[index_of_state]['districtData'] # this is all District data of particular state
		x = [[i['district'],i['confirmed']] for i in x] #updated x to just all district and its confirmed cases
		x = sorted(x,key=lambda t:t[1],reverse=True)
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
