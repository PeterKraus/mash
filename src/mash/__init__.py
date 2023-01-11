import sys
from .main import main
from . import _version

sys.path += sys.modules["mash"].__path__
__version__ = _version.get_versions()["version"]
