# COVID-1india WhatsApp Application

#### COVID-19india-WhatsApp is a Application Which Provides Latest Information of Corona Virus Cases on Your WhatsApp Number
***
## Setup
**STEP 1 :** Send **```join second-previous```** to WhatsApp Number - **``` +14155238886 ```**

<img src="images/join%20second-previous.PNG" height=450>


**STEP 2 :** A simple **```Hey```** Message will Guide you further and you will get a **Welcome message** like below screenshot:

<img src="images/welcome%20message.PNG" height=450> <img src="images/allindiacases.PNG" height=450> <img src="images/most%20affceted%20states.PNG" height=450> <img src="images/getdistrictfromstate.PNG" height=450>

**STEP 3 :** You can choose Any option like :
* ``` 1``` for **Latest Corona Virus Cases of All India**
* ``` 2``` for **To get state code and then Enter the State Code to get State Cases**
* ``` 3``` for **5 most Affected States in India**
* ``` 4``` for **How I Made this bot**
* or Enter the Name of State like ```Maharashtra``` to get most affected districts in **Maharastra**
***
## Source of CORONA-19 cases data
* COVID-19india WhatsApp Application uses the **OPEN SOURCED API** Provided by https://github.com/covid19india to Get the latest data on Corona Virus Cases Data.

* You can Always Cross check Data on https://www.covid19india.org/

* This Website is created by a group of dedicated volunteers who curate and verify the data coming from several sources on Corona Cases and Provide the Lastest Updates and They own all the Data Which this Application provide on Your whatsApp
***

## How This Works
COVID-19india WhatsApp Application uses following things to operate:
* **```  Python  ```**
* **```  Twilio  ```**
* **```  ngrok  ```**

* **Step 1 :** Using Python it collected The data from the from API of **covid19india** using **```requests```** Module
* **Step 2 :** Using **```Flask``` and ```Twilio```** Python Libraries I hosted it on localhost and arranged **'POST','GET'** Methods
* **Step 3 :** using **```ngrok```** to convert my localhost into **```'http' server```**
* **Step 4 :** Added **```'http' server into Twilio```** for sending WhatsApp Messages
***
