from HTTPClient import ThoughtworksHttpClient
from constants import USER_ID, OUTPUT_URL, INPUT_URL

twclient = ThoughtworksHttpClient(INPUT_URL, OUTPUT_URL, USER_ID)

input_string = twclient.get_input()
print(input_string)
ans = dict()

for i in input_string['text'].lower():
    if i in ['a', 'e', 'i', 'o', 'u']:
        if ans.get(i):
            ans[i] += 1
        else:
            ans[i] = 1
output = dict(output=ans)
print(output)
twclient.send_answer(output)
