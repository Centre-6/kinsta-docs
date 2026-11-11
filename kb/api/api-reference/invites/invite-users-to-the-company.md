---
url: "https://api-docs.kinsta.com/api-reference/invites/invite-users-to-the-company/"
title: "Invite users to the company"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "invites"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.043Z"
fetched_at: "2026-11-11T13:03:49Z"
sha256: "3b81b291c988788d121ae42f48f5548c4f15ca5f06302612e614cd997d94a45a"
body_chars: 8316
extracted_with: "main"
status: "live"
---

# Invite users to the company

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/invites/invite-users-to-the-company/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Invite users to the company

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{id}/company-invites \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "emails": [
    "[email protected]"
  ],
  "role": "company-admin"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/company-invites"

payload = {
    "emails": ["[email protected]"],
    "role": "company-admin"
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
  body: JSON.stringify({emails: ['[email protected]'], role: 'company-admin'})
};

fetch('https://api.kinsta.com/v2/company/{id}/company-invites', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/company-invites",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'emails' => [
        '[email protected]'
    ],
    'role' => 'company-admin'
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

	url := "https://api.kinsta.com/v2/company/{id}/company-invites"

	payload := strings.NewReader("{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"role\": \"company-admin\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/company/{id}/company-invites")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"role\": \"company-admin\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/company-invites")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"role\": \"company-admin\"\n}"

response = http.request(request)
puts response.read_body
```

202

401

404

500

```
{
  "message": "Inviting users to company in progress",
  "status": 202,
  "operation_id": "company:invite-users-to-company-c3d4e5f6-a7b8-4c9d-8e1f-2a3b4c5d6e7f"
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

company

/

{id}

/

company-invites

Try it

Invite users to the company

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{id}/company-invites \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "emails": [
    "[email protected]"
  ],
  "role": "company-admin"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/company-invites"

payload = {
    "emails": ["[email protected]"],
    "role": "company-admin"
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
  body: JSON.stringify({emails: ['[email protected]'], role: 'company-admin'})
};

fetch('https://api.kinsta.com/v2/company/{id}/company-invites', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/company-invites",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'emails' => [
        '[email protected]'
    ],
    'role' => 'company-admin'
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

	url := "https://api.kinsta.com/v2/company/{id}/company-invites"

	payload := strings.NewReader("{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"role\": \"company-admin\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/company/{id}/company-invites")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"role\": \"company-admin\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/company-invites")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"role\": \"company-admin\"\n}"

response = http.request(request)
puts response.read_body
```

202

401

404

500

```
{
  "message": "Inviting users to company in progress",
  "status": 202,
  "operation_id": "company:invite-users-to-company-c3d4e5f6-a7b8-4c9d-8e1f-2a3b4c5d6e7f"
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

[​](#parameter-id)

id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-emails)

emails

string<email>[]

required

Example:

```
["[email protected]"]
```

[​](#body-role)

role

enum<string>

required

Available options:

`company-admin`,

`company-developer`,

`company-billing`

Example:

`"company-admin"`

#### Response

202

application/json

Invitation sent to the users for the company

[​](#response-message)

message

string

required

Example:

`"Inviting users to company in progress"`

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

`"company:invite-users-to-company-c3d4e5f6-a7b8-4c9d-8e1f-2a3b4c5d6e7f"`
