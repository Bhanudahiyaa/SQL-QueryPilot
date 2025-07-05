# 🧠 SQL-Whisperer

---

## 📌 Overview

**SQL Query Pilot** is an intelligent tool that translates natural language into SQL queries and executes them on a database—all through a user-friendly interface. Whether you're a beginner learning SQL or a developer rapidly prototyping, this platform accelerates data interactions with ease.

---
## 📸 Preview
<img width="1470" alt="Screenshot 2025-07-05 at 18 52 40" src="https://github.com/user-attachments/assets/909fc8aa-7fd3-4fd6-87f3-10580bfb6257" />
<img width="1470" alt="Screenshot 2025-07-05 at 18 52 50" src="https://github.com/user-attachments/assets/5f9fc4c1-7cef-4fe5-a32b-12a3c9e4d22e" />
<img width="1470" alt="Screenshot 2025-07-05 at 18 52 57" src="https://github.com/user-attachments/assets/df3c0e5b-f633-4e7e-95e9-e3b1d2b263d2" />
<img width="1470" alt="Screenshot 2025-07-05 at 18 53 22" src="https://github.com/user-attachments/assets/307228d9-c2fe-4b2a-bb23-353ee830ee0f" />
<img width="1470" alt="Screenshot 2025-07-05 at 18 53 27" src="https://github.com/user-attachments/assets/eea1eb55-b5c0-491d-a013-5275ae2d48a3" />







---
## ⚙️ Tech Stack

- **Frontend**: Streamlit
- **Backend AI**: Google Gemini Pro via `google-generativeai`
- **Database**: SQLite (default), extendable to other DB engines
- **Language**: Python 3.10+
- **Deployment**:Streamlit Cloud

---

## 🔁 How It Works

1. **Input Query in Natural Language**  
   _e.g., "List all employees with a salary above 50,000"_
2. **AI Translates to SQL**  
   Gemini generates the corresponding SQL.
3. **Execution Engine**  
   Query is run on a user-selected or uploaded database.
4. **Output Table**  
   Cleanly formatted results are displayed instantly.

---

## 🔍 Key Features

- 🧠 Natural language to SQL conversion
- ⚡ One-click query execution
- 🔄 Editable SQL previews
- 📂 Upload your own `.db` SQLite file
- 🧪 Safe read-only query handling

---



## 🧰 Setup Instructions

### ✅ Prerequisites

- Python 3.10 or higher
- Google Gemini API key

### 📦 Installation

```bash
git clone https://github.com/Bhanudahiyaa/SQL-QueryPilot.git
cd SQL-QueryPilot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
