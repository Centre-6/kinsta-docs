---
url: "https://api-docs.kinsta.com/api-reference/wordpress-cdn/update-cdn-image-optimization/"
title: "Update CDN Image Optimization"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-cdn"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.342Z"
fetched_at: "2026-10-07T22:39:50Z"
sha256: "ea81680982d835d53ebaf92ac4dfb543e309de5220c89c01b07761244f3b5341"
body_chars: 8365
extracted_with: "main"
status: "live"
---

# Update CDN Image Optimization

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-cdn/update-cdn-image-optimization/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Update CDN Image Optimization

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/cdn/image-optimization \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "image_optimization_type": "lossy"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/cdn/image-optimization"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "image_optimization_type": "lossy"
}
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
  body: JSON.stringify({
    environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    image_optimization_type: 'lossy'
  })
};

fetch('https://api.kinsta.com/v2/sites/cdn/image-optimization', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/cdn/image-optimization",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'image_optimization_type' => 'lossy'
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

	url := "https://api.kinsta.com/v2/sites/cdn/image-optimization"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"image_optimization_type\": \"lossy\"\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/cdn/image-optimization")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"image_optimization_type\": \"lossy\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/cdn/image-optimization")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"image_optimization_type\": \"lossy\"\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "cdn:update-image-optimization-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Updating Site Image Optimization in progress",
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

PUT

/

sites

/

cdn

/

image-optimization

Try it

Update CDN Image Optimization

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/cdn/image-optimization \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "image_optimization_type": "lossy"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/cdn/image-optimization"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "image_optimization_type": "lossy"
}
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
  body: JSON.stringify({
    environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    image_optimization_type: 'lossy'
  })
};

fetch('https://api.kinsta.com/v2/sites/cdn/image-optimization', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/cdn/image-optimization",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'image_optimization_type' => 'lossy'
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

	url := "https://api.kinsta.com/v2/sites/cdn/image-optimization"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"image_optimization_type\": \"lossy\"\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/cdn/image-optimization")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"image_optimization_type\": \"lossy\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/cdn/image-optimization")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"image_optimization_type\": \"lossy\"\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "cdn:update-image-optimization-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Updating Site Image Optimization in progress",
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

[​](#body-image-optimization-type)

image_optimization_type

enum<string>

required

Available options:

`off`,

`lossy`,

`lossless`

Example:

`"lossy"`

#### Response

202

application/json

Updating Site Image Optimization in progress

[​](#response-operation-id)

operation_id

string

required

Example:

`"cdn:update-image-optimization-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Updating Site Image Optimization in progress"`

[​](#response-status)

status

number

required

Example:

`202`
