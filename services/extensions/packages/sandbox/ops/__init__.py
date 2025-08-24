from ..libs.jnt import (
    JntBlenderModule
)
from . import (
    repository_management
)

# -----------------------------------------------------------------------------
class JNT_module(JntBlenderModule):
    """
        JNT feature that manage a sub-set of features
    """
    def get_modules(self):
        return [
            repository_management
        ]
