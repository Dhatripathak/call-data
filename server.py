from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/process_name", methods=["POST"])
def process_name():
    name = request.form["SpeechResult"]
    response = VoiceResponse()

    # Ask for the caller's age
    response.gather(input="speech", action="/process_age", method="POST")
    response.say(f"Thank you, {name}. Please tell us your age.")
    return str(response)

@app.route("/process_age", methods=["POST"])
def process_age():
    age = request.form["SpeechResult"]
    response = VoiceResponse()

    # Ask for the number of family members
    response.gather(input="speech", action="/process_family_members", method="POST")
    response.say(f"Got it. You are {age} years old. How many family members do you have?")
    return str(response)

@app.route("/process_family_members", methods=["POST"])
def process_family_members():
    family_members = request.form["SpeechResult"]
    response = VoiceResponse()

    # End the call
    response.say(f"Thank you for providing the information. You have {family_members} family members. Goodbye!")
    response.hangup()
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)