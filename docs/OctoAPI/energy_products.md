---
layout: default
title: energy_products
parent: OctoAPI
nav_order: 4
---

## Summary

Retrieve all products
Retrieve the details of a meter-point.

This endpoint can be used to get the GSP of a given meter-point.

[API Docs](https://developer.octopus.energy/docs/api/#electricity-meter-points)

## Parameters

Required:

- mpan
  - The electricity meter-point’s MPAN.

## Example

```python
energy_products()
```

## Response

```json
{
  "count": 108,
  "next": "https://api.octopus.energy/v1/products/?page=2",
  "previous": null,
  "results": [
    {
      "code": "VAR-17-01-11",
      "full_name": "Flexible Octopus January 2017 v1",
      "display_name": "Flexible Octopus",
      "description": "This great value 12 month fixed tariff guarantees…",
      "is_variable": true,
      "is_green": false,
      "is_tracker": false,
      "is_prepay": false,
      "is_business": false,
      "is_restricted": false,
      "term": 12,
      "brand": "OCTOPUS_ENERGY",
      "available_from": "2017-05-05T05:37:27Z",
      "available_to": null,
      "links": [
        {
          "href": "https://api.octopus.energy/v1/products/VAR-17-01-11/",
          "method": "GET",
          "rel": "self"
        }
      ]
    }
  ]
}
```
