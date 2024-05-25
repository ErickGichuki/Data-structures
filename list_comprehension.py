my_words = ["eric", "jay", "beryl", "fay", "sam", "kamau"]
odd_len_my_words = [word for word in my_words if len(word) % 2 != 0]

print("The words: ", my_words)
print("words with odd length: ", odd_len_my_words)