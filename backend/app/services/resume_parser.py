import pdfplumber
import docx
import io


class ResumeParser:

    def extract_text(self, file_bytes, filename):

        if filename.endswith(".pdf"):
            text = ""

            with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""

            return text

        elif filename.endswith(".docx"):

            doc = docx.Document(io.BytesIO(file_bytes))

            return "\n".join([para.text for para in doc.paragraphs])

        else:
            return "Unsupported format"