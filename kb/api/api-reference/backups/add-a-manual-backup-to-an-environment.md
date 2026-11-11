---
url: "https://api-docs.kinsta.com/api-reference/backups/add-a-manual-backup-to-an-environment/"
title: "Add a manual backup to an environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "backups"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:50:00.236Z"
fetched_at: "2026-11-11T13:03:33Z"
sha256: "a151949e322dc96e6f7b362173b0ec359c555b535bb266e39a2c95378d02c9c6"
body_chars: 7852
extracted_with: "main"
status: "live"
---

# Add a manual backup to an environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/backups/add-a-manual-backup-to-an-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Add a manual backup to an environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "tag": "my-awesome-backup"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups"

payload = { "tag": "my-awesome-backup" }
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
  body: JSON.stringify({tag: 'my-awesome-backup'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'tag' => 'my-awesome-backup'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups"

	payload := strings.NewReader("{\n  \"tag\": \"my-awesome-backup\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"tag\": \"my-awesome-backup\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tag\": \"my-awesome-backup\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding a manual backup to environment in progress",
  "status": 202,
  "operation_id": "backups:add-manual-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "support_reference_id": 123456
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

manual-backups

Try it

Add a manual backup to an environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "tag": "my-awesome-backup"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups"

payload = { "tag": "my-awesome-backup" }
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
  body: JSON.stringify({tag: 'my-awesome-backup'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'tag' => 'my-awesome-backup'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups"

	payload := strings.NewReader("{\n  \"tag\": \"my-awesome-backup\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"tag\": \"my-awesome-backup\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/manual-backups")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"tag\": \"my-awesome-backup\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding a manual backup to environment in progress",
  "status": 202,
  "operation_id": "backups:add-manual-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "support_reference_id": 123456
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

[​](#body-tag)

tag

string

default:""

Example:

`"my-awesome-backup"`

#### Response

202

application/json

Creating manual backup action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Adding a manual backup to environment in progress"`

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

`"backups:add-manual-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-support-reference-id)

support_reference_id

number

Example:

`123456`
