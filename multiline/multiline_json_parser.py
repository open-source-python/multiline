__version__ = '1.0.2'
__all__ = [
    'dump', 'dumps', 'load', 'loads']
__author__ = 'Sanket Tantia'


import json
import re


def replace_new_line(matched_string):
    if matched_string:
        return matched_string.group(1)+re.sub(r'\n', r'\\n', 
                matched_string.group(2))+matched_string.group(3)
    else:
        return matched_string


def custom_parser(multiline_string):
    if isinstance(multiline_string, (bytes, bytearray)):
        multiline_string = multiline_string.decode()
    multiline_string = re.sub(r'\t', r' ', multiline_string)
    return re.sub(r'(\s*")(.*?)((?<!\\)")', replace_new_line, 
    multiline_string, flags=re.DOTALL)


def convert_multiline_to_singleline_dec(actual_fn):
    def wrapper_fn(input_json, *args, **kwargs):

        # For load fn, expected parameter is file pointer
        if actual_fn.__name__ == 'load':
            input_json = input_json.read()

        if isinstance(input_json, str):
            if input_json.startswith('\ufeff'):
                raise JSONDecodeError("Unexpected UTF-8 BOM (decode using utf-8-sig)",
                                    input_json, 0)
        else:
            if not isinstance(input_json, (bytes, bytearray)):
                raise TypeError(f'the JSON object must be str, bytes or bytearray, '
                                f'not {input_json.__class__.__name__}')

        # Parse the json only if multline line values are present
        if kwargs.get('multiline', False):
            kwargs.pop('multiline')
            return json.loads(custom_parser(input_json), *args, **kwargs)
        # Using the input json as it is
        else:
            return json.loads(input_json, *args, **kwargs)
        
    return wrapper_fn


@convert_multiline_to_singleline_dec
def loads(s, *args, **kwargs):
    pass


@convert_multiline_to_singleline_dec
def load(fp, *args, **kwargs):
    pass


def dump(obj, fp, *args, **kwargs):
    return json.dump(obj, fp, *args, **kwargs)


def dumps(obj, *args, **kwargs):
    return json.dumps(obj, *args, **kwargs)