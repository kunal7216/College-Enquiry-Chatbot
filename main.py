

from flask import Flask, render_template, request
import random

app = Flask(__name__)


def getresponse(user_input):
    user_input_lower = user_input.lower()

    if any(keyword in user_input_lower for keyword in ['hi', 'hello', 'hey']):
        return ["Hello! What can I do for you?"]

    elif 'admission' in user_input_lower:
        return ["Oh, sorry! Currently, admissions are closed, but you can contact the Admission Office for more information. Application can also be submitted online through the Graphice Era University. Refer <a href=https://GEHU.ac.in/academics/admissions/admissions-and-eligibility>website</a>."]

    elif 'courses' in user_input_lower:
        return ["We provide Bachelors Programmes in Automobile Engineering, Civil Engineering, Computer Engineering, Electrical Engineering, Electronics and Telecommunications Engineering, Information Technology Engineering, Mechanical Engineering, and Applied Sciences. For more details, visit <a target=\"_blank\" href=\"https://gehu.ac.in/academics/\">here</a>."]

    elif 'fees structure' in user_input_lower:
        return ["For Fee details, visit <a target=\"_blank\" href=\"https://gehu.ac.in/academics/admissions/fee-structure/\">here</a>."]

    elif 'location' in user_input_lower:
        return ["Our college is located in Clement Town, Dehradun, Uttarakhand. For more details, visit <a target=\"_blank\" href=\"https://goo.gl/maps/nABAciXu58ty7PyX6\">here</a>."]

    elif 'hostel' in user_input_lower:
        return ["GEHU provides safe and affordable hostel facilities for boys and girls. For more details, visit <a target=\"_blank\" href=\"https://GEHU.ac.in/about/infrastructure-and-facilities/hostel-facility/\">here</a>."]

    elif 'placement' in user_input_lower:
        return ["Various companies, including TCS, RELIANCE JIO, L AND T INFOTECH, are coming to recruit our students and offer maximum packages. For more information, visit <a target=\"_blank\" href=\"https://GEHU.ac.in/students/placements/our-recruiters/\">here</a>. Our college organizes various activities related to placements. For the latest update, visit <a target=\"_blank\" href=\"https://GEHU.ac.in/students/placements/placement-cell-activities/\">here</a>."]

    else:
        # Default response if no specific pattern is matched
        return ["I'm sorry, I didn't understand that. Can you please provide more details?"]




def chat(inp):
    inp_x = inp.lower()
    response = getresponse(inp_x)
    return random.choice(response)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    try:
        userText = request.args.get('msg')
        return str(chat(userText))
    except Exception as e:
        print("Error during prediction:", e)
        return "Error during prediction"

if __name__ == "__main__":
    app.run()
