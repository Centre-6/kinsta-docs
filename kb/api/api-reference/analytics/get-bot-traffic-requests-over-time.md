---
url: "https://api-docs.kinsta.com/api-reference/analytics/get-bot-traffic-requests-over-time/"
title: "Get bot traffic requests over time"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "analytics"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T09:49:46.573Z"
fetched_at: "2026-11-11T13:03:09Z"
sha256: "783d5a79085196c437897a3224759b75f6d86d1a590e1f9846d6f26de8cf384b"
body_chars: 7175
extracted_with: "main"
status: "live"
---

# Get bot traffic requests over time

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/analytics/get-bot-traffic-requests-over-time/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Query Parameters](#query-parameters)
    - [Response](#response)

---

Get bot traffic requests over time

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests",
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

400

401

404

500

```
{
  "analytics": {
    "requests_over_time": [
      {
        "traffic_type": "likely_humans",
        "label": "Likely humans",
        "total": 10572,
        "timeline": [
          {
            "date": "2026-09-14T00:00:00.000Z",
            "requests": 5286
          }
        ]
      }
    ]
  }
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

analytics

/

bot-protection

/

requests

Try it

Get bot traffic requests over time

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests",
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/bot-protection/requests")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

400

401

404

500

```
{
  "analytics": {
    "requests_over_time": [
      {
        "traffic_type": "likely_humans",
        "label": "Likely humans",
        "total": 10572,
        "timeline": [
          {
            "date": "2026-09-14T00:00:00.000Z",
            "requests": 5286
          }
        ]
      }
    ]
  }
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

#### Query Parameters

[​](#parameter-time-span)

time_span

enum<string>

default:7_days

Available options:

`24_hours`,

`7_days`,

`30_days`,

`60_days`

Example:

`"30_days"`

[​](#parameter-company-id)

company_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#parameter-one-of-0)

from

string | null

Example:

`"2025-10-20T00:00:00.000Z"`

[​](#parameter-one-of-0)

to

string | null

Example:

`"2025-10-30T00:00:00.000Z"`

#### Response

200

application/json

Getting bot traffic requests analytics

[​](#response-analytics)

analytics

object

required

Show child attributes
