import random
from urllib.request import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []

phrases = {
    "class %%%(%%%):":
      "make a class name %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** params",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params",
    "*** = %%%()":
      "set *** to an instance of class %%%",
    "***.***(@@@)":
      "from *** get the *** function, call it with params self, @@@ ",
    "***.*** = '***'":
      "from *** get the *** attribute and set it to '***' "
}

if len(sys.argv) == 2 and sys.argv[1] == "english":
    phrases_first = True
else:
    phrases_first = False


for word in urlopen(word_url).readlines():
    words.append(str(word.strip(), encoding = "utf-8"))

def covert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(words, snippet.count("%%%"))]
    other_name = random.sample(words, snippet.count("***"))
    results = []
    param_name = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_name.append(', '.join(random.sample(words, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_name:
            result = result.replace("***", word, 1)

        for word in param_name:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
        while True:
            snippets = list(phrases.keys())
            random.shuffle(snippets)

            for snippet in snippets:
                phrase = phrases[snippet]
                question, answer = covert(snippet, phrase)
                if phrases_first:
                    question, answer = answer, question

                print(question)

                input("> ")
                print(f"answer: {answer}\n\n")
except EOFError:
    print("\nbye")
