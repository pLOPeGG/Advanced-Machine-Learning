import numpy as np
from typing import List


def fact(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res


def combi(k, n):
    return fact(n)/fact(k)/fact(n-k)


pi = np.array([0.5, 0.5])
mu = np.array([1./3, 1./2])

data = np.array([[1, 4],
                 [3, 2],
                 [4, 1],
                 [2, 3]])


class Bernouilli:
    def __init__(self, mu: float):
        self.mu = mu

    def p(self, x: np.ndarray):
        return combi(x[0], sum(x)) * self.mu ** x[0] * (1 - self.mu) ** x[1]


class Mixture:
    def __init__(self, pi: np.ndarray, bern_l: List[Bernouilli]):
        self.pi = pi
        self.bern_l = bern_l

    def p_mixt(self, x: np.ndarray):
        return self.pi.dot([b.p(x) for b in self.bern_l])

    def resp(self, x: np.ndarray):
        tot_resp = self.p_mixt(x)
        print(tot_resp, [b.p(x) for b in self.bern_l], sep='\n')
        return np.array([p*bern.p(x)/tot_resp for p, bern
                         in zip(self.pi, self.bern_l)])

    def maxi(self, x_a: np.ndarray):
        resp_a = np.array([self.resp(x) for x in x_a])
        n_a = resp_a.sum(axis=0)

        new_pi = n_a/n_a.sum()
        new_mu = np.array([sum([r * x[0] / sum(x) for r, x in zip(resp, x_a)])
                           for resp in resp_a.T]) / n_a

        print(f"LOG: PREVIOUS_PI={self.pi}",
              f"LOG: PREVIOUS_MU={np.array([b.mu for b in self.bern_l])}",
              sep='\n')

        print(f"LOG: PI={new_pi}",
              f"LOG: MU={new_mu}",
              sep='\n')

        self.pi = new_pi
        self.bern_l = [Bernouilli(mu) for mu in new_mu]


def exa():
    bern_l = [Bernouilli(x) for x in mu]
    mix = Mixture(pi, bern_l)
    for x in data:
        print(x)
        print(mix.resp(x))
        print()


def exb():
    bern_l = [Bernouilli(x) for x in mu]
    mix = Mixture(pi, bern_l)

    mix.maxi(data)


def main():
    print('A')
    exa()
    print('B')
    exb()
    pass


if __name__ == "__main__":
    main()
