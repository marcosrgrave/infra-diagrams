For now, dockerfile has no effect, so do this instead:

```
sudo apt install graphviz
pip install poetry
poetry install --no-root --no-dev
poetry run python3 main.py
```