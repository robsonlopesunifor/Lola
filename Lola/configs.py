import pathlib
import sys

from pydantic import BaseSettings

sys.path.append("/app")


class Settings(BaseSettings):
    # Project
    PROJECT_NAME: str = "grand_central"
    PROJECT_VERSION: str = ""
    PROJECT_ROOT: pathlib.Path = pathlib.Path(__file__).parent
    PACT_DIR: str = f"{PROJECT_ROOT.parent}/tests/pacts/"
    DEBUG: bool = False
    BOCUSE_HOST: str
    BOCUSE_PORT: int


settings = Settings()
