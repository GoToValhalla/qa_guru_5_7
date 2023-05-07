from pypdf import PdfReader
import os
from property import  RESOURCES_PATH

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_pdf():
    pdf_file = os.path.join(RESOURCES_PATH, 'docs-pytest-org-en-latest.pdf')
    reader = PdfReader(pdf_file)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)
    assert number_of_pages == 412
    assert page is not None, 'Page is empty'
    assert text is not None and len(text.strip()) > 0, 'Text is empty'