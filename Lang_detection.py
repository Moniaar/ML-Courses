import polyglot
from polyglot.text import Text, Word
text = Text("아는데요?")
print("Language Detected: Code={}, Name={}\n".format(text.language.code, text.language.name))
