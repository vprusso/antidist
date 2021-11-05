from src.antidist import AntiDist

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Antidistinguishability.")
    parser.add_argument("-d", help="Dimension of pure states.")
    parser.add_argument("-i", help="Number of total iterations to perform.")
    args = parser.parse_args()

    dim, iters = int(args.d), int(args.i)

    for i in range(iters):
        ad = AntiDist(dim)
        print(f"Iteration {i+1} out of {iters}. Is antidistinguishable: {ad.is_antidistinguishable} -- Is violated: {ad.is_conjecture_violated}")

