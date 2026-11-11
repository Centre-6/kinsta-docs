---
url: "https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/set-the-bot-protection-level-of-an-environment/"
title: "Set the bot protection level of an environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-bot-protection"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:50:00.273Z"
fetched_at: "2026-11-11T13:04:00Z"
sha256: "bf28bc496bfc2a370dcc6b37a0d0e32990e3538be3a3cf7caa29acf369d26d78"
body_chars: 8847
extracted_with: "main"
status: "live"
---

# Set the bot protection level of an environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-bot-protection/set-the-bot-protection-level-of-an-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Set the bot protection level of an environment

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "level": "block-automations"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level"

payload = { "level": "block-automations" }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'PUT',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({level: 'block-automations'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'level' => 'block-automations'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level"

	payload := strings.NewReader("{\n  \"level\": \"block-automations\"\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"level\": \"block-automations\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"level\": \"block-automations\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Setting a bot protection level in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "environment:set-bot-protection-level-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

PUT

/

sites

/

environments

/

{env_id}

/

bot-protection

/

level

Try it

Set the bot protection level of an environment

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "level": "block-automations"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level"

payload = { "level": "block-automations" }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'PUT',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({level: 'block-automations'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'level' => 'block-automations'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level"

	payload := strings.NewReader("{\n  \"level\": \"block-automations\"\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"level\": \"block-automations\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/bot-protection/level")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"level\": \"block-automations\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Setting a bot protection level in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "environment:set-bot-protection-level-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-level)

level

enum<string>

required

The bot protection tier to apply to the environment:

- `block-malicious-traffic`
  - What it does: Provides essential protection against malicious traffic.
  - Recommended for: Always-on protection from Kinsta.
- `block-automations`
  - What it does: Blocks automated traffic while allowing humans and verified bots.
  - Recommended for: Most sites.
- `challenge-bots`
  - What it does: Challenges suspicious automated requests while allowing legitimate traffic.
  - Recommended for: Sites seeing increased scraping, spam, or suspicious traffic.
- `challenge-everyone`
  - What it does: All unverified traffic is challenged, including humans.
  - Recommended for: Sites under active attack or dealing with sustained abuse.

Available options:

`block-malicious-traffic`,

`block-automations`,

`challenge-bots`,

`challenge-everyone`

Example:

`"block-automations"`

#### Response

202

application/json

Setting the bot protection level started. Use the operation_id to check the status.

[​](#response-message)

message

string

required

Example:

`"Setting a bot protection level in progress. Use the operation_id to check the status."`

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

`"environment:set-bot-protection-level-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
