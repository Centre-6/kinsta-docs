---
url: "https://api-docs.kinsta.com/api-reference/wordpress-cdn/clear-site-cdn-cache/"
title: "Clear Site CDN Cache"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-cdn"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.858Z"
fetched_at: "2026-11-11T13:04:01Z"
sha256: "e6ce163eb61351399b08ba63be38f3d153247470de7f4b16390aab30d77efc9c"
body_chars: 8412
extracted_with: "main"
status: "live"
---

# Clear Site CDN Cache

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-cdn/clear-site-cdn-cache/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Clear Site CDN Cache

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/cdn/clear-cache \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "cdn_cache_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/cdn/clear-cache"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "cdn_cache_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
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
    environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    cdn_cache_id: '6ba7b810-9dad-11d1-80b4-00c04fd430c8'
  })
};

fetch('https://api.kinsta.com/v2/sites/cdn/clear-cache', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/cdn/clear-cache",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'cdn_cache_id' => '6ba7b810-9dad-11d1-80b4-00c04fd430c8'
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

	url := "https://api.kinsta.com/v2/sites/cdn/clear-cache"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"cdn_cache_id\": \"6ba7b810-9dad-11d1-80b4-00c04fd430c8\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/cdn/clear-cache")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"cdn_cache_id\": \"6ba7b810-9dad-11d1-80b4-00c04fd430c8\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/cdn/clear-cache")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"cdn_cache_id\": \"6ba7b810-9dad-11d1-80b4-00c04fd430c8\"\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "cdn-cache:clear-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Clearing site CDN cache in progress",
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

cdn

/

clear-cache

Try it

Clear Site CDN Cache

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/cdn/clear-cache \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "cdn_cache_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/cdn/clear-cache"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "cdn_cache_id": "6ba7b810-9dad-11d1-80b4-00c04fd430c8"
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
    environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    cdn_cache_id: '6ba7b810-9dad-11d1-80b4-00c04fd430c8'
  })
};

fetch('https://api.kinsta.com/v2/sites/cdn/clear-cache', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/cdn/clear-cache",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'cdn_cache_id' => '6ba7b810-9dad-11d1-80b4-00c04fd430c8'
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

	url := "https://api.kinsta.com/v2/sites/cdn/clear-cache"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"cdn_cache_id\": \"6ba7b810-9dad-11d1-80b4-00c04fd430c8\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/cdn/clear-cache")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"cdn_cache_id\": \"6ba7b810-9dad-11d1-80b4-00c04fd430c8\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/cdn/clear-cache")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"cdn_cache_id\": \"6ba7b810-9dad-11d1-80b4-00c04fd430c8\"\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "cdn-cache:clear-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Clearing site CDN cache in progress",
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

[​](#body-cdn-cache-id)

cdn_cache_id

string

required

Example:

`"6ba7b810-9dad-11d1-80b4-00c04fd430c8"`

#### Response

202

application/json

Clearing site CDN cache in progress

[​](#response-operation-id)

operation_id

string

required

Example:

`"cdn-cache:clear-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Clearing site CDN cache in progress"`

[​](#response-status)

status

number

required

Example:

`202`
