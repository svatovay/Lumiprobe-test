def num_sqrt(input_num: int):
    """
    Find integer sqrt if it possible.

    :param input_num:
    :return: int sqrt
    """
    result = input_num ** (1 / 2)
    return int(result) if result.is_integer() else None


tests = (
    {'test_num': 4,
     'answer': 2
     },
    {'test_num': 25,
     'answer': 5
     },
    {'test_num': 71,
     'answer': None
     },
    {'test_num': 9,
     'answer': 3
     },
)

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = num_sqrt(test['test_num'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
