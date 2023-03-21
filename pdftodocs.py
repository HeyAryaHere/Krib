from pypdf import PdfReader
import docx

doc = "trial.docx"
reader = PdfReader("trial.pdf")
page = reader.pages[0]
text = page.extract_text()

mydoc = docx.Document()
mydoc.add_paragraph(text)
mydoc.save(doc)