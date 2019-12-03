import re

from HTTPClient import ThoughtworksHttpClient
from constants import USER_ID, OUTPUT_URL, INPUT_URL

twclient = ThoughtworksHttpClient(INPUT_URL, OUTPUT_URL, USER_ID)

input_string = twclient.get_input()
print(input_string)
input_string = input_string['text']
ans = 0
ans += len(re.findall('\. ', input_string))
ans += len(re.findall('\?', input_string))
if input_string[-1] == '.':
    ans += 1
output = dict(output=dict(sentenceCount=ans))
print(output)
twclient.send_answer(output)

