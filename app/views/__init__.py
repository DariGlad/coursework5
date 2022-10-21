from .main import app as main_bp
from .choose import app as choose_bp
from .fight import app as fight_bp
from .errors import app as errors_bp

__all__ = [
    "main_bp",
    "choose_bp",
    "fight_bp",
    "errors_bp"
]
