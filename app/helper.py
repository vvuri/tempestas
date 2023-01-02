import yaml

from .config import SECRET_FILE


def load_secrets():
    with open(SECRET_FILE) as f:
        return yaml.full_load(f)
