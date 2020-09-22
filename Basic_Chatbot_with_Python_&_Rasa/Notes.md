# Notes

- Start with " rasa init " Command to start the Chatbot Basic Template

- First Train the existing chatbot with "rasa train" and then use  "rasa shell" to start the chatbot

- "/stop" to  exit the "rasa shell"

- "nlu" stands for Natural Language Understanding

- "rasa shell nlu " to get more info(Confidences) regarding the Working of Bot while understanding the sentence typed 

- "Ctrl+ C" to exit "rasa shell nlu" 

### Domain File

- This file defines the entire scope of the Chatbot

- If we add or remove the intents in the "nlu" file we need to change in the "domain.yml" file also.

### Stories File

- It defines the potential Conversational Flow between the User and Chatbot

- We need not define all the possible Conversations.

- Defining the most likely possible Conversations Would be Sufficient

- Each Story will be like "intent" recognised by bot followed by name of "response" it should return for that intent.

- Name of Stories are not important. It is just for our Reference.

### Start with your own bot

- After typing "rasa init" We get a basic template of chatbot. To make our own bot, First change the "nlu", "stories" , domains.yml files to fit the requirements of your bot

- Once We have changed the 3 files , We will now train our nlu Model using "rasa train"

- After training We can talk to bot using "rasa shell"


### Doing a Particular Task asked by User

## Using Entities 

- We need to extract the required data from user input as entities like this:-
- We will modify the examples in the intents like :
    - What is the time zone of [london](city)
    - How .... ..... ... ........ ..... [entity](name_of_entity)

- By above Tagging, We are telling our NLU model that part in the Square Brackets is an entity named "city"

- Also don't forget including city in the entities section in "domains.yml" file

- Dont forget training the model once changes are made before using "rasa shell"


## Using Slots 


- In this chatbot, To find the actual time zone , First we need to store the entity "city" in Chatbots Memory called slots and then write some code in Python .

- Slots are essentially Key-Value Pairs and they are specified in domain.yml file

- In rasa if name of slot value is same as an entity, Then entity value will be updated at "slot" also if we set 
 " auto_fill : True "

- Info present in slots can be used in responses using {}


## Using Actions

To create Custom Actions We need 3 things :

- Update "stories" and "domain" files to include custom actions.

- Create the Custom actions logic in "actions" file.

- Start the action server.

###### The chatboat wil interact with the actions server to trigger custom action logic and get appropriate response

- As usual we create a "actions" section in the "domain" file and include name of action kept in the "stories" file.

- In "actions" file by default a Class will be present in Commented Format. 

- Make sure that action name returned by the "name" function of "Class" in the "actions" file is same as that of action name we used in "domains" and "stories" files

- We can get the data saved in slots by using "tracker.get_slot("slot_name")" 

- We will output text from the action using "dispatcher.utter_message(text="output_message_we_want_to_send")"

- In actual production, To get the required quantities, they use either Databases or API call

- We actually give the logic in the "run function" of Class


- Once the changes are made in "actions" file also, Then we first "rasa train"

- Then we need to run the action server which chatbot uses to communicate with to perform these custom actions.

- So we need to create an endpoint for the action server.

- We can use the default endpoint also which acn be done by uncommenting in "endpoints" file.

- Now we can open other Command Prompt in the same directory and start the action server by "rasa run actions" 

- Finally Now we can type "rasa shell" to run the Chatbot

- More diverse examples we can provide for each intents More better our chatbot will be. 


