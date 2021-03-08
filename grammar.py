#!/usr/bin/env python3

import os
import openai
from flask import make_response

openai.api_key = os.environ["sk-o5pTpkgbf98UwVBbkzGFpBLscP78wVZfXeeXpyS5"]

GRAMMAR_TRAINING = """My students sent me sentences to correct:
###
1. Tom egg.
2. The kids dog.
3. Everybody shall bring their paper.
4. Maths are a common course.
5. I insure its right.
6. %s
###
I corrected their grammar:
###
1. Tom's egg.
2. The kids' dog.
3. Everybody shall bring his or her paper.
4. Maths is a common course.
5. I ensure it's right.
6. 
"""

def check_grammar(text, length=False):
	"""
	This function responds to a request for /api/grammar/?text=…
	
	:param text:   the text to be checked
	:return:       suggested correction
	"""

	if length:
		estimated_tokens = length
	else:
		estimated_tokens = len(text) / 4 * 1.2

	request = GRAMMAR_TRAINING % text

	response = openai.Completion.create(
		engine="davinci",
		prompt=request,
		temperature=0.3,
		max_tokens=estimated_tokens,
		top_p=1,
		best_of=3,
		frequency_penalty=0.61,
		presence_penalty=0,
		stop=["###"]
	)
	return response