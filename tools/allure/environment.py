import sys

from config import settings
import platform


def create_allure_environment_file():
    os_info = f'{platform.system()}, {platform.release()}'
    python_version = f'{sys.version}'

    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    items.append(f"os_info={os_info}")
    items.append(f"python_version={python_version}")
    properties = '\n'.join(items)


    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
