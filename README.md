# Amazon Alexa Skill: Binary and Decimal Converter

## About

In this workshop, we will be creating an Amazon Alexa skill that converts from binary form to decimal form and vice versa.
Additionally, we will incorporating three types of binary forms for the user to choose from:
- Unsigned
- Signed
- Two's Complement

### Goals

This tutorial will teach you the following:
- Create an Amazon Alexa skill
- Work with utterances, intents, and slots
- Understand the architecture of an Alexa skill
- Utilize AWS Lambda
- Understand the various types of binary and how to convert to and from decimal form

## Setup

- Create an Amazon account:
  - Visit https://amazon.com/ and create one, no credit card necessary
- Create an AWS account:
  - Visit https://aws.amazon.com/ to do so
  - This one does require a credit card, but Amazon won't charge you
  - Note: This takes up to 24 hours for the account to activate
  - We will be using AWS Lambda to create the Alexa Skill
- Create an Amazon developer account:
  - Go to https://developer.amazon.com and link it to your Amazon account
- Download and install a text editor
  - I use GitHub's open source text editor, Atom. You can download it at https://atom.io/
  - Other text editors I recommend are Sublime (https://www.sublimetext.com/) or VIM, but an text editor works
- Clone/download this repository
  - This comes with the template that we will be using to create the functions running Alexa, as well as the completed version
  - The sample code included to start our project is referenced from the Alexa 101 workshop (https://wrkshp.github.io/alexa/)
  - Note: We will be writing in Python 3.6

## Adding a new skill

- To begin, navigate to https://developer.amazon.com/
- Click the Alexa tab and select the Alexa Skills Kit at the bottom of the page
- Click Start a Skill in the top right corner
  - You will be prompted to sign in
- Once you've returned to the Alexa Skills Kit page, click on Create Skill
  - Enter a SkillName and click Next
    - This can be anything you want and will be what the skill will be listed as in the skills store
  - Choose a model to add to your skill and click Create Skill
    - For simplicity, we will be selecting the Custom model
- Now that your skills has now been built, we can create the skill's invocation name under the Invocation tab
  - The invocation name is the way the user will begin an interaction with a particular custom skill
    - In other words, this is the name we use when we talk to Alexa
    - I will be naming my invocation ```echoconvert```
- Hit Save Model at the top and select Intents in the left menu

## Adding intents

- An intent is how Alexa handles the request that the user makes to Alexa
- Click Add Intent and for this skill, we will need to create six (6) intents:
  - GetDecimalIntentUnsigned
  - GetDecimalIntentSigned
  - GetDecimalIntentTwosComp
  - GetUnsignedBinaryIntent
  - GetSignedBinaryIntent
  - GetTwosCompBinaryIntent
- For each intent, we can customize its utterances and slots
  - Uterances are how the user would speak to Alexa
  - Slots are the variables that you'd want your user to fill in when making an utterance
- For each intent, we will be adding custom slots:
  - For the get decimal intents, add a custom slot called ```BinaryNumber```
  - For the get binary intents, add a custom slot called ```DecimalNumber```
  - Choose for the two slots, the prebuilt slot type ```AMAZON.SearchQuery```
    - The reason we use search query rather than number for the slot type is that we want the entire number that the user inputs
    - Amazon Alexa cuts off the leading zeros, which is important especially when we convert from binary to decimal, when the slot type is AMAZON.number
- Now that the intents are added, we can define some sample utterances
  - To keep it simple, for the get decimal intents we will be adding the following utterances according to which binary type the intent is:  
  ```What is decimal number {DecimalNumber} in unsigned binary form```  
  ```What is decimal number {DecimalNumber} in signed binary form```  
  ```What is decimal number {DecimalNumber} in two's complement binary form```  
  - and for the get binary intents:  
  ```What is unsigned binary number {BinaryNumber} in decimal form```  
  ```What is signed binary number {BinaryNumber} in decimal form```  
  ```What is two's complement binary number {BinaryNumber} in decimal form```  
  - Feel free to add more than just these. The more you add, the better the UX will be because they will have more options
  - Hit Save Model and then click Build Model
  
## Configuring the skill 
- Now that the interaction model has been built successfully, we will set a web service endpoint to handle skill requests
- Scroll down and click on Endpoint
  - We will be using AWS Lambda for this section, so select that option
- Now navigate to https://aws.amazon.com/ and under the My Account tab, click on AWS Mangagement Console
  - You can now use the search bar to find the Lambda service
- Once you are in the Lambda Mangagement Console, click Create function
  - We will be building our function from scratch
  - Choose a name for your function. I named mine ```echoconvertFunction```
  - Set your runtime to Python 3.6 or whichever you are most comfortable with, but I am coding in Python
  - Under role, you can create a new role from the template(s)
    - Enter a name for your new role. Mine is called ```AlexaSkill```
    - Under policy templates, choose Simple Microservice permissions
  - Click Create function
- Afterwards, go back to the Alexa Skills developer console to retrieve your Skill ID
- Copy and paste your ID into the Alexa Skills Kit trigger and hit save

## Code Rundown
- A template of the code has been included in this repository so open that in any text editor you wish to you use
- Running through the skeleton, there are five (5) main sections:
  - Helpers that build the responses
  - Functions that control how the skill behaves
  - Managing events
  - The main handler
  - Functions used to convert
- Within each section, a quick overview of what each function does:
  - ```build_speechlet_response(title, output, reprompt_text, should_end_session)```: builds the json for the speechlet response
  - ```build_response(session_attributes, speechlet_response)```: builds the json for the actual response
  - ```get_welcome_response()```: returns the build response for what Alexa tells the user when the invoke the skill
  - ```handle_session_end_request()```: returns the build response that ends the skill's session
  - ```get_..._number(intent,session)```: these return the build response to get the type of number that the user wants
  - ```on_launch(launch_request, session)```: this gets the welcome response
  - ```on_intent(intent_request, session)```: this gets the intent's response
  - ```lambda_handler(event, context)```: this handles how lambda acts
  - ```convertToDecimal(n, binType)```: this converts the type of binary number indicated to decimal form
  - ```convertToBinary(n)```: for simplicity, this only converts to signed binary with which we can the manipulate for unsigned and two's complement
  - ```twosComp(n)```: returns the two's complement of a binary number
    - Note: the binary number needs to be in signed for for the function to work properly
    
