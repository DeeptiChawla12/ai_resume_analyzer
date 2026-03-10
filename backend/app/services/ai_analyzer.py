import os
import json
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()


class AIAnalyzer:

    def __init__(self):

        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-02-01",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )

        self.model = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    def analyze_resume(self, resume_text, job_description):

        prompt = f"""
You are an advanced ATS resume analyzer used by tech companies.

Compare the RESUME with the JOB DESCRIPTION.

Score from 0 to 100 based on:
- skill match
- experience
- tools
- architecture knowledge

Return ONLY JSON.

Format:

{{
"ATS_score": number,
"skills_detected": [],
"missing_skills": [],
"interview_questions": []
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an ATS resume analyzer."},
                {"role": "user", "content": prompt}
            ]
            
        )

        result = response.choices[0].message.content

        try:
            return json.loads(result)

        except:
            return {"error": result}