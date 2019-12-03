from HTTPClient import ThoughtworksHttpClient
from constants import USER_ID, OUTPUT_URL, INPUT_URL

twclient = ThoughtworksHttpClient(INPUT_URL, OUTPUT_URL, USER_ID)

input_string = twclient.get_input()
print(input_string)
count = len(input_string['text'].split())
output = dict(output=dict(wordCount=count))
print(output)
twclient.send_answer(output)
