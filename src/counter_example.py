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

"""Counterexample of antidistinguishability conjecture from arXiv:2206.08313."""
import numpy as np

from antidist import AntiDist


if __name__ == "__main__":
    dim: int = 4
    vectors = np.array(
        [
            [
                0.50127198 - 0.037607j,
                -0.00698152 - 0.590973j,
                0.08186514 - 0.4497548j,
                -0.01299883 + 0.43458491j,
            ],
            [
                -0.07115345 - 0.27080326j,
                0.82047712 + 0.26320823j,
                0.22105089 - 0.2091996j,
                -0.23575591 - 0.1758769j,
            ],
            [
                0.31360906 + 0.46339313j,
                -0.0465825 - 0.47825017j,
                -0.10470394 - 0.11776404j,
                0.60231515 + 0.26154959j,
            ],
            [
                -0.53532122 - 0.03654632j,
                0.40955941 - 0.15150576j,
                -0.05741386 + 0.23873985j,
                -0.4737113 - 0.48652564j,
            ],
        ]
    )
    ad = AntiDist(dim, vectors)

    print(f"Are the states antidistinguishable: {ad.is_antidistinguishable}")
    print(f"Is inequality satisfied: {ad.is_inequality_satisfied}")
    print(f"Is conjecture violated: {ad.is_conjecture_violated}")
