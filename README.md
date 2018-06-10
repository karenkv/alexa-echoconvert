# Amazon Alexa Skill: Binary and Decimal Converter

### Video Tutorial  

[![Video Tutorial](https://img.youtube.com/vi/1yA2gIhINfE/0.jpg)](https://www.youtube.com/watch?v=1yA2gIhINfE "Amazon Alexa Tutorial: Binary-Decimal Converter")  
https://www.youtube.com/watch?v=1yA2gIhINfE

## About

In this tutorial, we will be creating an Amazon Alexa skill that converts from binary form to decimal form and vice versa.
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
    - Note: You are welcome to add to the welcome response to let Alexa give the user templates of what to ask her.
  - ```handle_session_end_request()```: returns the build response that ends the skill's session
  - ```get_..._number(intent,session)```: these return the build response to get the type of number that the user wants
  - ```on_launch(launch_request, session)```: this gets the welcome response
  - ```on_intent(intent_request, session)```: this gets the intent's response
  - ```lambda_handler(event, context)```: this handles how lambda acts
  - ```convertToDecimal(n, binType)```: this converts the type of binary number indicated to decimal form
  - ```convertToBinary(n)```: for simplicity, this only converts to signed binary with which we can the manipulate for unsigned and two's complement
  - ```twosComp(n)```: returns the two's complement of a binary number
    - Note: the binary number needs to be in signed for for the function to work properly
- Now actually working on the code, first there are a few things we will be adding at the top:
  - Where it says ```BINARY_NUMBER```, you want to set that equal to ``` 'BinaryNumber' ``` or whatever you named your slot for binary number input
  - And where it says ```DECIMAL_NUMBER```, you want to set that equal to ``` 'DecimalNumber' ``` or whatever you named your slot for decimal number input
- Moving onto coding the converter functions, I want to put a disclaimer that there are built-in ways to convert to and from binary in python, but for educational purposes, we will be doing these conversions ourselves.
- For the conversion to decimal form, the function takes in a string named ```n```, which is the binary number taken from the intent request, and another string named ```binType```, which is the binary number's type
  - To convert from binary to decimal, starting from the far right and with base 0, you want to add to your sum 2 to that base times the value in that place
    - For example, the binary number 1011 = 1 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 = 1 + 2 + 8 = 11
  - Coding-wise, first you want to convert the binary number to a list and store it in a variable named "temp" so we can iterate through it later:  
    ```python
    temp = list(n)
    ```  
  - Next, you will have a string named "sign" that's default to "+" and check if the binType is signed or twos  
    ```python 
    sign = "+"
    ```  
    -  If it is signed, the first value of the binary number will indicate if it is positive or negative.
      - If the value at index 0 of the temporary list we created is a 1 and if it is, change the sign to "-". Otherwise, leave it as "+".
      - Then you want you want to strip the list of its first value.  
    ```python
    if binType == "signed":
        if(temp[0] == "1"):
            sign = "-"
        temp = temp[1:]
    ```
    - If it is a two's complement number, you want to again check if the value at index 0 is 1 and if it is, two's complement it and set the sign to "-"  
    ```python
    if binType == "twos":
        if(temp[0] == "1"):
            t = twosComp(n)
            temp = list(t)
            sign = "-"
    ```  
  - Now you want to create to to variables "d" and "base" and set them equal to 0
    - d is what we will be using to store our sum and base keeps track of what exponent we are on
  ```python
  d = 0
  base = 0
  ```  
  - Iterating through the temporary list we created earlier in reverse, you want to add to d 2 to the base times the value i in temp and then increment the base by one
  ```python
  for i in reversed(temp):
        d += 2**base * int(i)
        base += 1
  ```
  - Now you want to check again the binary type and only return the sign if it is signed or a two's complement. If it is unsigned, you can return d as is.
  ```python
  if binType == "signed" or binType == "twos":
        return sign + str(d)
    return str(d)
    ```
  - Altogether, your function should look as follows:
  ```python
  def convertToDecimal(n, binType):
    temp = list(n)
    sign = "+"
    if binType == "signed":
        if(temp[0] == "1"):
            sign = "-"
        temp = temp[1:]
    if binType == "twos":
        if(temp[0] == "1"):
            t = twosComp(n)
            temp = list(t)
            sign = "-"
    d = 0
    base = 0
    for i in reversed(temp):
        d += 2**base * int(i)
        base += 1
    if binType == "signed" or binType == "twos":
        return sign + str(d)
    return str(d)
    ```
- Working on converting to signed binary now, the function takes in one variable, n, which is the decimal number to be converted.
  - To convert from decimal to binary, you want to continuously find the largest base 2 number, keeping track if your remainder is divisible by 2 and if it is, keep a 1 in its place at that base.
  - To do so in code, if your number is less than 0, return 1 + the -n conversion, stripping the first index
  - If it's 0, simply return 0
  - If it's neither negative nor 0, recursively floor divide your n by 2 and add the modulus by two
  - Your function should look like this, following the steps above:
  ```python
  def convertToBinary(n):
    if n < 0:
        return '1' + convertToBinary(-n)[1:]
    elif n == 0:
        return '0'
    else:
        return convertToBinary(n//2) + str(n%2)
  ```
- The final function is the two's complement, which takes in a binary number in string form
  - To two's complement a number, you want to change all the 1's to 0's and vice versa and then binary add a 1.
  - To do this, we first change the string n to a list and store it in temp and then iterate through temp and change these values from 0 to 1 or 1 to 0  
  ```python
  temp = list(n)
    for i in range(len(temp)):
        if temp[i] == "1":
            temp[i] = "0"
        else:
            temp[i] = "1"
  ```
  - Next, we have a carry variable set to 1 and a "twos" variable set to an empty string. You then reverse temp to iterate through it backwards.  
  ```python
  carry = 1
    twos = ""
    temp.reverse()
    ```
  - Iterating through the list, you want to add a string 0 to twos if the carry is 1 and the value in temp is 1 or if they are both 0. If not, you add a 1 and only change the carry to 0 if the carry is originally 1 and the value is 0.  
  ```python
  for j in temp:
        if carry == 1 and j == "1":
            twos += "0"
        elif carry == 1 and j == "0":
            twos += "1"
            carry = 0
        elif carry == 0 and j == "1":
            twos += "1"
        elif carry == 0 and j == "0":
            twos += "0"
            ```
  - Afterwards, you return twos reversed.  
  ```python
  return twos[::-1]
  ```
  - Putting this together, your final function looks as follows:  
  ```python
  def twosComp(n):
    temp = list(n)
    for i in range(len(temp)):
        if temp[i] == "1":
            temp[i] = "0"
        else:
            temp[i] = "1"
    carry = 1
    twos = ""
    temp.reverse()
    for j in temp:
        if carry == 1 and j == "1":
            twos += "0"
        elif carry == 1 and j == "0":
            twos += "1"
            carry = 0
        elif carry == 0 and j == "1":
            twos += "1"
        elif carry == 0 and j == "0":
            twos += "0"
    return twos[::-1]
- Now that we have created our converter functions, we can work on creating the functions to handle our skill's behavior.
  - First off, the intent should look something like this:
  ```json
    intent: {
      ...
      'slots': {
        'BinaryNumber': {
          'name': 'BinaryNumber',
          'value': '-15'
          }
        }
      }
  ```
  - For each one, you want to first check if the slot is in the intent response's slot value. if it is, continue. Otherwise, output that Alexa doesn't understand and the should end session is set to false.
  - For the decimal numbers, all the functions will look the similar. If the BINARY_NUMBER is in the intent['slots'], you set the binary number equal to the value at that slot and you use the decimal converter. You then output that the binary number is that value and you set the end session to true.
    - For example, for the get_unsigned_decimal_number function, it will look like so:
    ```python
    def get_unsigned_decimal_number(intent, session):
      session_attributes = {}

      reprompt_text = None

      #TODO: Convert binary to decimal
      if BINARY_NUMBER in intent['slots']:
          binary_number = intent['slots'][BINARY_NUMBER]['value']
          decimal_number = convertToDecimal(binary_number, "unsigned")
          speech_output = "Unsigned binary number " + binary_number + " is " + decimal_number + " in decimal form."
          should_end_session = True
      else:
          speech_output = "I'm not sure what you meant by that. Please try again."
          should_end_session = False


      return build_response(session_attributes, build_speechlet_response(
          intent['name'], speech_output, reprompt_text, should_end_session))
    ```
    - For the other two types, you will change the following line of code so that unsigned is signed or twos:
    ```python
    decimal_number = convertToDecimal(binary_number, "unsigned")
    ```
  - For binary numbers, the functions will slightly vary. The set up is the same as for getting decimal numbers, but you will want to manipulate the conversion to binary since it returns a signed binary number.
    - For a basis, the signed binary looks like this:
    ```python
    def get_signed_binary_number(intent, session):
      session_attributes = {}

      reprompt_text = None

      #TODO: Convert decimal to binary
      if DECIMAL_NUMBER in intent['slots']:
          decimal_number = intent['slots'][DECIMAL_NUMBER]['value']
          binary_number = convertToBinary(int(decimal_number))
          speech_output = "Decimal number " + decimal_number + " is " + binary_number + " in signed binary form."
          should_end_session = True
      else:
          speech_output = "I'm not sure what you meant by that. Please try again."
          should_end_session = False


      return build_response(session_attributes, build_speechlet_response(
          intent['name'], speech_output, reprompt_text, should_end_session))
    ```
    - For unsigned, you want to strip binary_number so that it is
    ```python
    binary_number = convertToBinary(int(decimal_number))[1:]
    ```
    - And for two's complement, you want to check if the sign of decimal number is "-" and if it is twos complement it, replacing the 1 of the binary number as 0.
    ```python
    binary_number = convertToBinary(int(decimal_number))
        if decimal_number[0] == "-":
            bin = twosComp("0"+binary_number[1:])
            binary_number = bin
    ```
- The final version of the code is included in the repository for reference.
- Saving the code, copy and paste it to the Lambda editor and click save.
- Double check that your location is in N.Virginia and that your ARN located at the top right, or Amazon Resource Name, has us-east-1 is in because this is the only physical location in AWS for Alexa Skills so far. 
  - This is something that Amazon stresses because your skill won't work if it isn't configured correctly.
- Once you have your ARN, in the Default Region box in your developer tab, paste the ARN and click Save Endpoints.

## Testing
- Now that you've completed all this, you can click the Build tab and doublecheck that the checklist is filled out. 
- Then click the Test tab.
- You want to ensure that test is enabled for the skill.
- Open the skill by typing in "open echoconvert".
- Now you can ask Alexa one of the utterances we created earlier such as ```What is decimal number -15 in two's complement binary form?```
- Congrats! You've officially completed your skill.
