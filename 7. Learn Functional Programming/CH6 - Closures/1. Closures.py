def word_count_aggregator():
    count = 0
    def calculate_total(doc):
        splitting = doc.split(" ")
        words = len(splitting)
        nonlocal count 
        count += words
        return count
    return calculate_total

