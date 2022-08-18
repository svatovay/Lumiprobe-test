def is_correct_sequence(input_seq: str) -> bool:
    """
    Check the sequence of "()" for correct.

    :param input_seq:
    :return: bool
    """
    opened_brackets = 0
    for el in input_seq:
        if el == '(':
            opened_brackets += 1
        else:
            if opened_brackets:
                opened_brackets -= 1
            else:
                return False
    return True if not opened_brackets else False


tests = (
    {'test_seq': '(()))',
     'answer': False
     },
    {'test_seq': ')))(((',
     'answer': False
     },
    {'test_seq': '(()())',
     'answer': True
     },
    {'test_seq': '((()())())',
     'answer': True
     },
    {'test_seq': '()()((()()))(()()()()(((())()()()()))',
     'answer': False
     },
    {'test_seq': '()()((()())))(()()()()(((())()()()()))',
     'answer': False
     },
)

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = is_correct_sequence(test['test_seq'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
