# ComunidadConnect

**ComunidadConnect** is a simple web application designed to help Spanish-speaking communities access critical resources and understand emergency instructions in **accessible Spanish**. This is a very early demo, so there may be times where certain words or phrases cannot be translated perfectly.

---

## Features

1. **Search Local Resources**  
   - Enter a U.S. ZIP code to find local resources such as:  
     - Food banks  
     - Medical clinics  
     - Legal aid services  
     - Community centers  

2. **Simple Spanish Translation**  
   - Enter English instructions or phrases to receive a **simplified Spanish version**.  
   - The app also extracts **key actions** from your text to highlight important steps (e.g., "Evacuate", "Call 911", "Go to shelter").  

---

## Quick Start

### Requirements
- Docker installed on your system
- `.env.example` file configured with any environment variables (optional)

### Running the App
1. Build the Docker image:

   ```bash
   docker build -t comunidadconnect:latest .

   2. Run the container on port 5000:
   docker run --rm -p 5000:5000 --env-file .env.example comunidadconnect:latest

   3. Open your web browser and go to:
   http://localhost:5000

How to Use
Search Resources
Enter a U.S. ZIP code (e.g., 20164 for Northern Virginia).
Click Search.
View a list of nearby resources, including addresses, phone numbers, and descriptions.
Translate Text
Type an English instruction or message in the Simple Spanish Translation box.
Click Translate.
See the simplified Spanish translation and a list of key actions extracted from your text.
Notes
This is an early demo, so some words or phrases may not translate perfectly.
The app currently focuses on key Latino community “hot spots” in the U.S.
The translation system uses a simplified dictionary-based approach to maximize accessibility.
Example Use Cases
Helping Spanish speakers understand emergency instructions during disasters.
Quickly locating local food banks, medical clinics, and legal aid services.
Translating English instructions into simple Spanish for community outreach.
License
This project is for educational/demo purposes.
