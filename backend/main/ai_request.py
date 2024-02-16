import requests
import json
import warnings

def ai_message(data):
	warnings.filterwarnings('ignore', message='Unverified HTTPS request')
# Set the URL and payload for OAuth token request
	oauth_url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
	oauth_payload = {'scope': 'GIGACHAT_API_PERS'}
	oauth_headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Accept': 'application/json',
		'RqUID': 'eb1c7911-998f-4720-91d8-e5177c943f5d',
		'Authorization': 'Basic ZWIxYzc5MTEtOTk4Zi00NzIwLTkxZDgtZTUxNzdjOTQzZjVkOmZjMzhlOGVjLWZmNDYtNGZjZC1iN2E5LTdhYmU5Y2RiNDA4YQ=='
	}

	# Make OAuth token request
	oauth_response = requests.post(oauth_url, headers=oauth_headers, data=oauth_payload,verify=False)

	# Extract access token
	access_token = oauth_response.json()['access_token']

	# Set the URL and payload for chat completion request
	chat_completion_url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
	chat_completion_payload = {
		"model": "GigaChat:latest",
		"messages": [{"role": "user", "content": f"{data}"}],
		"temperature": 1,
		"top_p": 0.1,
		"n": 1,
		"stream": False,
		"max_tokens": 512,
		"repetition_penalty": 1
	}
	chat_completion_headers = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
		'Authorization': f'Bearer {access_token}'
	}

	# Make chat completion request
	chat_completion_response = requests.post(chat_completion_url, headers=chat_completion_headers, data=json.dumps(chat_completion_payload), verify=False)

	# Print the response
	message_from_ai =chat_completion_response.json()['choices'][0]['message']['content']
	return message_from_ai