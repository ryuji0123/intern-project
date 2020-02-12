from PIL import Image
import sys
sys.path.append('/path/to/dir')

import pyocr
import pyocr.builders
import os

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

# use all files on ./image/ directory.
for root, dirs, files in os.walk("./image/."):
    for filename in files:
        print(filename)
        try:
            input_img = Image.open('./image/' + filename)
        except: continue
        txt = tool.image_to_string(
            input_img,
            lang='jpn',
            builder=pyocr.builders.TextBuilder()
            )

        with open('./out.txt', mode='w') as f:
            f.write(txt)
