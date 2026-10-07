---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-tools/search-and-replace/"
title: "Search and replace"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-tools"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.097Z"
fetched_at: "2026-10-07T22:41:36Z"
sha256: "59023bd71758647fd29fef0e026444247a6a300b6bce1c653826172e2ee36dfb"
body_chars: 9812
extracted_with: "main"
status: "live"
---

# Search and replace

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-tools/search-and-replace/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Search and replace

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/tools/search-and-replace \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "search": "old-text",
  "replace": "new-text",
  "perform_replacement": false,
  "is_clear_cache": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/search-and-replace"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "search": "old-text",
    "replace": "new-text",
    "perform_replacement": False,
    "is_clear_cache": False
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
    search: 'old-text',
    replace: 'new-text',
    perform_replacement: false,
    is_clear_cache: false
  })
};

fetch('https://api.kinsta.com/v2/sites/tools/search-and-replace', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/tools/search-and-replace",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'search' => 'old-text',
    'replace' => 'new-text',
    'perform_replacement' => false,
    'is_clear_cache' => false
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

	url := "https://api.kinsta.com/v2/sites/tools/search-and-replace"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"search\": \"old-text\",\n  \"replace\": \"new-text\",\n  \"perform_replacement\": false,\n  \"is_clear_cache\": false\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/tools/search-and-replace")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"search\": \"old-text\",\n  \"replace\": \"new-text\",\n  \"perform_replacement\": false,\n  \"is_clear_cache\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/search-and-replace")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"search\": \"old-text\",\n  \"replace\": \"new-text\",\n  \"perform_replacement\": false,\n  \"is_clear_cache\": false\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "operation_id": "environments:search-and-replace-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Search and replace in progress",
  "status": 202
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

tools

/

search-and-replace

Try it

Search and replace

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/tools/search-and-replace \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "search": "old-text",
  "replace": "new-text",
  "perform_replacement": false,
  "is_clear_cache": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/search-and-replace"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "search": "old-text",
    "replace": "new-text",
    "perform_replacement": False,
    "is_clear_cache": False
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
    search: 'old-text',
    replace: 'new-text',
    perform_replacement: false,
    is_clear_cache: false
  })
};

fetch('https://api.kinsta.com/v2/sites/tools/search-and-replace', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/tools/search-and-replace",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'search' => 'old-text',
    'replace' => 'new-text',
    'perform_replacement' => false,
    'is_clear_cache' => false
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

	url := "https://api.kinsta.com/v2/sites/tools/search-and-replace"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"search\": \"old-text\",\n  \"replace\": \"new-text\",\n  \"perform_replacement\": false,\n  \"is_clear_cache\": false\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/tools/search-and-replace")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"search\": \"old-text\",\n  \"replace\": \"new-text\",\n  \"perform_replacement\": false,\n  \"is_clear_cache\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/search-and-replace")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"search\": \"old-text\",\n  \"replace\": \"new-text\",\n  \"perform_replacement\": false,\n  \"is_clear_cache\": false\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "operation_id": "environments:search-and-replace-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Search and replace in progress",
  "status": 202
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

#### Body

application/json

[​](#body-environment-id)

environment_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#body-search)

search

string

required

Example:

`"old-text"`

[​](#body-replace)

replace

string

default:""

required

Example:

`"new-text"`

[​](#body-perform-replacement)

perform_replacement

boolean

default:false

Example:

`false`

[​](#body-is-clear-cache)

is_clear_cache

boolean

default:false

Example:

`false`

#### Response

202

application/json

Search and replace action started. Check MyKinsta for status

[​](#response-operation-id)

operation_id

string

required

Example:

`"environments:search-and-replace-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Search and replace in progress"`

[​](#response-status)

status

number

required

Example:

`202`
