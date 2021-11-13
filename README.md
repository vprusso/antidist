# antidist

The `antidist` package is a Python toolkit for studying the
antidistinguishability conjecture. This repo contains companion code for the
arXiv:XX note. 

This code provides a counterexample to the conjecture, but it can also be used
to study antidistinguishability more broadly.

### Antidistinguishability Conjecture

The antidistinguishability conjecture was originally stated in [1].
Specifically, from Appendix-C of [1], the conjecture is stated as follows:

> Let |ρ_1>, ..., |ρ_d> be d pure states. If |<ρ_i|ρ_j>| ≤ (d − 2)/(d − 1) for all i != j, then the states are anti-distinguishable.

The conjecture trivially holds for d = 2 and it also holds for d = 3 based on
[2].

The conjecture does not hold for d = 4 as shown in [4].

### Installing

Python 3.9+ is required along with the `poetry` program. To install a virtual
environment with the package along with all dependencies installed, one may run
the following command:

```
poetry install
```

To invoke the virtual environment in the shell, one may run:

```
poetry shell
```
### Usage

The `main.py` script may be run with command line arguments specifying the
dimension of the random pure states as well as the number of random instances to
run.

For instance, if we wish to run 10 random tests when the dimension of the pure
states are equal to 5, we would run the following:

```
>>> python main.py -d 5 -i 10
Iteration 1 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 2 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 3 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 4 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 5 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 6 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 7 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 8 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 9 out of 10. Is antidistinguishable: True -- Is violated: False
Iteration 10 out of 10. Is antidistinguishable: True -- Is violated: False
```

### Examples

The counterexample shown in [4] can be invoked as follows:

```
>>> python src/counter_example.py
Are the states antidistinguishable: False
Is inequality satisfied: True
Is conjecture violated: True
```

### References

```
[1] Havlíček, Vojtěch, and Barrett, Jonathan,
"Simple communication complexity separation from quantum state antidistinguishability",
Physical Review Research 2.1 (2020): 013326.
arXiv:1911.01927

[2] Caves, Carlton, Fuchs, Christopher, Schack, Rüdiger,
"Conditions for compatibility of quantum-state assignments",
Physical Review A 66.6 (2002): 062111.
arXiv:quant-ph/0206110

[3] Bandyopadhyay, Somshubhro, Jain, Rahul, Oppenheim, Jonathan,
Perry, Christopher,
"Conclusive exclusion of quantum states",
Physical Review A 89.2 (2014): 022336.
arXiv:1306.4683

[4] Russo, Vincent and Sikora, Jamie
""
arXiv:XX
```

