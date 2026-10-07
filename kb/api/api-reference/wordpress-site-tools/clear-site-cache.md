---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-tools/clear-site-cache/"
title: "Clear Site Cache"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-tools"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.968Z"
fetched_at: "2026-10-07T22:40:15Z"
sha256: "4d15fdb6a346768a729d2aa7aaca0e3839f7efe7a81472d1da05d82cea3a6d45"
body_chars: 7419
extracted_with: "main"
status: "live"
---

# Clear Site Cache

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-tools/clear-site-cache/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Clear Site Cache

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/tools/clear-cache \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/clear-cache"

payload = { "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1" }
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
  body: JSON.stringify({environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1'})
};

fetch('https://api.kinsta.com/v2/sites/tools/clear-cache', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/tools/clear-cache",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1'
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

	url := "https://api.kinsta.com/v2/sites/tools/clear-cache"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/tools/clear-cache")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/clear-cache")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "cache:clear-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Clearing site cache in progress",
  "status": 202
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

tools

/

clear-cache

Try it

Clear Site Cache

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/tools/clear-cache \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/clear-cache"

payload = { "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1" }
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
  body: JSON.stringify({environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1'})
};

fetch('https://api.kinsta.com/v2/sites/tools/clear-cache', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/tools/clear-cache",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1'
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

	url := "https://api.kinsta.com/v2/sites/tools/clear-cache"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/tools/clear-cache")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/clear-cache")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "cache:clear-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Clearing site cache in progress",
  "status": 202
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

#### Body

application/json

[​](#body-environment-id)

environment_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

202

application/json

Clearing site cache in progress

[​](#response-operation-id)

operation_id

string

required

Example:

`"cache:clear-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Clearing site cache in progress"`

[​](#response-status)

status

number

required

Example:

`202`
