"""check_system - Tool for checking that a system is ok"""

__version__ = "0.0.1"

from check_system.cli import app
from check_system.lib import add

__all__ = ["add", "app"]
