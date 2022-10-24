# Single

Basic strategy with one provider. Proxy on each other provider for Sitri
class.

Hint

Before code with basic usage, I export variable:

PROJECT_A=1

Example:

``` python
from sitri.strategy.single import SingleStrategy
from sitri.contrib.system import SystemConfigProvider

conf = SystemConfigProvider(prefix="project")
strategy = SingleStrategy(conf)

print(strategy.get("a"))
# Output: 1
```
