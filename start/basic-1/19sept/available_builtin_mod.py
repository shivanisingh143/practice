import sys
import textwrap

# print(sys.builtin_module_names)
word = ', '.join(sorted(sys.builtin_module_names))
print(word)
print(textwrap.fill(word, width=70))
