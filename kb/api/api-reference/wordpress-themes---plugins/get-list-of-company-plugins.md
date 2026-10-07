---
url: "https://api-docs.kinsta.com/api-reference/wordpress-themes-&-plugins/get-list-of-company-plugins/"
title: "Get list of company plugins"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-themes-&-plugins"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:49.307Z"
fetched_at: "2026-10-07T22:59:09Z"
sha256: "4c8200991e9aab1b3b9f21d41d45fc7e56d6e3a54b556e29d8bc412c94b132af"
body_chars: 10615
extracted_with: "main"
status: "live"
---

# Get list of company plugins

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-themes-&-plugins/get-list-of-company-plugins/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Get list of company plugins

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/wp-plugins \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "offset": 0,
  "limit": 30,
  "search": "Elementor",
  "status": "active",
  "column": "updatesAvailable"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/wp-plugins"

payload = {
    "offset": 0,
    "limit": 30,
    "search": "Elementor",
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
  body: JSON.stringify({
    offset: 0,
    limit: 30,
    search: 'Elementor',
    status: 'active',
    column: 'updatesAvailable'
  })
};

fetch('https://api.kinsta.com/v2/company/{id}/wp-plugins', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/wp-plugins",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_POSTFIELDS => json_encode([
    'offset' => 0,
    'limit' => 30,
    'search' => 'Elementor',
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

	url := "https://api.kinsta.com/v2/company/{id}/wp-plugins"

	payload := strings.NewReader("{\n  \"offset\": 0,\n  \"limit\": 30,\n  \"search\": \"Elementor\",\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}")

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
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/company/{id}/wp-plugins")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"offset\": 0,\n  \"limit\": 30,\n  \"search\": \"Elementor\",\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/wp-plugins")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"offset\": 0,\n  \"limit\": 30,\n  \"search\": \"Elementor\",\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "company": {
    "plugins": {
      "total": 15,
      "last_updated_at": "2026-01-01T12:00:00.000Z",
      "items": [
        {
          "name": "elementor",
          "title": "Elementor",
          "description": "Popular page builder.",
          "latest_version": "3.22.1",
          "is_latest_version_vulnerable": false,
          "environment_count": 5,
          "update_count": 2,
          "environments": [
            {
              "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
              "site_display_name": "My Awesome Site",
              "display_name": "Live",
              "plugin_status": "active",
              "plugin_update": "available",
              "plugin_version": "1.0.0",
              "is_plugin_version_vulnerable": false,
              "plugin_update_version": "1.0.1",
              "is_plugin_update_version_vulnerable": false,
              "plugin_update_status": "updated",
              "auto_update_type": "Kinsta Automatic Update"
            }
          ]
        }
      ]
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

company

/

{id}

/

wp-plugins

Try it

Get list of company plugins

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/wp-plugins \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "offset": 0,
  "limit": 30,
  "search": "Elementor",
  "status": "active",
  "column": "updatesAvailable"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/wp-plugins"

payload = {
    "offset": 0,
    "limit": 30,
    "search": "Elementor",
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
  body: JSON.stringify({
    offset: 0,
    limit: 30,
    search: 'Elementor',
    status: 'active',
    column: 'updatesAvailable'
  })
};

fetch('https://api.kinsta.com/v2/company/{id}/wp-plugins', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/wp-plugins",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_POSTFIELDS => json_encode([
    'offset' => 0,
    'limit' => 30,
    'search' => 'Elementor',
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

	url := "https://api.kinsta.com/v2/company/{id}/wp-plugins"

	payload := strings.NewReader("{\n  \"offset\": 0,\n  \"limit\": 30,\n  \"search\": \"Elementor\",\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}")

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
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/company/{id}/wp-plugins")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"offset\": 0,\n  \"limit\": 30,\n  \"search\": \"Elementor\",\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/wp-plugins")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"offset\": 0,\n  \"limit\": 30,\n  \"search\": \"Elementor\",\n  \"status\": \"active\",\n  \"column\": \"updatesAvailable\"\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "company": {
    "plugins": {
      "total": 15,
      "last_updated_at": "2026-01-01T12:00:00.000Z",
      "items": [
        {
          "name": "elementor",
          "title": "Elementor",
          "description": "Popular page builder.",
          "latest_version": "3.22.1",
          "is_latest_version_vulnerable": false,
          "environment_count": 5,
          "update_count": 2,
          "environments": [
            {
              "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
              "site_display_name": "My Awesome Site",
              "display_name": "Live",
              "plugin_status": "active",
              "plugin_update": "available",
              "plugin_version": "1.0.0",
              "is_plugin_version_vulnerable": false,
              "plugin_update_version": "1.0.1",
              "is_plugin_update_version_vulnerable": false,
              "plugin_update_status": "updated",
              "auto_update_type": "Kinsta Automatic Update"
            }
          ]
        }
      ]
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

[​](#parameter-id)

id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-offset)

offset

number

Example:

`0`

[​](#body-limit)

limit

number

Example:

`30`

[​](#body-search)

search

string

Example:

`"Elementor"`

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

[​](#body-order-by)

order_by

object

Show child attributes

#### Response

200

application/json

List of company plugins

[​](#response-company)

company

object

required

Show child attributes
