from pathlib import Path
import yaml


def load_config():
    default_file = Path(__file__).parent / 'config.yaml'
    with open(default_file, 'r') as file:
        config = yaml.safe_load(file)

    return config
