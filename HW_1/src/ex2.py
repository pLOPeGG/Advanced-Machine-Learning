import numpy as np

c = np.array([3, 7])
d = np.array([[2, 8],
              [3, 7]])
i = np.array([[2, 2],
              [6, 2]])
g = np.array([[1, 4, 5],
              [4, 4, 2],
              [3, 4, 3],
              [7, 2, 1]])
s = np.array([[2, 8],
              [8, 2]])


Z = 0
for c_i in range(2):
    for d_i in range(2):
        for i_i in range(2):
            for g_i in range(3):
                for s_i in range(2):
                    Z += c[c_i] * d[c_i, d_i] * i[d_i, i_i] * \
                         g[d_i*2 + i_i, g_i] * s[i_i, s_i]

print(Z)


def ex_a():
    p_s = np.zeros(2)
    for c_i in range(2):
        for d_i in range(2):
            for i_i in range(2):
                for g_i in range(3):
                    p_s += c[c_i] * d[c_i, d_i] * i[d_i, i_i] * \
                         g[d_i*2 + i_i, g_i] * s[i_i, :]
    p_s /= Z
    print(f'PHI(S) = {p_s*Z}')
    print(f'P(S) = {p_s}')


def ex_b():
    p_g_i0 = np.zeros(3)
    for c_i in range(2):
        for d_i in range(2):
            for s_i in range(2):
                p_g_i0 += c[c_i] * d[c_i, d_i] * i[d_i, 0] * \
                        g[d_i*2 + 0, :] * s[i_i, s_i]
    p_g_i0 /= Z
    p_g_given_i0 = p_g_i0/(sum(p_g_i0))

    print(f'PHI(G,i_0) = {p_g_i0*Z}')
    print(f'PHI(G|i_0) = {p_g_given_i0*Z}')
    print(f'P(G,i_0) = {p_g_i0}')
    print(f'P(G|i_0) = {p_g_given_i0}')


def ex_c():
    p_s_g0 = np.zeros(2)
    for c_i in range(2):
        for d_i in range(2):
            for i_i in range(2):
                p_s_g0 += c[c_i] * d[c_i, d_i] * i[d_i, i_i] * \
                        g[d_i*2 + i_i, 0] * s[i_i, :]
    p_s_g0 /= Z
    p_s_given_g0 = p_s_g0/(sum(p_s_g0))

    print(f'PHI(S,g_0) = {p_s_g0*Z}')
    print(f'PHI(S|g_0) = {p_s_given_g0*Z}')
    print(f'P(S,g_0) = {p_s_g0}')
    print(f'P(S|g_0) = {p_s_given_g0}')


def main():
    ex_a()
    ex_b()
    ex_c()
    pass


if __name__ == '__main__':
    main()