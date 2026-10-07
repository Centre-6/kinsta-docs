---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-themes-&-plugins/update-wp-plugin/"
title: "Update WP Plugin"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-themes-&-plugins"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:50.121Z"
fetched_at: "2026-10-07T22:59:02Z"
sha256: "4e6278735fe9962e27475f3c98280e7ef8d73c39f559884fce20220389e512bc"
body_chars: 7846
extracted_with: "main"
status: "live"
---

# Update WP Plugin

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-themes-&-plugins/update-wp-plugin/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Update WP Plugin

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/plugins \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "name": "akismet",
  "update_version": "5.3"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins"

payload = {
    "name": "akismet",
    "update_version": "5.3"
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
  body: JSON.stringify({name: 'akismet', update_version: '5.3'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/plugins', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'name' => 'akismet',
    'update_version' => '5.3'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins"

	payload := strings.NewReader("{\n  \"name\": \"akismet\",\n  \"update_version\": \"5.3\"\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/plugins")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"akismet\",\n  \"update_version\": \"5.3\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/plugins")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"akismet\",\n  \"update_version\": \"5.3\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Updating WordPress plugin in progress",
  "status": 202,
  "operation_id": "wp-plugin:update-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

PUT

/

sites

/

environments

/

{env_id}

/

plugins

Try it

Update WP Plugin

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/plugins \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "name": "akismet",
  "update_version": "5.3"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins"

payload = {
    "name": "akismet",
    "update_version": "5.3"
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
  body: JSON.stringify({name: 'akismet', update_version: '5.3'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/plugins', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'name' => 'akismet',
    'update_version' => '5.3'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/plugins"

	payload := strings.NewReader("{\n  \"name\": \"akismet\",\n  \"update_version\": \"5.3\"\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/plugins")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"akismet\",\n  \"update_version\": \"5.3\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/plugins")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"akismet\",\n  \"update_version\": \"5.3\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Updating WordPress plugin in progress",
  "status": 202,
  "operation_id": "wp-plugin:update-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#body-name)

name

string

required

Example:

`"akismet"`

[​](#body-update-version)

update_version

string

required

Example:

`"5.3"`

#### Response

202

application/json

Updating of plugin started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Updating WordPress plugin in progress"`

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

`"wp-plugin:update-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
