# multiline
Open source python module, which can parse multiline values in json files.

This module provides a wrapper on top of the four methods (load, loads, dump, dumps) present in the default json module. This is done to avoid the need of importing both modules `multiline` and `json`. 

If multline parsing is required while loading the json, then an additional argument ```multiline=True``` needs to be provided to trigger the custom parser.


While converting a raw json string to dictionary object:
```
input_dic = multiline.loads("""{
    "key1": {
        "subkey": {
            "subsubkey1": {
                "subsubsubkey1": "lorem dipsum\\n line1
                lorem \\"dipsum line2
                lorem dipsum line 3"
            },
            "subsubkey2": {
                "subsubsubkey1": "lorem dipsum\\n line1
                lorem dipsum line2"
            }
        }
    }
}""", multiline=True)
```


While reading a json file to dictionary object:
```
with open('tests/test.json', 'r') as fp:
    input_dic = multiline.load(fp, multiline=True)
```

Additional information about the package can be found at: https://sankettantia.medium.com/multiline-a-python-package-for-multi-line-json-values-c4f7a76f0305