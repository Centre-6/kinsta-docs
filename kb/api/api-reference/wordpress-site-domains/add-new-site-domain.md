---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-domains/add-new-site-domain/"
title: "Add new site domain"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-domains"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.221Z"
fetched_at: "2026-10-07T22:41:10Z"
sha256: "c68fe1ad0eec377c3b935a879e299af031928351317c4e33872ddde231df80e5"
body_chars: 10212
extracted_with: "main"
status: "live"
---

# Add new site domain

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-domains/add-new-site-domain/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Add new site domain

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/domains \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "domain_name": "<string>",
  "is_wildcardless": true,
  "add_with_www_subdomain": false,
  "setup_type": "quick",
  "custom_ssl_key": "<string>",
  "custom_ssl_cert": "<string>"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/domains"

payload = {
    "domain_name": "<string>",
    "is_wildcardless": True,
    "add_with_www_subdomain": False,
    "setup_type": "quick",
    "custom_ssl_key": "<string>",
    "custom_ssl_cert": "<string>"
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
    domain_name: '<string>',
    is_wildcardless: true,
    add_with_www_subdomain: false,
    setup_type: 'quick',
    custom_ssl_key: '<string>',
    custom_ssl_cert: '<string>'
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/domains', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/domains",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'domain_name' => '<string>',
    'is_wildcardless' => true,
    'add_with_www_subdomain' => false,
    'setup_type' => 'quick',
    'custom_ssl_key' => '<string>',
    'custom_ssl_cert' => '<string>'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/domains"

	payload := strings.NewReader("{\n  \"domain_name\": \"<string>\",\n  \"is_wildcardless\": true,\n  \"add_with_www_subdomain\": false,\n  \"setup_type\": \"quick\",\n  \"custom_ssl_key\": \"<string>\",\n  \"custom_ssl_cert\": \"<string>\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/domains")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"domain_name\": \"<string>\",\n  \"is_wildcardless\": true,\n  \"add_with_www_subdomain\": false,\n  \"setup_type\": \"quick\",\n  \"custom_ssl_key\": \"<string>\",\n  \"custom_ssl_cert\": \"<string>\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/domains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"domain_name\": \"<string>\",\n  \"is_wildcardless\": true,\n  \"add_with_www_subdomain\": false,\n  \"setup_type\": \"quick\",\n  \"custom_ssl_key\": \"<string>\",\n  \"custom_ssl_cert\": \"<string>\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding site domain in progress",
  "status": 202,
  "operation_id": "sites:add-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

domains

Try it

Add new site domain

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/domains \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "domain_name": "<string>",
  "is_wildcardless": true,
  "add_with_www_subdomain": false,
  "setup_type": "quick",
  "custom_ssl_key": "<string>",
  "custom_ssl_cert": "<string>"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/domains"

payload = {
    "domain_name": "<string>",
    "is_wildcardless": True,
    "add_with_www_subdomain": False,
    "setup_type": "quick",
    "custom_ssl_key": "<string>",
    "custom_ssl_cert": "<string>"
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
    domain_name: '<string>',
    is_wildcardless: true,
    add_with_www_subdomain: false,
    setup_type: 'quick',
    custom_ssl_key: '<string>',
    custom_ssl_cert: '<string>'
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/domains', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/domains",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'domain_name' => '<string>',
    'is_wildcardless' => true,
    'add_with_www_subdomain' => false,
    'setup_type' => 'quick',
    'custom_ssl_key' => '<string>',
    'custom_ssl_cert' => '<string>'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/domains"

	payload := strings.NewReader("{\n  \"domain_name\": \"<string>\",\n  \"is_wildcardless\": true,\n  \"add_with_www_subdomain\": false,\n  \"setup_type\": \"quick\",\n  \"custom_ssl_key\": \"<string>\",\n  \"custom_ssl_cert\": \"<string>\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/domains")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"domain_name\": \"<string>\",\n  \"is_wildcardless\": true,\n  \"add_with_www_subdomain\": false,\n  \"setup_type\": \"quick\",\n  \"custom_ssl_key\": \"<string>\",\n  \"custom_ssl_cert\": \"<string>\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/domains")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"domain_name\": \"<string>\",\n  \"is_wildcardless\": true,\n  \"add_with_www_subdomain\": false,\n  \"setup_type\": \"quick\",\n  \"custom_ssl_key\": \"<string>\",\n  \"custom_ssl_cert\": \"<string>\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding site domain in progress",
  "status": 202,
  "operation_id": "sites:add-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#body-domain-name)

domain_name

string

required

[​](#body-is-wildcardless)

is_wildcardless

boolean

default:true

[​](#body-add-with-www-subdomain)

add_with_www_subdomain

boolean

default:false

Cannot be enabled when is_wildcardless is true.

[​](#body-setup-type)

setup_type

enum<string>

default:quick

Available options:

`quick`,

`avoid_downtime`

[​](#body-custom-ssl-key)

custom_ssl_key

string

[​](#body-custom-ssl-cert)

custom_ssl_cert

string

#### Response

202

application/json

Site domain creation action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Adding site domain in progress"`

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

`"sites:add-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
