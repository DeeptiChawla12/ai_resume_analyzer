from fastapi import APIRouter, UploadFile, File, Form
from app.services.resume_parser import ResumeParser
from app.services.ai_analyzer import AIAnalyzer
from app.services.blob_service import BlobUploader

router = APIRouter()

parser = ResumeParser()
analyzer = AIAnalyzer()
blob_uploader = BlobUploader()


@router.post("/upload-resume")
async def upload_resume(
        file: UploadFile = File(...),
        job_description: str = Form(...)
):

    contents = await file.read()

    # Upload to Azure Blob
    blob_uploader.upload_file(contents, file.filename)

    # Extract text
    text = parser.extract_text(contents, file.filename)

    # Analyze with AI
    analysis = analyzer.analyze_resume(text, job_description)

    return analysis