---
url: "https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/add-a-bot-protection-exception-rule-to-an-environment/"
title: "Add a bot protection exception rule to an environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-bot-protection"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:50:00.347Z"
fetched_at: "2026-11-11T13:03:52Z"
sha256: "a6ce270d724647b6272bce2a3a26aee0fa48ea6fb47628cd81f81ff7ae71e9fb"
body_chars: 9141
extracted_with: "main"
status: "live"
---

# Add a bot protection exception rule to an environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/add-a-bot-protection-exception-rule-to-an-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Add a bot protection exception rule to an environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "type": "ip",
  "action": "skip",
  "value": "192.0.2.1"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules"

payload = {
    "type": "ip",
    "action": "skip",
    "value": "192.0.2.1"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({type: 'ip', action: 'skip', value: '192.0.2.1'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'ip',
    'action' => 'skip',
    'value' => '192.0.2.1'
  ]),
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <token>",
    "Content-Type: application/json"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules"

	payload := strings.NewReader("{\n  \"type\": \"ip\",\n  \"action\": \"skip\",\n  \"value\": \"192.0.2.1\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"ip\",\n  \"action\": \"skip\",\n  \"value\": \"192.0.2.1\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"ip\",\n  \"action\": \"skip\",\n  \"value\": \"192.0.2.1\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding a bot protection exception rule in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "environment:add-bot-protection-exception-rule-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
```

```
{
  "message": "Bad request format",
  "status": 400,
  "data": "<unknown>"
}
```

```
{
  "message": "No or invalid API key provided to the request",
  "status": 401,
  "data": "<unknown>"
}
```

```
{
  "message": "Error occurred while processing your request",
  "status": 500,
  "data": "<unknown>"
}
```

POST

/

sites

/

environments

/

{env_id}

/

bot-protection

/

exception-rules

Try it

Add a bot protection exception rule to an environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "type": "ip",
  "action": "skip",
  "value": "192.0.2.1"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules"

payload = {
    "type": "ip",
    "action": "skip",
    "value": "192.0.2.1"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({type: 'ip', action: 'skip', value: '192.0.2.1'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'ip',
    'action' => 'skip',
    'value' => '192.0.2.1'
  ]),
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <token>",
    "Content-Type: application/json"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules"

	payload := strings.NewReader("{\n  \"type\": \"ip\",\n  \"action\": \"skip\",\n  \"value\": \"192.0.2.1\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"ip\",\n  \"action\": \"skip\",\n  \"value\": \"192.0.2.1\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/exception-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"ip\",\n  \"action\": \"skip\",\n  \"value\": \"192.0.2.1\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding a bot protection exception rule in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "environment:add-bot-protection-exception-rule-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
```

```
{
  "message": "Bad request format",
  "status": 400,
  "data": "<unknown>"
}
```

```
{
  "message": "No or invalid API key provided to the request",
  "status": 401,
  "data": "<unknown>"
}
```

```
{
  "message": "Error occurred while processing your request",
  "status": 500,
  "data": "<unknown>"
}
```

#### Authorizations

[​](#authorization-authorization)

Authorization

string

header

required

Bearer authentication header of the form `Bearer <token>`, where `<token>` is your auth token.

#### Path Parameters

[​](#parameter-env-id)

env_id

string<uuid>

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-type)

type

enum<string>

required

The attribute the exception rule matches on.

Available options:

`ip`,

`path`,

`user_agent`,

`country`

Example:

`"ip"`

[​](#body-action)

action

enum<string>

required

The action to apply to traffic matching the rule.

Available options:

`skip`,

`challenge`,

`block`

Example:

`"skip"`

[​](#body-value)

value

string

required

The value to match against, based on the selected type.

Minimum string length: `1`

Example:

`"192.0.2.1"`

#### Response

202

application/json

Adding the bot protection exception rule started. Use the operation_id to check the status.

[​](#response-message)

message

string

required

Example:

`"Adding a bot protection exception rule in progress. Use the operation_id to check the status."`

[​](#response-status)

status

number

required

Example:

`202`

[​](#response-operation-id)

operation_id

string

Example:

`"environment:add-bot-protection-exception-rule-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
