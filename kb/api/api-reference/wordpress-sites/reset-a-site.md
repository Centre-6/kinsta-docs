---
url: "https://api-docs.kinsta.com/api-reference/wordpress-sites/reset-a-site/"
title: "Reset a site"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-sites"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.219Z"
fetched_at: "2026-11-11T13:04:58Z"
sha256: "54bea6753b3f1ebe984aab4953ca6c60da773a296e96f7895acddf8e72eee39e"
body_chars: 7620
extracted_with: "main"
status: "live"
---

# Reset a site

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-sites/reset-a-site/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Reset a site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/{site_id}/reset-site \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "admin_password": "vJnFnN-~v)PxF[6k"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/reset-site"

payload = { "admin_password": "vJnFnN-~v)PxF[6k" }
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
  body: JSON.stringify({admin_password: 'vJnFnN-~v)PxF[6k'})
};

fetch('https://api.kinsta.com/v2/sites/{site_id}/reset-site', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/reset-site",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'admin_password' => 'vJnFnN-~v)PxF[6k'
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/reset-site"

	payload := strings.NewReader("{\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/{site_id}/reset-site")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/reset-site")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Reset site in progress",
  "status": 202,
  "operation_id": "sites:reset-site-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
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

{site_id}

/

reset-site

Try it

Reset a site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/{site_id}/reset-site \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "admin_password": "vJnFnN-~v)PxF[6k"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/reset-site"

payload = { "admin_password": "vJnFnN-~v)PxF[6k" }
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
  body: JSON.stringify({admin_password: 'vJnFnN-~v)PxF[6k'})
};

fetch('https://api.kinsta.com/v2/sites/{site_id}/reset-site', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/reset-site",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'admin_password' => 'vJnFnN-~v)PxF[6k'
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/reset-site"

	payload := strings.NewReader("{\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/{site_id}/reset-site")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/reset-site")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Reset site in progress",
  "status": 202,
  "operation_id": "sites:reset-site-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
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

[​](#parameter-site-id)

site_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-admin-password)

admin_password

string

required

Example:

`"vJnFnN-~v)PxF[6k"`

#### Response

202

application/json

Site reset action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Reset site in progress"`

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

`"sites:reset-site-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-support-reference-id)

support_reference_id

number

Example:

`123456`
