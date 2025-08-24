from ..libs.jnt import (
    JntBlenderModule
)
from . import (
    menu_topbar
)

# -----------------------------------------------------------------------------
class JNT_module(JntBlenderModule):
    """
        JNT feature that manage a sub-set of features
    """
    def get_modules(self):
        return [
            menu_topbar
        ]
