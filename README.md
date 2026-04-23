# 🚀 AI Resume Analyzer & Interview Assistant

An AI-powered ATS (Applicant Tracking System) tool that analyzes resumes against job descriptions and provides actionable insights to improve job readiness.

---

## 📌 Overview

This application helps job seekers understand how well their resume matches a specific role.

Users can upload a resume and provide a job description to instantly receive:

- ✅ ATS Match Score  
- ✅ Matched Skills  
- ❌ Missing Skills  
- 💡 Improvement Suggestions  
- 🎯 Interview Questions  
- ⚠️ ATS Issues Detection  

The goal is to reduce manual effort and provide data-driven decision support for resume optimization.

---

## 🎥 Demo

👉 Video Walkthrough: https://drive.google.com/file/d/1YGMONt07F4CvaKsECe3h8xmPUgEC9aJo/view?usp=sharing

👉 Screenshots:
- Resume Upload  
- ATS Score Output  
- Skills Analysis  
- Suggestions & Insights  

(Add your screenshots here)

---

## ⚙️ Key Features

- Upload resume (PDF)
- Store files securely using Azure Blob Storage
- Paste job description
- AI-powered resume vs job description analysis
- ATS score calculation
- Skill matching and gap detection
- Resume improvement suggestions
- ATS issue detection (formatting issues, etc.)
- Interview question generation
- Loading/progress indicator for better UX

---

## 🧠 How It Works

1. User uploads a resume  
2. Resume is stored in Azure Blob Storage  
3. User provides a job description  
4. Backend sends data to Azure AI model  
5. AI analyzes content and returns:
   - ATS score  
   - Skills match  
   - Missing skills  
   - Suggestions  
   - Interview questions  
   - ATS issues  

---

## 🏗️ Architecture

```
User
  ↓
Frontend (HTML / CSS / JS)
  ↓
FastAPI Backend
  ↓
Azure Blob Storage (Resume Storage)
  ↓
Azure AI Foundry (Analysis Engine)
  ↓
Results (Score + Insights)
```

---

## 💼 Business Use Case

This system can be extended into real-world applications such as:

- Resume screening for HR teams  
- Workforce skill gap analysis  
- Internal hiring automation  
- Document analysis systems  
- Decision-support tools  

---

## 🛠️ Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- Python  
- FastAPI  

### AI Integration
- Azure AI Foundry (Azure OpenAI)  

### Cloud
- Azure Blob Storage  

---

## 📂 Project Structure

```
ai-resume-analyzer
│
├── backend
│   ├── main.py
│   ├── ai_analyzer.py
│   ├── blob_storage.py
│
├── frontend
│   ├── index.html
│   ├── css/style.css
│   └── js/script.js
```

---

## 🔌 API Endpoint

POST /upload-resume

### Request:
- Resume file  
- Job description  

### Response:
```json
{
  "ATS_score": 85,
  "skills_detected": ["Swift", "iOS", "MVVM"],
  "missing_skills": ["CI/CD", "Unit Testing"],
  "suggestions": ["Add CI/CD pipeline experience"],
  "interview_questions": ["Explain MVVM architecture"],
  "ats_issues": ["Resume contains tables"]
}
```

---

## ⚙️ Setup

### 1. Clone Repository
```
git clone https://github.com/yourusername/ai-resume-analyzer.git
```

### 2. Install Dependencies
```
pip install fastapi uvicorn azure-storage-blob openai
```

### 3. Configure Azure AI
```
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_DEPLOYMENT=your_model
```

### 4. Configure Azure Storage
```
AZURE_STORAGE_CONNECTION_STRING=your_connection
CONTAINER_NAME=resumes
```

### 5. Run Backend
```
uvicorn main:app --reload
```

### 6. Run Frontend
Open in browser:
```
frontend/index.html
```

---

## 🚧 Future Improvements

- Resume parsing (auto-extract fields)  
- ATS score visualization  
- AI-based resume rewriting  
- PDF report generation  
- Multi-resume comparison  
- Authentication & dashboard  
- Full cloud deployment  

---

## ⭐ Why This Project Matters

This project demonstrates the ability to:

- Build end-to-end AI systems  
- Integrate cloud services with AI  
- Solve real-world problems  
- Deliver practical and user-focused tools  

---

## 📬 Contact

Deepti Chawla  
Email: deeptichawla1994@gmail.com
