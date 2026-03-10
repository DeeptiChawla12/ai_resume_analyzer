# AI Resume Analyzer

AI Resume Analyzer is an AI-powered ATS (Applicant Tracking System) tool that compares a candidate’s resume with a job description and provides an ATS score, skills match analysis, missing skills, and improvement suggestions.

This project helps job seekers optimize their resumes to improve their chances of passing ATS screening systems used by companies during recruitment.

---

# Features

• Upload Resume  
• Store resume securely in Azure Blob Storage  
• Paste Job Description  
• AI-powered Resume vs Job Description comparison  
• ATS Score calculation  
• Matched Skills detection  
• Missing Skills identification  
• AI suggestions to improve resume  
• ATS issues detection  
• Interview question generation  
• Resume analysis report download  
• Loader / progress indicator while AI analysis runs  

---

# Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI

### AI Integration
- Azure AI Foundry (Azure OpenAI)

### Cloud Services
- Azure Blob Storage

### Tools
- REST APIs
- CORS Middleware

---

# Azure Services Used

### Azure AI Foundry
Used to deploy and run the AI model that analyzes the resume and job description.

### Azure Blob Storage
Used to securely store uploaded resume files before processing.

---

# Project Architecture

```
User
  ↓
Frontend (HTML / CSS / JS)
  ↓
FastAPI Backend
  ↓
Azure Blob Storage (Store Resume)
  ↓
Azure AI Foundry (Resume Analysis)
  ↓
Return ATS Score + Suggestions
```

---

# Project Structure

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
│   ├── css
│   │   └── style.css
│   └── js
│       └── script.js
```

---

# How It Works

1. User uploads a resume file.
2. Resume is uploaded to **Azure Blob Storage**.
3. User pastes the job description.
4. Backend sends resume content and job description to **Azure AI Foundry**.
5. AI analyzes the resume.
6. The system returns:

- ATS Score
- Matched Skills
- Missing Skills
- Resume Improvement Suggestions
- ATS Issues
- Interview Questions

---

# Installation

## 1 Clone the repository

```
git clone https://github.com/yourusername/ai-resume-analyzer.git
```

---

## 2 Install dependencies

```
pip install fastapi
pip install uvicorn
pip install azure-storage-blob
pip install openai
```

---

## 3 Configure Azure AI Foundry

Add your Azure OpenAI credentials in your backend configuration:

```
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_DEPLOYMENT=your_model_deployment
```

---

## 4 Configure Azure Blob Storage

Add your storage connection string:

```
AZURE_STORAGE_CONNECTION_STRING=your_connection_string
CONTAINER_NAME=resumes
```

---

## 5 Run the backend server

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 6 Run the frontend

Open the frontend file in your browser:

```
frontend/index.html
```

---

# API Endpoint

### POST

```
/upload-resume
```

### Request Parameters

- Resume file
- Job description text

### Example Response

```
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

# Future Improvements

- Resume parsing (extract name, email, skills)
- ATS score visualization charts
- Resume rewriting using AI
- PDF report generation
- Multiple resume comparison
- Authentication system
- Cloud deployment
