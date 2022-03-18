# Copyright (C) 2022 Vincent Russo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Information about antidist and dependencies."""
__all__ = ["about"]

import platform
import sys

from cvxopt import __version__ as cvxopt_version
from numpy import __version__ as numpy_version
from picos import __version__ as picos_version

PYTHON_VERSION = sys.version_info[0:3]


def about() -> None:
    """Displays information about antidist, core/optional packages, and
    Python version/platform information.
    """

    about_str = f"""
antidist: Python package for studying the antidistinguishability conjecture.
==============================================================================
Authored by: Vincent Russo, 2022

Core Dependencies
-----------------
CVXOPT Version:\t{cvxopt_version}
NumPy Version:\t{numpy_version}
Picos Version:\t{picos_version}
Optional Dependencies
---------------------
Python Version:\t{PYTHON_VERSION[0]}.{PYTHON_VERSION[1]}.{PYTHON_VERSION[2]}
Platform Info:\t{platform.system()} ({platform.machine()})"""
    print(about_str)


if __name__ == "__main__":
    about()
