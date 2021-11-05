import cvxopt
import picos
import numpy as np


class AntiDist:
    """For a given dimension, determine whether a collection of "d"
    d-dimensional states are antidistinguishable."""

    def __init__(self, dim: int, vectors: np.ndarray = None, verbose: bool = False) -> None:
        """Construct problem instance for given dimension.

        Args:
            dim: Dimension of states.
            vectors: Optional argument to supply specific vectors
            verbose: Optional argument for SDP solver verbosity.
        """
        self.dim = dim

        # Keep track of these quantities for the conjecture.
        self.smallest_overlap = float("inf")
        self.largest_overlap = float("-inf")

        # Conjectured upper bound for the overlap of states.
        self.upper_bound = (self.dim - 2) / (self.dim - 1)

        self.vectors = self.generate_random_vectors() if vectors is None else vectors
        self.verbose = verbose

    def generate_random_vectors(self) -> np.ndarray:
        """Return a list of "d" d-dimensional Haar-random vectors.

        Returns:
            An np.ndarray of "d" d-dimensional complex random vectors.
        """
        components = np.random.randn(self.dim*self.dim, 2).view(np.complex128)
        vectors = []
        for v in range(self.dim):
            vectors.append([])
            for c in range(self.dim):
                vectors[v].append(components[v*self.dim + c][0])

            # Normalize vectors.
            vectors[v] = vectors[v]/np.linalg.norm(vectors[v])
        return np.array(vectors)

    @property
    def is_antidistinguishable(self) -> bool:
        """Return whether the states are antidistinguishable.

        Return:
            True if the states are antidistinguishable, False otherwise.
        """
        problem = picos.Problem()

        # States as rows:
        state_mtx = cvxopt.matrix(self.vectors)
        num_states, dim = state_mtx.size[0], state_mtx.size[1]

        # Set up density matrices as problem parameters.
        density_matrices: list[picos.Constant] = []
        for i in range(num_states):
            mtx = (state_mtx[i, :].H * state_mtx[i, :])
            density_matrices.append(picos.Constant("ρ[{}]".format(i), mtx))

        # Set up the Lagrange multiplier matrix.
        y_var = picos.HermitianVariable("Y", (dim, dim))

        # Add constraints:
        problem.add_list_of_constraints([y_var << p for p in density_matrices])

        # Inner product is max: <I, Y> where "I" is the d-dimensional identity operator.
        problem.set_objective("max", "I" | y_var)
        solution = problem.solve(solver="cvxopt", verbosity=self.verbose)

        # Extract the optimal measurements:
        self.measurements = [problem.get_constraint(k).dual for k in range(num_states)]

        # Compute the error rate. Value > 0 indicates not antidistinguishable.
        self.sdp_val = solution.value
        return True if np.isclose(self.sdp_val, 0) else False

    @property
    def is_inequality_satisfied(self) -> bool:
        """The anti-distinguishability conjecture states that for |ρ_1>, ...,
        |ρ_d> pure states, if |<ρ_i|ρ_j>| ≤ (d − 2)/(d − 1) for all i != j, then
        the states are anti-distinguishable.

        Returns:
            True if the conjecture is satisfied, False otherwise.
        """
        self.smallest_overlap = float("inf")
        self.largest_overlap = float("-inf")
        for i, _ in enumerate(self.vectors):
            for j, _ in enumerate(self.vectors):
                if i != j:

                    ip_val = np.abs(np.trace(self.vectors[i].conj().T * self.vectors[j].reshape(-1,1)))

                    # Retain the smallest and largest overlap of states.
                    self.smallest_overlap = min(self.smallest_overlap, ip_val)
                    self.largest_overlap = max(self.largest_overlap, ip_val)
                    
                    # If |<ρ_i|ρ_j>| > (d − 2)/(d − 1) for some i != j, return
                    # False.
                    if ip_val > self.upper_bound:
                        return False
        return True

    @property
    def is_conjecture_violated(self) -> bool:
        """Check if the antidistinguishability conjecture is satisfied.

        Returns:
            True if the conjecture is violated, False otherwise.
        """
        # The conjecture states that if the inequality is satisfied, then the
        # states are antidistinguishable. If we find a violation of this fact
        # then we have a violation of the conjecture.
        return self.is_inequality_satisfied and not self.is_antidistinguishable
