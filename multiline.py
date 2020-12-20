__version__ = '1.0.1'
__all__ = [
    'dump', 'dumps', 'load', 'loads']

__author__ = 'Sanket Tantia'

import json
import re


def remove_new_line_occurence(matched_string):
    return matched_string.group(1)+re.sub(r'\n', r'\\n', 
    matched_string.group(2))+matched_string.group(3)


def convert_multiline_to_singleline(multiline_string):
    if isinstance(multiline_string, (bytes, bytearray)):
        multiline_string = multiline_string.decode()
    return re.sub(r'(:\s*(?:"|\'))(.*)((?<!\\)(?:"|\'))', remove_new_line_occurence, 
    multiline_string, flags=re.DOTALL)


def loads(s, *args, **kwargs):
    if isinstance(s, str):
        if s.startswith('\ufeff'):
            raise JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)",
                                  s, 0)
    else:
        if not isinstance(s, (bytes, bytearray)):
            raise TypeError(f'the JSON object must be str, bytes or bytearray, '
                            f'not {s.__class__.__name__}')

    if kwargs.get('multiline', False):
        s = convert_multiline_to_singleline(s)
        kwargs.pop('multiline')
    return json.loads(s, *args, **kwargs)


def load(fp, *args, **kwargs):
    pass


# TEST
print(loads(bytearray("""{"a": "ssssss
sd\\"mskds","b": "Ssss","c": "sdjs
ndjasn
djasn"}""", 'utf-8'), multiline=True))

# TEST
# z = re.sub(r'f(\n)', r'\\n', z, re.DOTALL)
# print(z)
# with open('multilinejson-env/test.json', 'r') as f:
#     print(json.load(f))