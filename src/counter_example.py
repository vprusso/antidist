"""Counterexample of antidistinguishability conjecture from arXiv:XX."""
from antidist import AntiDist
import numpy as np


if __name__ == "__main__":
    dim = 4
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
