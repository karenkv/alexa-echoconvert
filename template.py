# Author: Karen Vu
# Date: June 7, 2018
# This code is for an Amazon Alexa skill that converts binary numbers to decimal
# or decimal numbers to binary. As a reference, this code was based off of
# the sample skill created by Amazon during a workshop I attended.

BINARY_NUMBER =
DECIMAL_NUMBER =

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """
    If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Echoconvert skill."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.

    #TODO: Give a welcome response.
    reprompt_text = "Please try asking for a conversion by, "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the number conversion skill. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_unsigned_decimal_number(intent, session):
    session_attributes = {}

    reprompt_text = None

    #TODO: Convert binary to decimal
    if BINARY_NUMBER in intent['slots']:
        binary_number = intent['slots'][BINARY_NUMBER]['value']
        decimal_number =
        speech_output =
        should_end_session = True
    else:
        speech_output = "I'm not sure what you meant by that. Please try again."
        should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_unsigned_binary_number(intent, session):
    session_attributes = {}

    reprompt_text = None

    #TODO: Convert decimal to binary
    if DECIMAL_NUMBER in intent['slots']:
        decimal_number = intent['slots'][DECIMAL_NUMBER]['value']
        binary_number =
        speech_output =
        should_end_session = True
    else:
        speech_output = "I'm not sure what you meant by that. Please try again."
        should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_signed_decimal_number(intent, session):
    session_attributes = {}

    reprompt_text = None

    #TODO: Convert binary to decimal
    if BINARY_NUMBER in intent['slots']:
        binary_number = intent['slots'][BINARY_NUMBER]['value']
        decimal_number =
        speech_output =
        should_end_session = True
    else:
        speech_output = "I'm not sure what you meant by that. Please try again."
        should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_signed_binary_number(intent, session):
    session_attributes = {}

    reprompt_text = None

    #TODO: Convert decimal to binary
    if DECIMAL_NUMBER in intent['slots']:
        decimal_number = intent['slots'][DECIMAL_NUMBER]['value']
        binary_number =
        speech_output =
        should_end_session = True
    else:
        speech_output = "I'm not sure what you meant by that. Please try again."
        should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_twoscomp_decimal_number(intent, session):
    session_attributes = {}

    reprompt_text = None

    #TODO: Convert binary to decimal
    if BINARY_NUMBER in intent['slots']:
        binary_number = intent['slots'][BINARY_NUMBER]['value']
        decimal_number =
        speech_output =
        should_end_session = True
    else:
        speech_output = "I'm not sure what you meant by that. Please try again."
        should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_twoscomp_binary_number(intent, session):
    session_attributes = {}

    reprompt_text = None

    #TODO: Convert decimal to binary
    if DECIMAL_NUMBER in intent['slots']:
        decimal_number = intent['slots'][DECIMAL_NUMBER]['value']
        binary_number =
        speech_output =
        should_end_session = True
    else:
        speech_output = "I'm not sure what you meant by that. Please try again."
        should_end_session = False


    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
# --------------- Events ------------------


def on_launch(launch_request, session):
    """
    Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """
    Called when the user specifies an intent for this skill
    """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # TODO: Dispatch to your skill's intent handlers
    if intent_name == "GetUnsignedBinaryIntent":
        return get_unsigned_binary_number(intent, session)
    elif intent_name == "GetDecimalIntentUnsigned":
        return get_unsigned_decimal_number(intent, session)
    elif intent_name == "GetSignedBinaryIntent":
        return get_signed_binary_number(intent, session)
    elif intent_name == "GetDecimalIntentSigned":
        return get_signed_decimal_number(intent, session)
    elif intent_name == "GetTwosCompBinaryIntent":
        return get_twoscomp_binary_number(intent, session)
    elif intent_name == "GetDecimalIntentTwosComp":
        return get_twoscomp_decimal_number(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """
    Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])


# --------------- Converter Functions ----------------------
def convertToDecimal(n, binType):
    '''
    Converts a binary number to decimal form
    '''


def convertToBinary(n):
    '''
    Converts a decimal number to binary form
    '''


def twosComp(n):
    '''
    Two's complement of a binary number
    '''
