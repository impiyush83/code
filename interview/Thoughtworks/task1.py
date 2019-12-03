from interview.Thoughtworks.HTTPClient import ThoughtworksHttpClient
from interview.Thoughtworks.constants import INPUT_URL, OUTPUT_URL, USER_ID

twclient = ThoughtworksHttpClient(INPUT_URL, OUTPUT_URL, USER_ID)

input_string = twclient.get_input()
print(input_string)
count = len(input_string['text'])
output = dict(output=dict(count=count))
print(output)
twclient.send_answer(output)
