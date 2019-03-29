#!/usr/bin/env python3

import os
import re

def md2xliff(root, name):
    filepath = os.path.join(root, name)
    language = "zh-Hans"
    bashCommand = f'extract "{filepath}.md" "{filepath}.{language}.xliff" "{filepath}.{language}.skl" en-US {language}'
    print(bashCommand)
    os.system(bashCommand)
    language = "en-US"
    bashCommand = f'extract "{filepath}.md" "{filepath}.{language}.xliff" "{filepath}.{language}.skl" en-US {language}'
    print(bashCommand)
    os.system(bashCommand)

for root, dirs, files in os.walk(".", topdown=False):
    [md2xliff(re.sub(r'^./?', '', root), name.replace('.md', '')) for name in files if ".md" in name]
