# Deploy EC2

## requirements
**python**
3.5.3


**pip**

```
pip install -r requirement.txt
```

## Create secret config file

```
project_folder/
	.config_secret/
		settings_common.json
		settings_debug.json
		settings_deploy.json
	.django_app/
	...
	...
...
```

### settings_common.json example

```json
{
  "django": {
    "secret_key": "Django projects secretkey"
  }
}
```

### settings_debug.json example

```json
{
  "django": {
    "allowed_hosts": [
      "*"
    ]
  }
}
```

### settings_deploy.json example

```json
{
  "django": {
    "allowed_hosts": [
      "*"
    ]
  }
}
```

### runserver

```
# local development
python3 manage.py runserver --settings=config.settings.debug
```
