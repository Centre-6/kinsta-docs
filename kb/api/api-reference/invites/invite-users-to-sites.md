---
url: "https://api-docs.kinsta.com/api-reference/invites/invite-users-to-sites/"
title: "Invite users to sites"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "invites"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.068Z"
fetched_at: "2026-11-11T13:03:48Z"
sha256: "87b8b75521e872081f2224a02474940fff5bd9048819b035e1e1de128ac8c80d"
body_chars: 9709
extracted_with: "main"
status: "live"
---

# Invite users to sites

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/invites/invite-users-to-sites/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Invite users to sites

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{id}/site-invites \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "emails": [
    "[email protected]"
  ],
  "site_capabilities": [
    {
      "site_id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
      "role": "site-admin"
    }
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/site-invites"

payload = {
    "emails": ["[email protected]"],
    "site_capabilities": [
        {
            "site_id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
            "role": "site-admin"
        }
    ]
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
  body: JSON.stringify({
    emails: ['[email protected]'],
    site_capabilities: [{site_id: 'b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e', role: 'site-admin'}]
  })
};

fetch('https://api.kinsta.com/v2/company/{id}/site-invites', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/site-invites",
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
    'site_capabilities' => [
        [
                'site_id' => 'b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e',
                'role' => 'site-admin'
        ]
    ]
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

	url := "https://api.kinsta.com/v2/company/{id}/site-invites"

	payload := strings.NewReader("{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/company/{id}/site-invites")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/site-invites")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

401

404

500

```
{
  "message": "Inviting users to sites in progress",
  "status": 202,
  "operation_id": "company:invite-users-to-sites-d4e5f6a7-b8c9-4d0e-9f2a-3b4c5d6e7f80"
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

site-invites

Try it

Invite users to sites

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{id}/site-invites \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "emails": [
    "[email protected]"
  ],
  "site_capabilities": [
    {
      "site_id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
      "role": "site-admin"
    }
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/site-invites"

payload = {
    "emails": ["[email protected]"],
    "site_capabilities": [
        {
            "site_id": "b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e",
            "role": "site-admin"
        }
    ]
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
  body: JSON.stringify({
    emails: ['[email protected]'],
    site_capabilities: [{site_id: 'b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e', role: 'site-admin'}]
  })
};

fetch('https://api.kinsta.com/v2/company/{id}/site-invites', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/site-invites",
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
    'site_capabilities' => [
        [
                'site_id' => 'b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e',
                'role' => 'site-admin'
        ]
    ]
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

	url := "https://api.kinsta.com/v2/company/{id}/site-invites"

	payload := strings.NewReader("{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/company/{id}/site-invites")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/site-invites")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"emails\": [\n    \"[email protected]\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"b2c3d4e5-f6a7-4b8c-9d0e-1f2a3b4c5d6e\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

401

404

500

```
{
  "message": "Inviting users to sites in progress",
  "status": 202,
  "operation_id": "company:invite-users-to-sites-d4e5f6a7-b8c9-4d0e-9f2a-3b4c5d6e7f80"
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

[​](#body-site-capabilities)

site_capabilities

object[]

required

Show child attributes

#### Response

202

application/json

Invitation sent to the user for the sites

[​](#response-message)

message

string

required

Example:

`"Inviting users to sites in progress"`

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

`"company:invite-users-to-sites-d4e5f6a7-b8c9-4d0e-9f2a-3b4c5d6e7f80"`
