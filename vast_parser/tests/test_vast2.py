import os
from vast_parser import vast2

def _test_vast(vast_document_path):
    vast2_document_filename = os.path.abspath(vast_document_path)

    # Getting document content
    vast_file_content = ""
    with open(vast2_document_filename, mode="r") as vast_file: vast_file_content = vast_file.read()

    # Parsing document via models
    vast_document = vast2.VAST.parse(vast_file_content)
    parsing_result = vast_document.render(fragment=True)

    assert parsing_result == vast_file_content

def test_vast2_inline_document():
    _test_vast("tests/test_files/vast2_inline_document.xml")