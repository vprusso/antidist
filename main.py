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
