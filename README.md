# Amazon Alexa Skill: Binary and Decimal Converter

## About

In this workshop, we will be creating an Amazon Alexa skill that converts from binary form to decimal form and vice versa.
Additionally, we will incorporating three types of binary forms for the user to choose from:
- Unsigned
- Signed
- Two's Complement

### Goals

This workshop will teach you the following:
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
    - I will be naming my invocation "echoconvert"
- Hit Save Model at the top and select Intents in the left menu

## Intents

-
