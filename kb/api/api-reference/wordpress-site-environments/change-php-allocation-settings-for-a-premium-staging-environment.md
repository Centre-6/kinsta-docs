---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/change-php-allocation-settings-for-a-premium-staging-environment/"
title: "Change PHP allocation settings for a premium staging environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.627Z"
fetched_at: "2026-10-07T22:41:13Z"
sha256: "cf4e5b03aadf67b4051c2ce57a45d51148f81359c34baac9da2a1254c1883e1d"
body_chars: 8431
extracted_with: "main"
status: "live"
---

# Change PHP allocation settings for a premium staging environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/change-php-allocation-settings-for-a-premium-staging-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Change PHP allocation settings for a premium staging environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "thread_count": 2,
  "thread_memory": 256
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation"

payload = {
    "thread_count": 2,
    "thread_memory": 256
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
  body: JSON.stringify({thread_count: 2, thread_memory: 256})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'thread_count' => 2,
    'thread_memory' => 256
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation"

	payload := strings.NewReader("{\n  \"thread_count\": 2,\n  \"thread_memory\": 256\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"thread_count\": 2,\n  \"thread_memory\": 256\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"thread_count\": 2,\n  \"thread_memory\": 256\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "operation_id": "environments:change-environment-php-allocation-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Environment PHP allocation change in progress",
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

environments

/

{env_id}

/

change-environment-php-allocation

Try it

Change PHP allocation settings for a premium staging environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "thread_count": 2,
  "thread_memory": 256
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation"

payload = {
    "thread_count": 2,
    "thread_memory": 256
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
  body: JSON.stringify({thread_count: 2, thread_memory: 256})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'thread_count' => 2,
    'thread_memory' => 256
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation"

	payload := strings.NewReader("{\n  \"thread_count\": 2,\n  \"thread_memory\": 256\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"thread_count\": 2,\n  \"thread_memory\": 256\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/change-environment-php-allocation")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"thread_count\": 2,\n  \"thread_memory\": 256\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "operation_id": "environments:change-environment-php-allocation-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Environment PHP allocation change in progress",
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

#### Path Parameters

[​](#parameter-env-id)

env_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-thread-count)

thread_count

number

required

Example:

`2`

[​](#body-thread-memory)

thread_memory

number

required

Example:

`256`

#### Response

202

application/json

Environment PHP allocation change action started. Check MyKinsta for status

[​](#response-operation-id)

operation_id

string

required

Example:

`"environments:change-environment-php-allocation-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Environment PHP allocation change in progress"`

[​](#response-status)

status

number

required

Example:

`202`
