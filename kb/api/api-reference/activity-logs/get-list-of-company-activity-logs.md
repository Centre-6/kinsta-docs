---
url: "https://api-docs.kinsta.com/api-reference/activity-logs/get-list-of-company-activity-logs/"
title: "Get list of company activity logs"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "activity-logs"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.291Z"
fetched_at: "2026-10-07T22:40:44Z"
sha256: "6fe9cd6021e6d1db992aeba52c617d049c3ccc1c18397400d7c5835e4ab78ef5"
body_chars: 8132
extracted_with: "main"
status: "live"
---

# Get list of company activity logs

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/activity-logs/get-list-of-company-activity-logs/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Query Parameters](#query-parameters)
    - [Response](#response)

---

Get list of company activity logs

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/activity-logs \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/activity-logs"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/company/{id}/activity-logs', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/activity-logs",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <token>"
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.kinsta.com/v2/company/{id}/activity-logs"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/company/{id}/activity-logs")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/activity-logs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

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
    "activity_logs": {
      "items": [
        {
          "id": 34181968,
          "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "created_at": 1665382600770,
          "is_done": true,
          "has_failed": false,
          "has_warning": false,
          "type": "deleteSite",
          "public_error": "The environment is blocked by another process. Please try again a bit later.",
          "ip_address": "203.0.113.42",
          "descriptions": [
            "Delete site \"Test ABC\""
          ],
          "initiated_by": {
            "id": "admin-user",
            "role": "admin",
            "full_name": "Jane",
            "first_name": "Smith"
          },
          "user_agent_info": {
            "browser_name": "Chrome",
            "browser_version": "126.0.0",
            "os_name": "macOS"
          },
          "api_key_info": {
            "id": "cf5b98a0-6fdd-4997-9c1f-e73d566533be",
            "name": "Public API Key"
          }
        }
      ],
      "total": 42
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

activity-logs

Try it

Get list of company activity logs

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/activity-logs \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/activity-logs"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/company/{id}/activity-logs', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/activity-logs",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <token>"
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.kinsta.com/v2/company/{id}/activity-logs"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/company/{id}/activity-logs")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/activity-logs")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

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
    "activity_logs": {
      "items": [
        {
          "id": 34181968,
          "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "created_at": 1665382600770,
          "is_done": true,
          "has_failed": false,
          "has_warning": false,
          "type": "deleteSite",
          "public_error": "The environment is blocked by another process. Please try again a bit later.",
          "ip_address": "203.0.113.42",
          "descriptions": [
            "Delete site \"Test ABC\""
          ],
          "initiated_by": {
            "id": "admin-user",
            "role": "admin",
            "full_name": "Jane",
            "first_name": "Smith"
          },
          "user_agent_info": {
            "browser_name": "Chrome",
            "browser_version": "126.0.0",
            "os_name": "macOS"
          },
          "api_key_info": {
            "id": "cf5b98a0-6fdd-4997-9c1f-e73d566533be",
            "name": "Public API Key"
          }
        }
      ],
      "total": 42
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

#### Query Parameters

[​](#parameter-limit)

limit

number

default:10

Example:

`10`

[​](#parameter-offset)

offset

number

default:0

Example:

`3`

[​](#parameter-category)

category

enum<string>

Available options:

`siteActions`,

`kinstaDns`,

`migrations`,

`billing`,

`notifications`,

`userManagement`,

`personalSettings`,

`samlSso`

Example:

`"siteActions"`

[​](#parameter-site-id)

site_id

string

[​](#parameter-id-initiated-by)

id_initiated_by

string

[​](#parameter-id-api-key)

id_api_key

string

[​](#parameter-language)

language

enum<string>

default:en

Available options:

`da`,

`de`,

`en`,

`es`,

`fr`,

`it`,

`ja`,

`nl`,

`pt`,

`sv`

#### Response

200

application/json

Successfully found activity logs

[​](#response-company)

company

object

required

Show child attributes
