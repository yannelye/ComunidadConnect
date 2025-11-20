# 🌎 Comunidad Connect

# 1) Executive Summary

**Problem:**  
Latino communities in the U.S. often face challenges accessing emergency resources and understanding emergency instructions in English. During crises, this can create confusion and prevent timely access to food, shelter, legal aid, and medical care.

**Solution:**  
**Comunidad Connect** is an early demo web application that helps Latino communities quickly find local emergency resources by ZIP code and provides English-to-simple Spanish translations of emergency instructions. This lightweight app runs in a Docker container for easy deployment and access.  

> ⚠️ **Note:** This is a very early demo. Some words or phrases may not translate perfectly, and not all ZIP codes or resources may be available.  
> 📍 **Current Coverage:** The ZIP codes included are the "hot spots" in the U.S. for Latino communities right now, including Northern Virginia (e.g., `20164`).  

---

# 2) System Overview

**Course Concept(s):**  
- Flask: Used to build a small REST API.  
- Docker: Containerizes the app for one-command deployment.  

**Architecture Diagram:**  

<img width="323" height="574" alt="Screenshot 2025-11-20 at 5 53 11 PM" src="https://github.com/user-attachments/assets/e59de704-170d-4ba1-9120-6573e7faefb6" />


**Data/Models/Services:**  
- **Data Source:** `assets/resources.json` contains emergency resource data.  
- **Size:** ~20 entries covering hotspots in U.S. Latino communities.  
- **Format:** JSON array of objects with keys `zip`, `name`, `category`, `address`, `phone`, `description`.  
- **License:** All data compiled from publicly available information and example/demo sources.  

---

# 3) How to Run (Local)
## Docker

### Build the Docker image:

docker build -t comunidadconnect:latest .

#### Run the Docker container:

docker run --rm -p 5000:5000 --env-file .env.example comunidadconnect:latest

### ⚠️ Make sure no other containers are using port 5000. Stop extra containers with:

docker ps ---> This will list all existing containers 

docker stop <CONTAINER_ID>   --->  Stop container using port 5000

### Open your browser:

http://localhost:5000

---

# 📝 How to Use
### 1️⃣ Search for Resources
Enter a ZIP code (e.g., 20164) in the search box.


Click Search to see local resources in your area.

<img width="729" height="467" alt="Screenshot 2025-11-20 at 5 47 26 PM" src="https://github.com/user-attachments/assets/a2e8d809-d885-49ff-a38d-cd3e5315f290" />


--- 

### 2️⃣ Translate Text
Type or paste English text into the translation box.

Click Translate.

View a simple Spanish translation and highlighted key actions.

Example:

"Evacuate and seek shelter." → "Evacuar y buscar refugio."

<img width="719" height="511" alt="Screenshot 2025-11-20 at 5 48 54 PM" src="https://github.com/user-attachments/assets/d399bd79-b7d6-4c59-a562-269a98521e2e" />


# 4) Design Decisions
Why this concept?

Flask was chosen for its lightweight nature, simplicity, and minimal setup. 

Docker ensures the app runs consistently on any machine with one command. Alternatives like FastAPI or larger frameworks were avoided for unnecessary complexity.

# Tradeoffs:

Performance: Runs quickly; data stored in memory.

Cost: No external services used.

Complexity: Minimal; adding a database would increase complexity.

Maintainability: Easy to maintain for small-scale demo.

### Security/Privacy:

No API keys or secrets used.

Input validation is minimal; accepts ZIP codes and English text only.

No PII collected.

### Ops:

Flask logs all requests automatically.

Only one container is needed; scaling not required for demo.

Known limitations: single-endpoint structure, no database, translations may be incomplete.

# 5) Results & Evaluation

Sample output JSON included above.

Fast response due to in-memory JSON; very low resource footprint.

Smoke tests verified /resources endpoint returns correct JSON structure.

# 7) What’s Next

Add more frontend enhancements (animations, styling).

Support additional ZIP codes dynamically.

Expand translation accuracy and handle more complex sentences.

Consider adding categories filtering and a small database for persistence.

# 8) Links

GitHub Repo: https://github.com/yannelye/Final_Case

# ⚙ Notes
Only one Docker container should run at a time to avoid port conflicts.
ZIP codes reflect current Latino "hot spots" in the U.S.
Some words or phrases may not translate perfectly in this early demo.

*This repo is used for educational purposes only*
