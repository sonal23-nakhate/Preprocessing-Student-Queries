# Institute FAQ Chatbot

A web-based chatbot for answering frequently asked questions about an educational institute.

## Features

- Modern, responsive UI with gradient design
- Real-time chat interface
- Synonym-aware query matching
- Handles multiple question variations

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

## Available Queries

The chatbot can answer questions about:
- College timings & office hours
- Fees & scholarships
- Admission process
- Library & hostel facilities
- Placement & courses
- Contact information
- Transport facilities
- Attendance requirements
- Exam schedules

## Project Structure

```
├── app.py                 # Flask backend
├── templates/
│   └── index.html        # HTML template
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Frontend logic
├── requirements.txt      # Python dependencies
└── README.md            # Documentation
```
