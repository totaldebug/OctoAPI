---
layout: default
title: electricity_meter_point
parent: OctoAPI
nav_order: 4
---

## Summary

Retrieve a meter-point
Retrieve the details of a meter-point.

This endpoint can be used to get the GSP of a given meter-point.

[API Docs](https://developer.octopus.energy/docs/api/#electricity-meter-points)

## Parameters

Required:

- mpan
  - The electricity meter-point’s MPAN.

## Example

```python
electricity_meter_point('MAPN123456789')
```

## Response

```json
{
    "gsp": "_H",
    "mpan": "2000024512368",
    "profile_class": 1
}
```
