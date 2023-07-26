import json
from dotenv import dotenv_values
from UnlimitedGPT import ChatGPT
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

config = dotenv_values(".env.local") or dotenv_values(".env")

session_token = config["session_token"]
conversation_id = config["conversation_id"]
serverHost = config["host"] or "localhost"
serverPort = config["port"] or "3001"

app = None

def extract_query_params(url):
    # Parse the URL to extract query parameters
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # Convert the query parameters to a dictionary
    params_dict = {
        key: value[0] if len(value) == 1 else value
        for key, value in query_params.items()
    }

    return params_dict


class ChatGPTServer(BaseHTTPRequestHandler):
    def send_message(self, input):
        message = None

        if app != None:
            res = app.send_message(
                message=input,
                input_mode="INSTANT",  # Can be INSTANT or SLOW
                input_delay=0.1,  # Only used when input_mode is set to SLOW
                # continue_generating=True,  # If set to True, it will continue generating the response if the button was presented
            )
            message = res.response
        else:
            message = "Cannot connect to ChatGPT"
        
        dataStr = json.dumps( {"choices": [{"message": {"content": message }}]})
        self.wfile.write(dataStr.encode())

    def set_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        BaseHTTPRequestHandler.end_headers(self)

    def parse_POST(self):
        length = int(self.headers.get("content-length", 0))
        body = self.rfile.read(length)

        return json.loads(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.set_headers()

    def do_POST(self):
        data = self.parse_POST()
        messages = data["messages"]
        # model = data["model"]

        lastItem = messages.pop()

        self.send_response(200)
        self.set_headers()
        self.send_message(lastItem["content"])

    def do_GET(self):
        self.send_response(200)
        self.set_headers()

        params = extract_query_params(self.path)
        self.send_message(params.get("message"))


if __name__ == "__main__":
    webServer = HTTPServer((serverHost, int(serverPort)), ChatGPTServer)

    app = ChatGPT(
        session_token,
        conversation_id=conversation_id,
        proxy=None,
        chrome_args=[],
        disable_moderation=False,
        verbose=False,
        headless=True
    )
    print("Server started at http://%s:%s" % (serverHost, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
