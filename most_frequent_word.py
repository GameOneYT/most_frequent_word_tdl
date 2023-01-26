import sqlite3
from collections import Counter


# Connect to the database
conn = sqlite3.connect("db/messages.db")
c = conn.cursor()

# Execute a SQL query to get a list of all the words in the table
c.execute("SELECT msg_text FROM messages WHERE msg_text NOT LIKE ''")

data = c.fetchall()

# Create an empty list to store the words
words = []

# Iterate over the data
for row in data:
    # Split the row into a list of words
    row_words = row[0].split()
    
    # Add the words to the list
    words.extend(row_words)

# Count the frequency of each word

all_words = list((map(lambda x: x.lower(), words)))
word_counts = Counter(all_words)


# Get the 50 most common words
most_common_words = word_counts.most_common(50)

# Iterate over the most common words and calculate the percentage of each word
for word, count in most_common_words:
    percentage = count / len(all_words) * 100
    frequency = len(all_words) / count
    print(f"{word}: {count} times - {percentage:.2f}% - every {frequency:.2f} words")
    
print("\nWords count: "+str(len(all_words)))
