---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-tools/set-force-https-status/"
title: "Set Force HTTPS status"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-tools"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.080Z"
fetched_at: "2026-10-07T22:41:37Z"
sha256: "0671186db9322b278f21e24eb0a1c6fa3c4f9041a4ef0213b3f9aff83ff0be87"
body_chars: 8395
extracted_with: "main"
status: "live"
---

# Set Force HTTPS status

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-tools/set-force-https-status/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Set Force HTTPS status

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "type": "ENABLED_REDIRECT_TO_PRIMARY"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status"

payload = { "type": "ENABLED_REDIRECT_TO_PRIMARY" }
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
  body: JSON.stringify({type: 'ENABLED_REDIRECT_TO_PRIMARY'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'ENABLED_REDIRECT_TO_PRIMARY'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status"

	payload := strings.NewReader("{\n  \"type\": \"ENABLED_REDIRECT_TO_PRIMARY\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"ENABLED_REDIRECT_TO_PRIMARY\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"ENABLED_REDIRECT_TO_PRIMARY\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

404

500

```
{
  "message": "Updating Force HTTPS status in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "force-https:update-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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
  "message": "Could not find data or the user does not have permissions to retrieve it",
  "status": 404,
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

force-https-status

Try it

Set Force HTTPS status

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "type": "ENABLED_REDIRECT_TO_PRIMARY"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status"

payload = { "type": "ENABLED_REDIRECT_TO_PRIMARY" }
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
  body: JSON.stringify({type: 'ENABLED_REDIRECT_TO_PRIMARY'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'ENABLED_REDIRECT_TO_PRIMARY'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status"

	payload := strings.NewReader("{\n  \"type\": \"ENABLED_REDIRECT_TO_PRIMARY\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"ENABLED_REDIRECT_TO_PRIMARY\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/force-https-status")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"ENABLED_REDIRECT_TO_PRIMARY\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

404

500

```
{
  "message": "Updating Force HTTPS status in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "force-https:update-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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
  "message": "Could not find data or the user does not have permissions to retrieve it",
  "status": 404,
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

[​](#body-type)

type

enum<string>

required

Available options:

`ENABLED_FOR_ALL`,

`ENABLED_REDIRECT_TO_PRIMARY`,

`DISABLED`

Example:

`"ENABLED_REDIRECT_TO_PRIMARY"`

#### Response

202

application/json

Force HTTPS status update for the given environment is in progress

[​](#response-message)

message

string

required

Example:

`"Updating Force HTTPS status in progress. Use the operation_id to check the status."`

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

`"force-https:update-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
