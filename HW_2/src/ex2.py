import numpy as np


pi = np.array([1./2, 1./2])
A = np.array([[.4, .6],
              [.6, .4]])
phi = np.array([[.3, .7],
                [.8, .2]])
O = [1, 1, 0, 0]  # T, T, H, H


def exa():
    a = np.zeros((len(O), len(pi)))
    b = np.ones((len(O), len(pi)))

    a[0, :] = pi[:] * phi[:, O[0]]
    for i in range(1, len(a)):
        a[i, :] = phi[:, O[1]] * a[i - 1, :] @ A
    print(a)

    for i in reversed(range(len(b) - 1)):
        b[i, :] = np.sum([b[i + 1, j] * phi[j, O[i + 1]] * A[:, j] for j in range(len(pi))], axis=0)
    print(b)

    print(a*b)

    return a, b


def exb(a, b):
    print(a[-1, :].sum())


def exc(a, b):
    pass


def main():
    a, b = exa()
    exb(a, b)
    pass


if __name__ == "__main__":
    main()
