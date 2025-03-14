messages = [
            "well dang it",
            "dang the whole dang thing",
        ]

def filter_messages(messages):
    filtered_messages = []
    removal_counts = [] 

    for message in messages:
        words = message.split()
        print("Words: ",words)
        clean_words = []
        count = 0 
        for word in words:
            if word == "dang": 
                count += 1
            else:
                clean_words.append(word)
                print("cleaned: " ,clean_words)
        filtered_messages.append(" ".join(clean_words)) 
        removal_counts.append(count) 
        print(removal_counts)
    return filtered_messages, removal_counts

filter_messages(messages)
