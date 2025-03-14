def word_count_memo(document, memos):
    dict = memos.copy()
    if document in memos:
        count = word_count(document)
        return memos[document], dict
    else:
        count = word_count(document)
        dict[document] = count
        return count, dict
        
# Don't edit below this line

def word_count(document):
    count = len(document.split())
    return count

