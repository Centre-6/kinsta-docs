---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-a-plain-environment-no-wordpress-installed/"
title: "Create a plain environment (no WordPress installed)"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.574Z"
fetched_at: "2026-10-07T22:39:58Z"
sha256: "888943e93017cb385feb7ab7d5458b7b88f0c025765214d3aaea4df48c4ac364"
body_chars: 8052
extracted_with: "main"
status: "live"
---

# Create a plain environment (no WordPress installed)

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-a-plain-environment-no-wordpress-installed/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Create a plain environment (no WordPress installed)

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments/plain \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "display_name": "development",
  "is_premium": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments/plain"

payload = {
    "display_name": "development",
    "is_premium": False
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
  body: JSON.stringify({display_name: 'development', is_premium: false})
};

fetch('https://api.kinsta.com/v2/sites/{site_id}/environments/plain', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/environments/plain",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'display_name' => 'development',
    'is_premium' => false
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/environments/plain"

	payload := strings.NewReader("{\n  \"display_name\": \"development\",\n  \"is_premium\": false\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/{site_id}/environments/plain")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"display_name\": \"development\",\n  \"is_premium\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments/plain")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"display_name\": \"development\",\n  \"is_premium\": false\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Creating plain environment in progress",
  "status": 202,
  "operation_id": "environment:clone-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

environments

/

plain

Try it

Create a plain environment (no WordPress installed)

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments/plain \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "display_name": "development",
  "is_premium": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments/plain"

payload = {
    "display_name": "development",
    "is_premium": False
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
  body: JSON.stringify({display_name: 'development', is_premium: false})
};

fetch('https://api.kinsta.com/v2/sites/{site_id}/environments/plain', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/environments/plain",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'display_name' => 'development',
    'is_premium' => false
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/environments/plain"

	payload := strings.NewReader("{\n  \"display_name\": \"development\",\n  \"is_premium\": false\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/{site_id}/environments/plain")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"display_name\": \"development\",\n  \"is_premium\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments/plain")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"display_name\": \"development\",\n  \"is_premium\": false\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Creating plain environment in progress",
  "status": 202,
  "operation_id": "environment:clone-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#body-display-name)

display_name

string

required

Example:

`"development"`

[​](#body-is-premium)

is_premium

boolean

required

Example:

`false`

#### Response

202

application/json

Creating plain environment action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Creating plain environment in progress"`

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

`"environment:clone-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
