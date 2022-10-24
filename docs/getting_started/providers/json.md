# JSON

## Prepare

For more speed this provider you can install simplejson

``` sh
poetry add simplejson
```

## Usage

In this example we have *data.json*:

``` json
{
   "test":{
      "test_key1":"1",
      "test_key2":"2",
      "test_key3":"3",
      "test_key4":{
         "test_key4_1":"1",
         "test_key4_2":"2"
      }
   },
   "test0": "0"
}
```

In JSON's providers we have two get-modes: basic and path

Basic mode use as default python dict. If you want get value on sub
(non-first) level, you should take first level dictionary by key and get
values in this dict as default.

Path-mode make easy work with nested dictionary. You can type separated
keys of nested values. *Example: test.test_key4.test_key4_1*

``` python
from sitri.contrib.json import JsonConfigProvider


conf = JsonConfigProvider(json_path="./data.json", default_separator="/")

conf.get("test.test_key1", ":(")
# Output: :(

conf.get("test.test_key1", ":(", path_mode=True)
# Output: :(

conf.get("test.test_key1", ":(", path_mode=True, separator=".")
# Output: 1

conf.get("test/test_key1", ":(", path_mode=True)
# Output: 1

conf.get("test0")
# Output: 0
```
