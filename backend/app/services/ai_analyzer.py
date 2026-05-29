import os
import json
import re
import time

from google import genai
from google.genai import types
from dotenv import load_dotenv

# =====================================================
# LOAD ENV
# =====================================================

load_dotenv()


class AIAnalyzer:

    # =====================================================
    # INIT
    # =====================================================

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        print("\n===== GEMINI API KEY =====")
        print(api_key)

        if not api_key:
            raise Exception("GEMINI_API_KEY not found in .env")

        self.client = genai.Client(
            api_key=api_key
        )

    # =====================================================
    # CLEAN JSON RESPONSE
    # =====================================================

    def clean_json_response(self, text):

        if not text:
            raise Exception("Empty response from Gemini")

        text = text.strip()

        # REMOVE MARKDOWN
        text = text.replace("```json", "")
        text = text.replace("```", "")

        # EXTRACT JSON
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if not match:
            raise Exception("No valid JSON found")

        json_text = match.group(0)

        # REMOVE CONTROL CHARACTERS
        json_text = re.sub(
            r"[\x00-\x1F\x7F]",
            "",
            json_text
        )

        return json_text.strip()

    # =====================================================
    # SAFE JSON PARSER
    # =====================================================

    def parse_json(self, text):

        try:

            return json.loads(text)

        except json.JSONDecodeError as e:

            print("\n===== JSON PARSE ERROR =====")
            print(e)

            print("\n===== INVALID JSON =====")
            print(text)

            raise Exception("Invalid JSON returned from Gemini")

    # =====================================================
    # GEMINI REQUEST WITH RETRY
    # =====================================================

    def generate_content_with_retry(
        self,
        prompt,
        max_output_tokens=8000
    ):

        MAX_RETRIES = 3

        for attempt in range(MAX_RETRIES):

            try:

                response = self.client.models.generate_content(

                    model="gemini-2.5-flash",

                    contents=prompt,

                    config=types.GenerateContentConfig(
                        temperature=0,
                        max_output_tokens=max_output_tokens,
                        response_mime_type="application/json"
                    )
                )

                return response

            except Exception as e:

                error_message = str(e)

                print("\n===== GEMINI ERROR =====")
                print(error_message)

                # HANDLE QUOTA LIMIT
                if (
                    "429" in error_message or
                    "RESOURCE_EXHAUSTED" in error_message or
                    "503" in error_message
                ):

                    wait_time = 20

                    print(
                        f"\nQuota exceeded. Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:
                    raise e

        raise Exception("Maximum retries exceeded")

    # =====================================================
    # ATS ANALYSIS
    # =====================================================

    def analyze_resume(self, resume_text, job_description):

        try:

            # LIMIT INPUT ONLY FOR ATS
            resume_text = resume_text[:2500]
            job_description = job_description[:1200]

            prompt = f"""
You are an advanced ATS resume analyzer.

Compare the RESUME with the JOB DESCRIPTION.

Return ONLY valid compact JSON.

STRICT JSON FORMAT:

{{
    "ATS_score": 0,
    "skills_detected": [],
    "missing_skills": [],
    "interview_questions": []
}}

RULES:
- ATS score must be between 0-100
- Minimum 5 skills_detected
- Minimum 5 missing_skills
- Minimum 5 interview_questions
- Keep output concise
- No markdown
- No explanation
- No extra text
- Output ONLY JSON

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

            response = self.generate_content_with_retry(
                prompt,
                max_output_tokens=4000
            )

            print("\n===== RAW ATS RESPONSE =====")
            print(response)

            if not hasattr(response, "text"):
                raise Exception("No response text from Gemini")

            result = response.text

            print("\n===== ATS RESPONSE TEXT =====")
            print(result)

            if not result:
                raise Exception("Empty response text")

            cleaned_result = self.clean_json_response(result)

            parsed_result = self.parse_json(cleaned_result)

            return parsed_result

        except Exception as e:

            print("\n===== ATS ANALYSIS ERROR =====")
            print(e)

            return {
                "error": str(e)
            }

    # =====================================================
    # GENERATE ATS RESUME
    # =====================================================

    def generate_resume(self, resume_text, job_description):

        try:

            resume_text = resume_text.strip()
            job_description = job_description.strip()

            prompt = f"""
You are an expert Australian ATS resume optimizer.

IMPORTANT:
You MUST preserve the ORIGINAL resume structure, formatting, section order, and writing style.

DO NOT create a new resume design.

DO NOT change:
- section order
- headings
- company order
- project order
- formatting style
- bullet style
- career timeline

ONLY improve the content according to the job description.

The response content will be inserted back into the user's original resume template.

Return ONLY valid JSON.

STRICT JSON FORMAT:

{{
    "name": "",
    "title": "",
    "contact": "",
    "summary": "",
    "skills": [],

    "experience": [
        {{
            "role": "",
            "company": "",
            "duration": "",
            "location": "",
            "points": []
        }}
    ],

    "projects": [
        {{
            "title": "",
            "points": []
        }}
    ],

    "education": [
        {{
            "degree": "",
            "institute": "",
            "year": ""
        }}
    ]
}}

CRITICAL RULES:
- Preserve ALL companies
- Preserve ALL projects
- Preserve ALL education entries
- Preserve original company sequence
- Preserve original project sequence
- Preserve career timeline exactly
- Keep same number of companies
- Keep same number of projects
- Keep same number of education entries
- Maximum 3 concise points per company
- Maximum 2 concise points per project
- Professional summary 40-60 words
- ATS keyword optimized
- No markdown
- No explanations
- Output ONLY valid JSON

ORIGINAL RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}
"""

            response = self.generate_content_with_retry(
                prompt,
                max_output_tokens=12000
            )

            print("\n===== RAW RESUME RESPONSE =====")
            print(response)

            if not hasattr(response, "text"):
                raise Exception("No response text from Gemini")

            result = response.text

            print("\n===== GENERATED RESUME TEXT =====")
            print(result)

            if not result:
                raise Exception("Empty response text")

            cleaned_result = self.clean_json_response(result)

            parsed_result = self.parse_json(cleaned_result)

            # SAFETY CHECKS

            if "experience" not in parsed_result:
                parsed_result["experience"] = []

            if "projects" not in parsed_result:
                parsed_result["projects"] = []

            if "education" not in parsed_result:
                parsed_result["education"] = []

            if "skills" not in parsed_result:
                parsed_result["skills"] = []

            return parsed_result

        except Exception as e:

            print("\n===== GENERATE RESUME ERROR =====")
            print(e)

            return {
                "error": str(e)
            }