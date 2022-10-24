# Vedis

## Prepare

The configuration and start of the Vedis remains at your side

Install Vedis client with Poetry:

``` sh
poetry add vedis
```

## Usage

`VedisConfigProvider <sitri.contrib.vedis.VedisConfigProvider>`{.interpreted-text
role="class"} search variables in hash object from vedis (default hash
name - sitri).

In this example I create two vars in hash:

:   a = 1 b = 2

``` python
from vedis import Vedis

from sitri.contrib.vedis import VedisConfigProvider

conf = VedisConfigProvider(hash_name="test", vedis_connector=lambda: Vedis(":mem:"))

print(conf.get("a"))
# Output: 1
```
