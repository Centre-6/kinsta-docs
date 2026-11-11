---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-themes-&-plugins/bulk-update-wp-site-plugins/"
title: "Bulk update WP Site plugins"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-themes-&-plugins"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.701Z"
fetched_at: "2026-11-11T13:04:36Z"
sha256: "20be68085ea077acb5e90cfdeb574a6de3e30a990ced98961e3f5eb1e2515884"
body_chars: 8327
extracted_with: "main"
status: "live"
---

# Bulk update WP Site plugins

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-themes-&-plugins/bulk-update-wp-site-plugins/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Bulk update WP Site plugins

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "plugins": [
    {
      "name": "akismet"
    }
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update"

payload = { "plugins": [{ "name": "akismet" }] }
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
  body: JSON.stringify({plugins: [{name: 'akismet'}]})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'plugins' => [
        [
                'name' => 'akismet'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update"

	payload := strings.NewReader("{\n  \"plugins\": [\n    {\n      \"name\": \"akismet\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"plugins\": [\n    {\n      \"name\": \"akismet\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"plugins\": [\n    {\n      \"name\": \"akismet\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "message": "Bulk-updating WordPress plugins in progress",
  "status": 202,
  "operation_id": "wp-plugins:bulk-update-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "support_reference_id": 123456
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

PUT

/

sites

/

environments

/

{env_id}

/

plugins

/

bulk-update

Try it

Bulk update WP Site plugins

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "plugins": [
    {
      "name": "akismet"
    }
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update"

payload = { "plugins": [{ "name": "akismet" }] }
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
  body: JSON.stringify({plugins: [{name: 'akismet'}]})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'plugins' => [
        [
                'name' => 'akismet'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update"

	payload := strings.NewReader("{\n  \"plugins\": [\n    {\n      \"name\": \"akismet\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"plugins\": [\n    {\n      \"name\": \"akismet\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/plugins/bulk-update")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"plugins\": [\n    {\n      \"name\": \"akismet\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "message": "Bulk-updating WordPress plugins in progress",
  "status": 202,
  "operation_id": "wp-plugins:bulk-update-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "support_reference_id": 123456
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

[​](#body-plugins)

plugins

object[]

required

Show child attributes

#### Response

200

application/json

Successfully updated WP plugins

[​](#response-message)

message

string

required

Example:

`"Bulk-updating WordPress plugins in progress"`

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

`"wp-plugins:bulk-update-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-support-reference-id)

support_reference_id

number

Example:

`123456`
