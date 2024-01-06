# MPSolve  

Trying to make a proof of the multiplicative persistence conjecture using a formal language.  
The idea is to start by the proof of base 2 and then try to generalize it to other bases.
We can either extend the proof in base 3 and prove that the multiplicative persistennce is 1 more than in base 2 then extends to all other bases.
Or we can prove that the multiplicative persistence in base 3 doesn't have a majoration and then generalize it to all other bases.
I guess that we can use the Solane conjecture for that but I don't know how to use it yet.
```
Neil Sloane mentions a more general conjecture: for any number base b, there exists a constant M(b) such that no integer expressed in this base b has a multiplicative persistence greater than M(b)1.
```  
In our case we define P = 0 as the set of all digits and trying to define all other numbers, the multiplicative persistance is the first P that we can't define using P-1.

### Base 2

#### Define base 2 as a language

```
S -> Z | O | O S
Z -> "0"
O -> "1"
```

#### Define the multiplicative operation (sca : multiplicative anihihilator, sci : multiplicative identity)
```
sca -> O | O S
sci -> Z | O S | T S
```

#### Define the different set of multiplicative persistence (P)

```
Cases for P -> P-1:
P = 0;
Z -> Z
O -> O

P = 1;
Osca -> Z
Osci-> O

P = 2;
Can't create a valid expression with P = 2, all numbers are described by P = 0 or P = 1
```

#### Textual proof

```
In base 2, a number is either P0, which means it is a digit, or it is P1, which means it is either Osca or Osci (Since a number cannot start with a zero), which results in P0.
Osca and Osci define all numbers greater than P0.
Therefore, we have defined all possible numbers in base 2 using P0 and P1.
```

### Other bases

TODO : Make a construction method for base 2 and then generalize it to other bases or prove that it is not possible.

### Notes

Don't mind doing a pull request to improve this proof

### References

[French Wikipedia article on multiplicative persistence](https://fr.wikipedia.org/wiki/Persistance_d%27un_nombre)

[English Wikipedia article on multiplicative persistence](https://en.wikipedia.org/wiki/Persistence_of_a_number)

[Neil Sloane's article on multiplicative persistence](https://www.researchgate.net/publication/280445240_The_Persistence_of_a_Number)

[OEIS article on multiplicative persistence](https://oeis.org/A003001)

[The Multiplicative Persistence Conjecture Is True for Odd Targets (2021 research paper)](https://arxiv.org/abs/2110.04263)

[My older work with friends on this conjecture (french highschool math club article)](https://www.mathenjeans.fr/sites/default/files/comptes-rendus/suite-de-nombres_toulouse-rive-gauche_2018.pdf)