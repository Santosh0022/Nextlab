# -*- coding: utf-8 -*-
"""Welcome To Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

import re
import json

text = '''
{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}
'''


data = json.loads(text)


order_ids = [order["id"] for order in data.get("orders", [])]


error_codes = [error["code"] for error in data.get("errors", [])]


combined_list = order_ids + error_codes

print("\033[3m" + ", ".join(map(str, combined_list)) + "\033[0m")