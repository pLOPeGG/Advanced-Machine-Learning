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


def a():
    print(c@d)
    print(c@d@i)
    print(c@d@i@s)
    pass


def b():
    p_d = c@d
    p_i = p_d@i


def main():
    a()
    pass


if __name__ == '__main__':
    main()
