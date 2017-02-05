import os
import sys
os.makedirs(os.getcwd() + '/quine')
f = open('quine/quine.py', 'w')
quine = [
  "import os",
  "import sys",
  "os.makedirs(os.getcwd() + '/quine')",
  "f = open('quine/quine.py', 'w')",
  "quine = [",
  "  ",
  "]",
  "for i in range(0,5):",
  "    print(quine[i], file=f)",
  "for i in range(0,len(quine)):",
  "    print(quine[5] + chr(34) + quine[i] + chr(34) + ',', file=f)",
  "for i in range(6, len(quine)):",
  "    print(quine[i], file=f)",
]
for i in range(0,5):
    print(quine[i], file=f)
for i in range(0,len(quine)):
    print(quine[5] + chr(34) + quine[i] + chr(34) + ',', file=f)
for i in range(6, len(quine)):
    print(quine[i], file=f)

