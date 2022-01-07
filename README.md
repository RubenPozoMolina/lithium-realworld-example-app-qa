# lithium-realworld-example-app-qa
Testing lithium-realworld-example-app

## Prepare virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Create config file
```bash
cp config/config.template.ini config/config.ini
```

## Execute tests 
```bash
pytest -s
``` 