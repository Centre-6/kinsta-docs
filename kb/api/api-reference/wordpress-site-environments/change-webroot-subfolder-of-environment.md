---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/change-webroot-subfolder-of-environment/"
title: "Change webroot subfolder of environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.643Z"
fetched_at: "2026-10-07T22:41:15Z"
sha256: "adab3debdc6f951209ac03d31e00bd8537e37402fa5a8124f29c0b4aed7051a6"
body_chars: 9281
extracted_with: "main"
status: "live"
---

# Change webroot subfolder of environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/change-webroot-subfolder-of-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Change webroot subfolder of environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "web_root_subfolder": "/release_v1",
  "clear_all_cache": true,
  "refresh_plugins_and_themes": true
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder"

payload = {
    "web_root_subfolder": "/release_v1",
    "clear_all_cache": True,
    "refresh_plugins_and_themes": True
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
    web_root_subfolder: '/release_v1',
    clear_all_cache: true,
    refresh_plugins_and_themes: true
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'web_root_subfolder' => '/release_v1',
    'clear_all_cache' => true,
    'refresh_plugins_and_themes' => true
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder"

	payload := strings.NewReader("{\n  \"web_root_subfolder\": \"/release_v1\",\n  \"clear_all_cache\": true,\n  \"refresh_plugins_and_themes\": true\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"web_root_subfolder\": \"/release_v1\",\n  \"clear_all_cache\": true,\n  \"refresh_plugins_and_themes\": true\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"web_root_subfolder\": \"/release_v1\",\n  \"clear_all_cache\": true,\n  \"refresh_plugins_and_themes\": true\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "operation_id": "sites:change-webroot-subfolder-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Environment webroot subfolder change in progress",
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

change-webroot-subfolder

Try it

Change webroot subfolder of environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "web_root_subfolder": "/release_v1",
  "clear_all_cache": true,
  "refresh_plugins_and_themes": true
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder"

payload = {
    "web_root_subfolder": "/release_v1",
    "clear_all_cache": True,
    "refresh_plugins_and_themes": True
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
    web_root_subfolder: '/release_v1',
    clear_all_cache: true,
    refresh_plugins_and_themes: true
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'web_root_subfolder' => '/release_v1',
    'clear_all_cache' => true,
    'refresh_plugins_and_themes' => true
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder"

	payload := strings.NewReader("{\n  \"web_root_subfolder\": \"/release_v1\",\n  \"clear_all_cache\": true,\n  \"refresh_plugins_and_themes\": true\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"web_root_subfolder\": \"/release_v1\",\n  \"clear_all_cache\": true,\n  \"refresh_plugins_and_themes\": true\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/change-webroot-subfolder")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"web_root_subfolder\": \"/release_v1\",\n  \"clear_all_cache\": true,\n  \"refresh_plugins_and_themes\": true\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "operation_id": "sites:change-webroot-subfolder-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Environment webroot subfolder change in progress",
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

[​](#body-web-root-subfolder)

web_root_subfolder

string

required

Pattern: `^\/([a-zA-Z0-9_-]+\/?)*$`

Example:

`"/release_v1"`

[​](#body-clear-all-cache)

clear_all_cache

boolean

default:true

Example:

`true`

[​](#body-refresh-plugins-and-themes)

refresh_plugins_and_themes

boolean

default:true

Example:

`true`

#### Response

202

application/json

Environment webroot subfolder change action started. Check MyKinsta for status

[​](#response-operation-id)

operation_id

string

required

Example:

`"sites:change-webroot-subfolder-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Environment webroot subfolder change in progress"`

[​](#response-status)

status

number

required

Example:

`202`
