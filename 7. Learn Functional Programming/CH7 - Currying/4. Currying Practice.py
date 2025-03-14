def lines_with_sequence(char):
    def with_char(length):
        sequence = char * length
        def with_length(doc):
            docs = doc.split("\n")
            count = 0
            for i in range(len(docs)):
                if sequence in docs[i]:
                    count += 1
            return count
        return with_length
    return with_char
