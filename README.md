# UnlimitedGPT API

[![License](https://img.shields.io/github/license/hieunc229/UnlimitedGPT-API.svg?color=green)](https://github.com/hieunc229/UnlimitedGPT-API/blob/main/LICENSE)
[![Twitter Follow](https://img.shields.io/twitter/follow/hieuSSR.svg?style=social)](https://twitter.com/hieuSSR)

This is a fun project, aim to provides a chat API that is compatible with OpenAI API endpoint, based on [UnlimitedGPT](https://github.com/Sxvxgee/UnlimitedGPT)

## Requirements
- Python, pip installed
- Chrome browser

## Installation

#### 1. Download the repository

```ssh
git clone https://github.com/hieunc229/UnlimitedGPT-API
```

#### 2. Install dependencies with the following command

```ssh
# Windows
pip install UnlimitedGPT -U python-dotenv

# Linux/macOS
pip3 install UnlimitedGPT -U python-dotenv
```

#### 3. Setup configurations

There are 4 options available

- session_token=(your ChatGPT session token, see [Get your session_token](#get-your-session-token) below)
- conversation_id=(your ChatGPT conversation id, see [Get your conversation_id](#get-your-conversation-id) below)
- host=(your host address, `localhost`)
- port=(your server port, `8080`)

Note that your server will be available as `http://host:port` (or `http://localhost:8080` if you leave it as default)

#### 4. Start the server

Run the following command to start the server

```ssh
# Windows
python main.py

# Linux/macOS
python3 main.py
```

It'll take sometimes to start and connect with ChatGPT website.
Wait until you see `Server started at http://host:port`

### Get your session_token
1. Go to https://chat.openai.com/chat and open the developer tools by `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field.

![image](https://user-images.githubusercontent.com/19218518/206170122-61fbe94f-4b0c-4782-a344-e26ac0d4e2a7.png)

### Get your conversation_id
1. Go to https://chat.openai.com/chat
2. Click on any conversation, then take the part of the URL that comes after https://chat.openai.com/c/

Example: The conversation ID in the URL https://chat.openai.com/c/aa4f2349-8090-42a8-b8dc-0d116ce6b712 is aa4f2349-8090-42a8-b8dc-0d116ce6b712

## Usage
When the server has started, a `POST` method is available.

Example request
```
curl http://localhost:8080 \
    -X POST
    -d '{ "messages": [{ "content": "Hello!" }] }'
```

Note that it'll only take the content from the last item of `messages`

### On Gasby's settings:

In case you want to try it on GasbyAI.com, complete setting up the server step above. Then:

1. Choose `Custom Service` from `Provider` option
2. Enter your server endpoint (http://localhost:8080 by default), leave API Key empty
3. Click test to see if it's good



## Disclaimer
This project is not affiliated with OpenAI in any way. Use at your own risk. I am not responsible for any damage caused by this project. Please read the [OpenAI Terms of Service](https://beta.openai.com/terms) before using this project.

## License
This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.