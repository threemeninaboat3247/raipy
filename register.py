import os
import pypandoc

f = open('README.txt','w+')
f.write(pypandoc.convert_file('README.md', 'rst'))
f.close()
os.system("python setup.py sdist upload")
os.remove('README.txt')
