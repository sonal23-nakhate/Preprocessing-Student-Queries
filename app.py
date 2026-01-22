from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# FAQ keywords with synonyms
faq_keywords = {
    "timings": ["timing", "time", "hours", "schedule"],
    "fees": ["fees", "fee", "tuition", "payment", "cost"],
    "admission": ["admission", "admit", "apply", "enroll"],
    "library": ["library", "books", "reading"],
    "hostel": ["hostel", "mess", "room", "accommodation"],
    "contact": ["contact", "phone", "number", "call"],
    "email": ["email", "mail"],
    "placement": ["placement", "job", "career"],
    "attendance": ["attendance", "present", "presence"],
    "exam": ["exam", "test", "assessment"],
    "office": ["office"],
    "scholarship": ["scholarship", "scholar"],
    "address": ["address", "location", "where"],
    "course": ["course", "courses", "program", "degree"],
    "transport": ["transport", "bus", "travel"]
}

# FAQ responses
faq_responses = {
    "timings": "College timings are 9 AM to 5 PM.",
    "fees": "Annual tuition fees are ₹85,000.",
    "admission": "Admission is based on merit and entrance exam.",
    "library": "Library is open from 9 AM to 8 PM.",
    "hostel": "Hostel facility is available for students.",
    "contact": "Contact number is 9876543210.",
    "email": "Email ID is info@institute.edu",
    "placement": "Placement training starts from third year.",
    "attendance": "Minimum 75% attendance is mandatory.",
    "exam": "Exams are conducted semester-wise.",
    "office": "Office hours are 10 AM to 4 PM.",
    "scholarship": "Government and merit-based scholarships are available.",
    "address": "Institute is located at Nagpur, Maharashtra.",
    "course": "We offer Engineering, Diploma, and Management courses.",
    "transport": "Bus facility is available from major routes."
}

def get_bot_response(user_message):
    user_message = user_message.lower()
    
    # Check for each category
    for category, keywords in faq_keywords.items():
        for word in keywords:
            if word in user_message:
                return faq_responses[category]
    
    return "Sorry, I couldn't understand your question. Please ask about timings, fees, admission, library, hostel, contact, email, placement, attendance, exams, courses, or transport."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Please enter a message.'})
    
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
