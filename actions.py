from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction 
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.events import AllSlotsReset
import smtplib
import pandas
import requests
import json
import datetime 


class HealthForm(FormAction):

    def name(self):
        return "health_form"

    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot("fever") == True:
            return ["fever", "respiration"]
        else:
            return ["respiration"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "fever": [
                self.from_entity(entity="fever"),
                self.from_intent(intent=["affirm"], value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],

            "respiration": [
                self.from_entity(entity="respiration"),
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ]
        }





class ActionCoronaLocationTracker(Action):

    def name(self) -> Text:
        return "action_corona_location_tracker"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        response = requests.get("https://api.covid19india.org/data.json").json()
         
        entities = tracker.latest_message['entities']
        state = None
        for e in entities :
            if e['entity'] == "location" :
                state = e['value']
        
        message = "Please enter correct state name !"
        for data in response["statewise"]:
            if data["state"] == state.title():
                # print(data)
                message = "No of Active Cases :- " + data["active"] + "\n" + "No of Confirmed Cases :-  " + data["confirmed"] + "\n" + "No of Recovered Cases :-  " + data["recovered"] + "\n" + "No of Death Cases :-  " + data["deaths"] + "\n" + "The above details are latest updated on :-  " + data["lastupdatedtime"]
        

        


        dispatcher.utter_message(text= message )
        return []





class ActionCoronaTodaysStata(Action):

    def name(self) -> Text:
        return "action_todays_stats"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        response = requests.get("https://api.covid19india.org/data.json").json()
        

        current_time = datetime.datetime.now()  

        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']

        result = ""

        result += str(current_time.day-1)
        result +=" "
        result += months[current_time.month - 1]
        result +=" "

        message = "Something went Wrong"
        for data in response["cases_time_series"]:
            if data["date"] == result:
                message = "Here are Yesterday's Covid-19 Updates of India !" + "\n"+ "No of Confirmed Cases :-  " + data["dailyconfirmed"] + "\n" + "No of Recovered Cases :-  " + data["dailyrecovered"] + "\n" + "No of Death Cases :-  " + data["dailydeceased"] 
        

        dispatcher.utter_message(text= message )
        return []