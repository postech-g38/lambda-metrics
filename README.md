# API Gateway + Cognito Metrics Generator

This API is a ``post authentication Lambda trigger`` for Cognito, after every login or access throught API Gateway it will generate a metric on CloudWatch

```bash
# Running Pytest
pytest -s
```
* ensure to use -s argument so the log can be visible
