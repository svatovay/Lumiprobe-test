from collections import Counter


def symbol_counter(input_str: str) -> tuple:
    """
    Find the most frequent symbol.

    :param input_str:
    :return: tuple with symbol and count of occurrences
    """
    return Counter(input_str.lower()).most_common(1)[0]


tests = (
    {'test_str': 'aaaAAAbc',
     'answer': [('a', 6)]
     },
    {'test_str': 'RqRweHHrRT',
     'answer': [('r', 4)]
     },
    {'test_str': 'YrrbGtysdY',
     'answer': [('y', 3)]
     },
    {'test_str': 'AcawcmiMo',
     'answer': [('a', 2), ('m', 2), ('c', 2)]
     },
)

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = symbol_counter(test['test_str'])
        assert test_answer in test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
