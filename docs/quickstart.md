---
layout: default
title: 🚀 Quick Start With OctoAPI
nav_order: 1
---

# 🚀 Quick Start With GitHub Pages


## Install with pip

### from package

```shell
pip install OctoAPI
```

### from source

* Run the following command:
  
  ```shell
  pip install -e https://github.com/totaldebug/OctoAPI.git#egg=OctoAPI
  ```

* Add this to requirements.txt or run a requirements export
  
  ```shell
  -e git+https://github.com/totaldebug/octoAPI.git#egg=OctoAPI
  ```

## Include with project

* Go to [OctoAPI Repo](https://github.com/totaldebug/OctoAPI)
* Download a copy into your project folder
* Import as below:
  ```python
  from OctoAPI import OctoAPI
  ```

## Exanple usage

```python
# Import SonarrAPI Class
from OctoAPI import OctoAPI

# You can find your API key in Settings > General.
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Instantiate SonarrAPI Object
octo = OctoAPI(api_key)

# Get electricity meter point
print(octo.electricity_meter_point())
```
