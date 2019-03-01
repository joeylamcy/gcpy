from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .core import *
from .grid.horiz import *
from .grid.regrid import *
from .benchmark import *
from .units import *
from . import plot
from . import grid

#try:
#    from . version import __version__
#except ImportError:
#    raise ImportError('gcpy was not properly installed; some functionality '
#                      'may be not work. If installing from source code, '
#                      'please re-install in place by running\n'
#                      '$ pip install -e .'
#                      '\nElse, please reinstall using your package manager.')
