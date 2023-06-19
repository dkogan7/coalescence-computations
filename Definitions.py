import random

# population size
N1 = 30
# selfing rate
s1 = 1 / N1
# recombination rate selfing
r_s = 1/2
#recombination rate non-selfing
r_d = 1/2

# recombination rate
r1 = (1 - s1) * r_d + s1 * r_s
# states ordering - {}, {1, 1}, {2, 2}, {(1, 1)}, {(2, 2)}, {1, 1, 2, 2}
# {(1, 1), 2, 2}, {1, 1, (2, 2)}, {(1, 2), 1, 2}, {(1, 1), (2, 2)}
# {(1, 2), (1, 2)}, {12, 1, 2}, {(12, 1), 2}, {(12, 2), 1}, {12, (1, 2)}
# {12, 12}, {(12, 12)}


# probabilities are in order of states, the first number represents the order of states
# you can pass the two recombination rates conditioned on selfing
def trans_prob(s, N, r_s, r_d):
    r_b = s * r_s + (1 - s) * r_d
    transition_probabilities = {'{}': (0, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                '{1, 1}': (1, [1 / (2 * N), 1 - 1 / N, 0, 1 / (2 * N), 0, 0,
                                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                '{2, 2}': (2, [1 / (2 * N), 0, 1 - 1 / N, 0, 1 / (2 * N), 0, 0,
                                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                '{(1, 1)}': (3, [s / 2, 1 - s, 0, s / 2, 0, 0, 0, 0,
                                                 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                '{(2, 2)}': (4, [s / 2, 0, 1 - s, 0, s / 2, 0, 0, 0,
                                                 0, 0, 0, 0, 0, 0, 0, 0, 0]),
                                '{1, 1, 2, 2}': (5, [0, 1 / (2 * N), 1 / (2 * N), 0, 0, 1 - 6 / N, 1 / (2 * N),
                                                     1 / (2 * N), 2 / N, 0, 0, 2 / N, 0, 0, 0, 0, 0]),
                                '{(1, 1), 2, 2}': (
                                6, [s / (4 * N), (1 - s) / (2 * N), (s / 2) * (1 - 1 / N), s / (4 * N),
                                    s / (4 * N), (1 - s) * (1 - 5 / N), (s / 2) * (1 - 3 / N),
                                    (1 - s) / (2 * N),
                                    (1 - s) * (2 / N), s / (4 * N), 0, (1 - s) * (2 / N), s / N, 0, 0, 0,
                                    0]),
                                '{1, 1, (2, 2)}': (
                                7, [s / (4 * N), (s / 2) * (1 - 1 / N), (1 - s) / (2 * N), s / (4 * N),
                                    s / (4 * N), (1 - s) * (1 - 5 / N), (1 - s) / (2 * N),
                                    (s / 2) * (1 - 3 / N),
                                    (1 - s) * (2 / N), s / (4 * N), 0, (1 - s) * (2 / N), 0, s / N, 0, 0,
                                    0]),
                                '{(1, 2), 1, 2}': (
                                    8, [0, 1 / (2 * N), 1 / (2 * N), 0, 0, (1 - s) * (1 - 5 / N), (1 - s) / (2 * N),
                                        (1 - s) / (2 * N), (s / 2) * (1 - 3 / N) + (1 - s) * (3 / (2 * N)), 0,
                                        s / (4 * N),
                                        (s / 2) * (1 - 3 / N) + (1 - s) * (3 / (2 * N)), s / (2 * N), s / (2 * N),
                                        s / (2 * N),
                                        s / (4 * N), 0]),
                                '{(1, 1), (2, 2)}': (
                                    9, [s ** 2 / 4, (1 - s) * (s / 2), (1 - s) * (s / 2), s ** 2 / 4, s ** 2 / 4,
                                        (1 - s) ** 2 * (1 - 4 / N), s * (1 - s) / 2 * (1 - 2 / N),
                                        s * (1 - s) / 2 * (1 - 2 / N),
                                        2 * (1 - s) ** 2 / N, s ** 2 / 4 * (1 - 1 / N), 0, 2 * (1 - s) ** 2 / N,
                                        s * (1 - s) / N,
                                        s * (1 - s) / N, 0, 0, s ** 2 / (4 * N)]),
                                '{(1, 2), (1, 2)}': (
                                    10, [s ** 2 / (4 * N), (1 - s ** 2) * (1 / (2 * N)), (1 - s ** 2) * (1 / (2 * N)),
                                         s ** 2 / (4 * N), s ** 2 / (4 * N), (1 - s) ** 2 * (1 - 4 / N),
                                         (1 - s) ** 2 * (1 / (2 * N)),
                                         (1 - s) ** 2 * (1 / (2 * N)), s * (1 - s) * (1 - 2 / N) + (1 - s) ** 2 / N, 0,
                                         s ** 2 / 4 * (1 - 1 / N),
                                         s * (1 - s) * (1 - 2 / N) + (1 - s) ** 2 / N, s * (1 - s) / N, s * (1 - s) / N,
                                         s ** 2 / 2 * (1 - 1 / N),
                                         s ** 2 / 4 * (1 - 1 / N), s ** 2 / (4 * N)]),
                                '{12, 1, 2}': (
                                    11, [0, 1 / (2 * N), 1 / (2 * N), 0, 0, 0, 0, 0,
                                         r_b * (1 - 3 / N), 0, r_b / (2 * N),
                                         (1 - r_b) * (1 - 3 / N), 1 / (2 * N), 1 / (2 * N),
                                         1 / (2 * N), (1 - r_b) * (1 / (2 * N)), 0]),
                                '{(12, 1), 2}': (
                                    12,
                                    [s / (4 * N), (1 - s) / (2 * N), (s / 2) * (1 - 1 / N), s / (4 * N), s / (4 * N),
                                     0, 0, 0, r_d * (1 - s) * (1 - 2 / N), 0, r_d * (1 - s) / (2 * N),
                                     (1 - r_d) * (1 - s) * (1 - 2 / N),
                                     (s / 2) * (1 - 1 / N), (1 - s) / (2 * N), (1 - s) / (2 * N),
                                     (1 - r_d) * (1 - s) / (2 * N),
                                     s / (4 * N)]),
                                '{(12, 2), 1}': (
                                    13,
                                    [s / (4 * N), (s / 2) * (1 - 1 / N), (1 - s) / (2 * N), s / (4 * N), s / (4 * N),
                                     0, 0, 0, r_d * (1 - s) * (1 - 2 / N), 0, r_d * (1 - s) / (2 * N),
                                     (1 - r_d) * (1 - s) * (1 - 2 / N),
                                     (1 - s) / (2 * N), (s / 2) * (1 - 1 / N), (1 - s) / (2 * N),
                                     (1 - r_d) * (1 - s) / (2 * N),
                                     s / (4 * N)]),
                                '{12, (1, 2)}': (
                                    14, [s / (4 * N), (1 - s) / (2 * N), (1 - s) / (2 * N), s / (4 * N), s / (4 * N),
                                         0, 0, 0, r_b * (1 - s) * (1 - 2 / N), 0,
                                         r_b * (s / 2) * (1 - 1 / N),
                                         (1 - r_b) * (1 - s) * (1 - 2 / N),
                                         (1 - s) / (2 * N), (1 - s) / (2 * N), (s / 2) * (1 - 1 / N),
                                         (1 - r_b) * (s / 2) * (1 - 1 / N),
                                         s / (4 * N)]),
                                '{12, 12}': (
                                15, [(1 - r_b) ** 2 / (2 * N) + r_b ** 2 / (2 * N),
                                     0, 0, r_b * (1 - r_b) * (1 / N),
                                     r_b * (1 - r_b) * (1 / N), 0, 0, 0, 0, 0, r_b ** 2 * (1 - 1 / N), 0, 0, 0,
                                     2 * r_b * (1 - r_b) * (1 - 1 / N), (1 - r_b) ** 2 * (1 - 1 / N),
                                     (1 - r_b) ** 2 / (2 * N) + r_b ** 2 / (2 * N)]),
                                '{(12, 12)}': (
                                    16,
                                    [r_s ** 2 * s / 2 + (1 - r_s) ** 2 * s / 2, 0, 0, r_s * (1 - r_s) * s,
                                     r_s * (1 - r_s) * s, 0, 0, 0, 0, 0, r_d ** 2 * (1 - s), 0, 0, 0,
                                     2 * r_d * (1 - r_d) * (1 - s), (1 - r_d) ** 2 * (1 - s),
                                     r_s ** 2 * s / 2 + (1 - r_s) ** 2 * s / 2])

                                }
    return transition_probabilities


# In this list each entry represents values for a state. We pick a random number between 0 and 1
# and see which values it falls in between to determine the next randomly generated state


def upper_val(transition_probabilities):
    upper_values = [[0] * 17 for i in range(17)]
    for i in transition_probabilities.keys():
        index = transition_probabilities.get(i)[0]
        probabilities = transition_probabilities.get(i)[1]
        total = 0
        for j in range(len(upper_values[0])):
            total = total + probabilities[j]
            upper_values[index][j] = total
    return upper_values


# run a single simulation and obtain values for T_iT_j, T_i, T_j
def solve_coal(initial_state, upper_values):
    count = 0
    ti = 0
    tj = 0
    curr_state = initial_state
    while curr_state != 0:
        x = random.random()
        j = 0
        while upper_values[curr_state][j] < x:
            j = j + 1
        if curr_state != 1 and curr_state != 3:
            ti = ti + 1
        if curr_state != 2 and curr_state != 4:
            tj = tj + 1
        curr_state = j
        count = count + 1
    return ti, tj, ti * tj


# run the simulation for m trials and return E[T_iT_j], E[T_i], E[T_j] starting at an initial state
# the initial state is an integer from 0 to 16. N is the population size and r_s and r_d are recombination rates

# this is the important method to run trials.
def run_trials(m, initial_state, s, N, r_s, r_d):
    sum_ti = 0
    sum_tj = 0
    sum_ti_tj = 0
    sum_ti_2 = 0
    sum_tj_2 = 0
    t = trans_prob(s, N, r_s, r_d)
    u = upper_val(t)
    for i in range(m):
        ti, tj, ti_tj = solve_coal(initial_state, u)
        sum_ti = sum_ti + ti
        sum_tj = sum_tj + tj
        sum_ti_tj = sum_ti_tj + ti_tj
        sum_ti_2 = sum_ti_2 + (ti ** 2)
        sum_tj_2 = sum_tj_2 + (tj ** 2)
    return sum_ti / m, sum_tj / m, sum_ti_tj / m, sum_ti_2 / m, sum_tj_2 / m
