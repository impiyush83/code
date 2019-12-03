import requests


class ThoughtworksHttpClient:
    def __init__(self, input_url, output_url, user_id):
        self.input_url = input_url
        self.output_url = output_url
        self.user_id = user_id

    def get_input(self):
        resp = requests.get(self.input_url, headers=dict(userID=self.user_id))
        return resp.json()

    def send_answer(self, output):
        resp = requests.post(
            self.output_url,
            json=output,
            headers=dict(userID=self.user_id)
        )
        print(resp.status_code)
