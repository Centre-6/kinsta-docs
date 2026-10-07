---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-themes-&-plugins/get-list-of-wp-site-themes/"
title: "Get list of WP Site themes"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-themes-&-plugins"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.207Z"
fetched_at: "2026-10-07T22:41:32Z"
sha256: "91579d4ad10634432e2a6d214b32c6d8ac62eb8f8cd178994aa6ff4b21bdc788"
body_chars: 8733
extracted_with: "main"
status: "live"
---

# Get list of WP Site themes

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-themes-&-plugins/get-list-of-wp-site-themes/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Get list of WP Site themes

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "status": "active",
  "column": "updatesAvailable"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes"

payload = {
    "status": "active",
    "column": "updatesAvailable"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'GET',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({status: 'active', column: 'updatesAvailable'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_POSTFIELDS => json_encode([
    'status' => 'active',
    'column' => 'updatesAvailable'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes"

	payload := strings.NewReader("{\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "environment": {
    "themes": {
      "items": [
        {
          "name": "twentytwentythree",
          "title": "Twenty Twenty Three",
          "status": "active",
          "version": "1.0.0",
          "update": "available",
          "update_version": "1.0.1",
          "update_status": "updated",
          "is_version_vulnerable": false,
          "is_update_version_vulnerable": false,
          "auto_update_type": "Kinsta Automatic Update"
        }
      ],
      "last_updated_at": "2026-01-01T12:00:00.000Z"
    }
  }
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
  "message": "Could not find data or the user does not have permissions to retrieve it",
  "status": 404,
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

GET

/

sites

/

environments

/

{env_id}

/

wp-themes

Try it

Get list of WP Site themes

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "status": "active",
  "column": "updatesAvailable"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes"

payload = {
    "status": "active",
    "column": "updatesAvailable"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.get(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'GET',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({status: 'active', column: 'updatesAvailable'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_POSTFIELDS => json_encode([
    'status' => 'active',
    'column' => 'updatesAvailable'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes"

	payload := strings.NewReader("{\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}")

	req, _ := http.NewRequest("GET", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/wp-themes")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "environment": {
    "themes": {
      "items": [
        {
          "name": "twentytwentythree",
          "title": "Twenty Twenty Three",
          "status": "active",
          "version": "1.0.0",
          "update": "available",
          "update_version": "1.0.1",
          "update_status": "updated",
          "is_version_vulnerable": false,
          "is_update_version_vulnerable": false,
          "auto_update_type": "Kinsta Automatic Update"
        }
      ],
      "last_updated_at": "2026-01-01T12:00:00.000Z"
    }
  }
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
  "message": "Could not find data or the user does not have permissions to retrieve it",
  "status": 404,
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

[​](#body-status)

status

enum<string>

Available options:

`active`,

`inactive`

Example:

`"active"`

[​](#body-column)

column

enum<string>

Available options:

`vulnerable`,

`updatesAvailable`

Example:

`"updatesAvailable"`

#### Response

200

application/json

Successfully found WP themes

[​](#response-environment)

environment

object

required

Show child attributes
