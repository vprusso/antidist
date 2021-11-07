# Copyright (C) 2021 Vincent Russo
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

import argparse

from src.antidist import AntiDist

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utility to study the antidistinguishability of states.")
    parser.add_argument("-d", help="Dimension of pure states.", required=True, type=int)
    parser.add_argument("-i", help="Number of total iterations to perform.", required=True, type=int)

    args = parser.parse_args()
    dim, iters = args.d, args.i

    for i in range(iters):
        ad = AntiDist(dim)
        print(
            f"Iteration {i+1} out of {iters}. Is antidistinguishable: {ad.is_antidistinguishable} -- Is violated: {ad.is_conjecture_violated}"
        )
