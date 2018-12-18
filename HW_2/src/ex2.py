import numpy as np


pi = np.array([1./2, 1./2])
A = np.array([[.4, .6],
              [.6, .4]])
phi = np.array([[.3, .7],
                [.8, .2]])


def exa(O):
    a = np.zeros((len(O), len(pi)))
    b = np.ones((len(O), len(pi)))

    a[0, :] = pi[:] * phi[:, O[0]]
    for i in range(1, len(a)):
        a[i, :] = phi[:, O[i]] * (a[i - 1, :] @ A)
    print(a.T)

    for i in reversed(range(len(b) - 1)):
        b[i, :] = np.sum([b[i + 1, j] * phi[j, O[i + 1]] * A[:, j]
                          for j in range(len(pi))], axis=0)
    print(b.T)

    print(a*b)

    return a, b


def exb(a, b):
    print(a[-1, :].sum())


def zeta(a, b, O, p, n):
    print(b)
    z = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            z[i, j] = a[n-1, i]*phi[j, O[j]]*A[i, j]*b[n, j]/p
    return z


def exc(O_l):
    a_l, b_l = zip(*[exa(o) for o in O_l])
    a, b = a_l[0], b_l[0]

    p_x = sum(a[-1, :] for a in a_l)
    resp = [a*b for a, b in zip(a_l, b_l)]
    resp = np.array([[l/p_x[i] for l in r]for i, r in enumerate(resp)])

    print(resp)
    tot_pi = 0
    for r in range(2):
        for j in range(2):
            tot_pi += resp[r, 0, j]
    new_pi = [sum(resp[r, 0, k] for r in range(2))/tot_pi for k in range(2)]
    print(new_pi)

    tot_A = np.zeros(2)
    for j in range(2):
        for r in range(2):
            for k in range(2):
                for n in range(1, 4):
                    tot_A[j] += zeta(a_l[r], b_l[r], O_l[r], p_x[r], n)[j, k]
    new_A = np.zeros((2, 2))
    for j in range(2):
        for r in range(2):
            for k in range(2):
                for n in range(1, 4):
                    new_A[j, k] += zeta(a_l[r], b_l[r],
                                        O_l[r], p_x[r], n)[j, k]/tot_A[j]

    tot_resp = np.zeros(2)
    for k in range(2):
        for r in range(2):
            for n in range(4):
                tot_resp[k] += resp[r, n, k]
    new_mu = np.zeros(2)
    for k in range(2):
        for r in range(2):
            for n in range(4):
                new_mu[k] += resp[r, n, k] * O_l[r][n]
    for k in range(2):
        new_mu[k] /= tot_resp[k]
    print(new_pi)
    print(new_A)
    print(new_mu)


def main():
    O = [1, 1, 0, 0]  # T, T, H, H
    a, b = exa(O)
    exb(a, b)
    O_l = [[1, 1, 0, 0], [1, 0, 0, 1]]
    exc(O_l)
    pass


if __name__ == "__main__":
    main()
