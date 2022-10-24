# Index Priority

Strategy class take providers tuple and in loop requests values by key,
if each other provider in tuple give response strategy pipe this, else
response None.

Hint

In this example I create **data.json**:

> ``` json
> {
>     "test1": "1",
>     "test2": "2",
>     "test3": "3"
> }
> ```

Export three vars in env:

:   PROJECT_TEST1=0

    PROJECT_TEST4=1

    PROJECT_TEST5=2

Example:

``` python
from sitri.strategy.index_priority import IndexPriorityStrategy
from sitri.contrib.system import SystemConfigProvider
from sitri.contrib.json import JsonConfigProvider

system_conf = SystemConfigProvider(prefix="project")
json_conf = JsonConfigProvider()

strategy = IndexPriorityStrategy((json_conf, system_conf))

strategy.get("test1")
# Output: -1

strategy.get("test2")
# Output: 2

strategy.get("test4")
# Output: 1
```
