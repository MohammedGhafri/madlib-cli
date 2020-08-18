from madlib_cli.madlib import parse,fun_input,read_template,fun_input_test

def test_one():
    expected="""This is a short story of {noun}'s life.

He {verb} to ASAC {adverb} with his family's {noun}. but When he has a conflict with his family, he goes by {noun}.
too bad that he felt {adjective} last {noun} because he went daily by his {noun}.

on the occasion of this short story of {noun}'s life; he still like programming.
"""
    actual=read_template(open('assets/text.txt'))
    assert expected.strip() == actual


def test_two():
    expected=('{noun}{verb}{adverb}{noun}{noun}{adjective}{noun}{noun}{noun}', ['{noun}', '{verb}', '{adverb}', '{noun}', '{noun}', '{adjective}', '{noun}', '{noun}', '{noun}'])
    actual=parse(open('assets/text.txt').read())
    assert expected==actual

def test_three():
    a=('mohammed','trip')
    b="hello mohammed. How was your trip"
    expected=b
    actual=fun_input_test(open('assets/text1.txt').read(),a)
    assert expected==actual

def test_four():
    a=('Drink','milk','brush','teeth','carfully','attention','study')
    b="""Drink your milk then brush your teeth.
carfully, pay attention to your study"""
    expected=b
    actual=fun_input_test(open('assets/text2.txt').read(),a)
    assert expected==actual