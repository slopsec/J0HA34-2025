sample_text = """
Why Python Deserves Its Place at the Top

Python has become one of the most widely used programming languages in the world, and for good reason. Its appeal lies not only in technical capability, but also in its simplicity and adaptability. Whether you are a beginner writing your first script or a professional building large-scale systems, Python offers a balance of clarity and power that few languages can match.

At the heart of Python’s popularity is its readability. Its syntax is concise and intuitive, designed to mirror natural language as closely as possible. This lowers the barrier of entry for newcomers while allowing experienced developers to write cleaner, more maintainable code. The philosophy behind Python—often summarised in the “Zen of Python”—emphasises beauty, simplicity, and explicitness, making collaboration smoother and reducing the likelihood of bugs.

Equally important is Python’s versatility. It is the backbone of countless domains: powering websites with Django and Flask, handling data science and machine learning with libraries like pandas, NumPy, and TensorFlow, and even enabling automation for everyday tasks. This breadth means that learners can start small—perhaps with automating a spreadsheet—and gradually progress to building sophisticated AI models, all without leaving the ecosystem.

The Python community is another factor in its success. Millions of developers worldwide contribute libraries, tutorials, and tools that extend Python’s reach and ensure that help is never far away. This collaborative spirit has turned Python into more than just a programming language; it is a living, evolving platform for problem-solving.

Ultimately, Python thrives because it combines accessibility with depth. It empowers beginners, accelerates research, and drives innovation across industries. In a world where technology evolves rapidly, Python continues to prove that elegance, clarity, and community are timeless strengths.
"""

# Dictionary     { word : count }

# convert to lowercase and split
sample_text = sample_text.lower()
word_list = sample_text.split()

# Word count dictionary
word_count = { }

# For each word
# Clean up word
# if word not previously met set dictionary entry to 1
# if word already in dictionary, increase value by 1
for index in range(len(word_list)):
    word_list[index] = word_list[index].strip(" ,.;:'\"\n")
    
    # if not met create entry
    if word_list[index] not in word_count.keys():
        word_count[word_list[index]] = 1
    else: # If entry already exists
        word_count[word_list[index]] += 1  # increase counter

print(word_count)

