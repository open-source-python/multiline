import multiline

def test_loads_true():
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
    assert input_dic.__class__.__name__ == 'dict'



def test_load_true():
    with open('tests/test.json', 'r') as fp:
        input_dic = multiline.load(fp, multiline=True)
        assert input_dic.__class__.__name__ == 'dict'
