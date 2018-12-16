import numpy as np

c = np.array([0.4, 0.6])
d = np.array([[0.2, 0.8],
              [0.4, 0.6]])
i = np.array([[0.5, 0.5],
              [0.6, 0.4]])
g = np.array([[0.1, 0.4, 0.5],
              [0.4, 0.4, 0.2],
              [0.3, 0.4, 0.3],
              [0.7, 0.2, 0.1]])
s = np.array([[0.3, 0.7],
              [0.8, 0.2]])


def ex_a():
    print(c@d)
    print(c@d@i)
    print(c@d@i@s)  # this one
    pass


def ex_b():
    p_d = c@d
    p_i = p_d@i

    p_g_knowing_i0 = p_d@g[::2]
    # print('p(G|I=i0) = {}'.format(p_g_knowing_i0))

    p_i0 = (p_d@i)[0]
    p_g_and_i0 = p_g_knowing_i0 * p_i0
    # print('P(G,I=i0) = {}'.format(p_g_and_i0))

    sum_p_g_and_i0 = np.zeros(3)
    for d_i in range(2):
        for c_i in range(2):
            for s_i in range(2):
                sum_p_g_and_i0 += g[2*d_i, :] * i[d_i, 0] * \
                    d[c_i, d_i] * c[c_i] * s[0, s_i]
    print(sum_p_g_and_i0)
    print(sum_p_g_and_i0/sum(sum_p_g_and_i0))
    print(p_i0)


def ex_c():
    sum_p_s_g = 0
    p_g0 = 0
    for c_i in range(2):
        for d_i in range(2):
            for i_i in range(2):
                sum_p_s_g += c[c_i] * d[c_i, d_i] * i[d_i, i_i] * \
                             g[2*d_i+i_i, 0] * s[i_i, :]
                for s_i in range(2):
                    p_g0 += c[c_i] * d[c_i, d_i] * i[d_i, i_i] * \
                            g[2*d_i+i_i, :] * s[i_i, s_i]
    print('P(S, G=g0) = {}'.format(sum_p_s_g))
    print('P(G=g0) = {}'.format(p_g0))
    print('P(S|G=g0) = {}'.format(sum_p_s_g/p_g0[0]))


def main():
    ex_a()
    ex_b()
    ex_c()

    pass


if __name__ == '__main__':
    main()
