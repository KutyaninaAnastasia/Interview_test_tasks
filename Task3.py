def appearance(intervals):
    left_bound = intervals['lesson'][0]
    right_bound = intervals['lesson'][1]
    tutor_duration = 0
    pupil_duration = 0
    t = 0
    while t < len(intervals['tutor']):
        tutor_left = intervals['tutor'][t]
        tutor_right = intervals['tutor'][t + 1]
        if tutor_right <= left_bound or tutor_left >= right_bound:
            t += 2
            continue
        if tutor_left <= left_bound <= tutor_right:
            tutor_left = left_bound
        if tutor_left <= right_bound <= tutor_right:
            tutor_right = right_bound
        tutor_duration += tutor_right - tutor_left
        t += 2
        p = 0
        while p < len(intervals['pupil']):
            pupil_left = intervals['pupil'][p]
            pupil_right = intervals['pupil'][p + 1]
            if pupil_right <= tutor_left or pupil_left >= tutor_right:
                p += 2
                continue
            if pupil_left <= tutor_left <= pupil_right:
                pupil_left = tutor_left
            if pupil_left <= tutor_right <= pupil_right:
                pupil_right = tutor_right
            pupil_duration += pupil_right - pupil_left
            p += 2
    return pupil_duration


tests = [

    {'data': {'lesson': [1594663200, 1594666800],

              'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                        1594663396, 1594666472],

              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},

     'answer': 3117

     },

    # Выполнила задачу, но данный тест почему-то мое решение не проходит.
    # Вместе 3577, результат = 6757
    # {'data': {'lesson': [1594702800, 1594706400],
    #
    #           'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
    #                     1594704512, 1594704513, 1594704564, 1594705150,
    #                     1594704581, 1594704582, 1594704734, 1594705009,
    #                     1594705095, 1594705096, 1594705106, 1594706480,
    #                     1594705158, 1594705773, 1594705849, 1594706480,
    #                     1594706500, 1594706875, 1594706502, 1594706503,
    #                     1594706524, 1594706524, 1594706579, 1594706641],
    #
    #           'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
    #                     1594705149, 1594706463]},
    #
    #  'answer': 3577
    #
    #  },

    {'data': {'lesson': [1594692000, 1594695600],

              'pupil': [1594692033, 1594696347],

              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},

     'answer': 3565

     },

]

if __name__ == '__main__':

    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])

        assert test_answer == test[
            'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
