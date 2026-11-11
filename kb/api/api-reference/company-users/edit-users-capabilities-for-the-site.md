---
url: "https://api-docs.kinsta.com/api-reference/company-users/edit-users-capabilities-for-the-site/"
title: "Edit users capabilities for the site"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "company-users"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:58.968Z"
fetched_at: "2026-11-11T13:03:39Z"
sha256: "074452e65a33a34e4fd97f785b4936f008296e28647b03a718ce5acf0b6d5331"
body_chars: 10319
extracted_with: "main"
status: "live"
---

# Edit users capabilities for the site

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/company-users/edit-users-capabilities-for-the-site/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Edit users capabilities for the site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "user_ids": [
    "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
  ],
  "site_capabilities": [
    {
      "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
      "role": "site-admin"
    }
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities"

payload = {
    "user_ids": ["54fb80af-576c-4fdc-ba4f-b596c83f15a1"],
    "site_capabilities": [
        {
            "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
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
    user_ids: ['54fb80af-576c-4fdc-ba4f-b596c83f15a1'],
    site_capabilities: [{site_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1', role: 'site-admin'}]
  })
};

fetch('https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'user_ids' => [
        '54fb80af-576c-4fdc-ba4f-b596c83f15a1'
    ],
    'site_capabilities' => [
        [
                'site_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
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

	url := "https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities"

	payload := strings.NewReader("{\n  \"user_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"user_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"user_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "message": "Users capabilities updated for the site",
  "status": 202,
  "operation_id": "company:set-site-user-capabilities-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

{company_id}

/

users

/

site-capabilities

Try it

Edit users capabilities for the site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "user_ids": [
    "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
  ],
  "site_capabilities": [
    {
      "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
      "role": "site-admin"
    }
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities"

payload = {
    "user_ids": ["54fb80af-576c-4fdc-ba4f-b596c83f15a1"],
    "site_capabilities": [
        {
            "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
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
    user_ids: ['54fb80af-576c-4fdc-ba4f-b596c83f15a1'],
    site_capabilities: [{site_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1', role: 'site-admin'}]
  })
};

fetch('https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'user_ids' => [
        '54fb80af-576c-4fdc-ba4f-b596c83f15a1'
    ],
    'site_capabilities' => [
        [
                'site_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
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

	url := "https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities"

	payload := strings.NewReader("{\n  \"user_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"user_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{company_id}/users/site-capabilities")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"user_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ],\n  \"site_capabilities\": [\n    {\n      \"site_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n      \"role\": \"site-admin\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "message": "Users capabilities updated for the site",
  "status": 202,
  "operation_id": "company:set-site-user-capabilities-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#parameter-company-id)

company_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-user-ids)

user_ids

string[]

required

[​](#body-site-capabilities)

site_capabilities

object[]

required

Show child attributes

#### Response

200

application/json

Users capabilities updated for the site

[​](#response-message)

message

string

required

Example:

`"Users capabilities updated for the site"`

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

`"company:set-site-user-capabilities-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
