import docx

def getText(filename):
    doc = docx.Document(filename) # open file
    fullText = []
    for para in doc.paragraphs:  # access each paragraph
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('demo5.docx'))
