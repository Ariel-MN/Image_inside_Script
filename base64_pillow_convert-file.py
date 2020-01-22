# -*- coding: utf-8 -*-
"""
todo: Documentation

    Project name: _Studi_
    File name: base64_pillow_convert-file
    
    Date created: 22/1/2020
    Date last modified: 31/12/2019
    Status: Development

    Python version: 3.8
    Modules required: pillow, base64
"""
__author__ = 'Ariel Montes Nogueira'
__website__ = 'http://www.montes.ml'
__email__ = 'arielmontes1989@gmail.com'

__copyright__ = 'Copyright © 2020-present Ariel Montes Nogueira'
__credits__ = []
__license__ = '''
                Licensed under the Apache License, Version 2.0 (the "License");
                you may not use this file except in compliance with the License.
                You may obtain a copy of the License at
                
                    http://www.apache.org/licenses/LICENSE-2.0
                
                Unless required by applicable law or agreed to in writing, software
                distributed under the License is distributed on an "AS IS" BASIS,
                WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
                See the License for the specific language governing permissions and
                limitations under the License.'''
__recovery__ = 'https://github.com/Ariel-MN/Image_inside_Script'
__version__ = '1.0'


import base64
from PIL import Image, ImageTk


def file_convert(file_name=None):
    """ Convert image file to Binary or String utf-8 """

    if file_name is not None:
        file_name = str(file_name)

        with open(file_name, 'rb') as image_file:
            encoded_binary = base64.encodebytes((image_file.read()))  # Binary image convertion
            encoded_string = encoded_binary.decode("utf-8")  # String image convertion

        print("<< Format: Binary >>\n")
        print(f"Length: {len(encoded_binary)}\n")
        print(encoded_binary)

        print("\n<< Format: String utf-8 >>\n")
        print(f"Length: {len(encoded_string)}\n")
        print(encoded_string)


def base64_tools(run):
    """ Some examples of how to use base64 and Pillow """

    if run == True:

        # Binary encode image:
        ico_b = b'R0lGODlhMAAwAHAAACH5BAEAAAEALAAAAAAwADAAgQAAAAAAAAAAAAAAAAK6jI+py+0Po5y0Wgny\n3Sh7wG2fF1ojWU4nmkKr1' \
                b'rpvLK/084JpDuch/zH4REDU0FQ0zpDJ3hIWaSptgWCtKXyOcFTrYbhc\nhFlZanmrMJc7YTb6e0pDwfK3Gq4D6xK2O/yMRuYGxJ' \
                b'CnBcUX54cXVyXIyLKo9+j4BohY2WgJiXnp\n1OXF2cnp+dnZJjalKcgTZbhYGuoKKjXqMCnFtJqrG8jb61VUcnSTCltcityAqjx' \
                b'I2XwJffssXW19\nLV0AADs=\n'

        # String encode image:
        ico_s = """R0lGODlhMAAwAHAAACH5BAEAAAEALAAAAAAwADAAgQAAAAAAAAAAAAAAAAK6jI+py+0Po5y0Wgny3Sh7wG2fF1ojWU4nmkKr1rpvL
        K/084JpDuch/zH4REDU0FQ0zpDJ3hIWaSptgWCtKXyOcFTrYbhchFlZanmrMJc7YTb6e0pDwfK3Gq4D6xK2O/yMRuYGxJCnBcUX54cXVyXIyLKo9
        +j4BohY2WgJiXnp1OXF2cnp+dnZJjalKcgTZbhYGuoKKjXqMCnFtJqrG8jb61VUcnSTCltcityAqjxI2XwJffssXW19LV0AADs="""

        # Tool 1 - Convert binary encode into string encode:
        image_s = ico_b.decode('utf-8')

        # Tool 2 - Create image file from string:
        image_result = open('test_file.png', 'wb')  # create file
        image_result.write(base64.decodebytes(ico_b))  # write file for binary encode
        image_result.write(base64.decodebytes(ico_s.encode()))  # write file for string encode

        # Tool 3 - Show an image view:
        pic_bytes = base64.b64decode(ico_b)  # trasform into bytes with Base64
        pillow_img = ImageTk.BytesIO(pic_bytes)  # create a pillow image
        img = Image.open(pillow_img)  # get the image with PIL Image
        img.show()  # open-view the image


""" Program triggers """
file_convert(file_name=None)  # file_name=image.jpg
base64_tools(run=True)  # run=True for run
