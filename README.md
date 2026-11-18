# django-catalog

Standalone Django app that owns the product catalog feature of the TestCap shop.

## Contents

- `Category` and `Product` models
- Product list/detail views and templates
- Admin registration

## URLs

Included by `django-core1` at `/catalog/`:

- `/catalog/` - product list
- `/catalog/<slug>/` - product detail

## Install (development)

```bash
pip install -e .
```

## Tests

Run from the `django-core1` repo:

```bash
python manage.py test catalog
```

This repo knows nothing about orders; `django-orders` depends on it, not the other way around.
