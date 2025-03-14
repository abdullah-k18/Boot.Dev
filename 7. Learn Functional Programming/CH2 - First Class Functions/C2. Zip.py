valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line

def pair_document_with_format(doc_names, doc_formats):
    paired_docs = zip(doc_names, doc_formats) 
    filtered_docs = list(filter(lambda doc: doc[1] in valid_formats, paired_docs))
    return filtered_docs

