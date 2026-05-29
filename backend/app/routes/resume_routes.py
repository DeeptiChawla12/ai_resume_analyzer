from fastapi import APIRouter, UploadFile, File, Form

from app.services.resume_parser import ResumeParser
from app.services.ai_analyzer import AIAnalyzer

router = APIRouter()

parser = ResumeParser()
analyzer = AIAnalyzer()


# ATS ANALYSIS

@router.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    contents = await file.read()

    text = parser.extract_text(
        contents,
        file.filename
    )

    analysis = analyzer.analyze_resume(
        text,
        job_description
    )

    return analysis


# GENERATE RESUME

@router.post("/generate-resume")
async def generate_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):

    contents = await file.read()

    text = parser.extract_text(
        contents,
        file.filename
    )

    generated_resume = analyzer.generate_resume(
        text,
        job_description
    )

    return generated_resume
    