---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-domains/delete-one-or-more-site-domains/"
title: "Delete one or more site domains"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-domains"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.786Z"
fetched_at: "2026-11-11T13:04:07Z"
sha256: "7a8240a1ba3a9987ba599f04fc0eeb49ef2a730eaf069b40170ff4a95720b2d7"
body_chars: 8791
extracted_with: "main"
status: "live"
---

# Delete one or more site domains

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-domains/delete-one-or-more-site-domains/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Delete one or more site domains

cURL

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/domains \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "domain_ids": [
    "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "3b2b80af-576c-4fdc-ba4f-b596c83f15a1"
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/domains"

payload = { "domain_ids": ["54fb80af-576c-4fdc-ba4f-b596c83f15a1", "3b2b80af-576c-4fdc-ba4f-b596c83f15a1"] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'DELETE',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({
    domain_ids: ['54fb80af-576c-4fdc-ba4f-b596c83f15a1', '3b2b80af-576c-4fdc-ba4f-b596c83f15a1']
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/domains', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/domains",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_POSTFIELDS => json_encode([
    'domain_ids' => [
        '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
        '3b2b80af-576c-4fdc-ba4f-b596c83f15a1'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/domains"

	payload := strings.NewReader("{\n  \"domain_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n    \"3b2b80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ]\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.kinsta.com/v2/sites/environments/{env_id}/domains")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"domain_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n    \"3b2b80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/domains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"domain_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n    \"3b2b80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Deleting site domain in progress",
  "status": 202,
  "operation_id": "sites:delete-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

DELETE

/

sites

/

environments

/

{env_id}

/

domains

Try it

Delete one or more site domains

cURL

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/domains \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "domain_ids": [
    "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "3b2b80af-576c-4fdc-ba4f-b596c83f15a1"
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/domains"

payload = { "domain_ids": ["54fb80af-576c-4fdc-ba4f-b596c83f15a1", "3b2b80af-576c-4fdc-ba4f-b596c83f15a1"] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'DELETE',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({
    domain_ids: ['54fb80af-576c-4fdc-ba4f-b596c83f15a1', '3b2b80af-576c-4fdc-ba4f-b596c83f15a1']
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/domains', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/domains",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_POSTFIELDS => json_encode([
    'domain_ids' => [
        '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
        '3b2b80af-576c-4fdc-ba4f-b596c83f15a1'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/domains"

	payload := strings.NewReader("{\n  \"domain_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n    \"3b2b80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ]\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.kinsta.com/v2/sites/environments/{env_id}/domains")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"domain_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n    \"3b2b80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/domains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"domain_ids\": [\n    \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n    \"3b2b80af-576c-4fdc-ba4f-b596c83f15a1\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Deleting site domain in progress",
  "status": 202,
  "operation_id": "sites:delete-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#body-domain-ids)

domain_ids

string[]

required

Example:

```
[  
  "54fb80af-576c-4fdc-ba4f-b596c83f15a1",  
  "3b2b80af-576c-4fdc-ba4f-b596c83f15a1"  
]
```

#### Response

202

application/json

Site domain deletion action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Deleting site domain in progress"`

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

`"sites:delete-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
