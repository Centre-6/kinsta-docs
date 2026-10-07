---
url: "https://api-docs.kinsta.com/api-reference/analytics/get-cdn-bandwidth/"
title: "Get CDN Bandwidth"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "analytics"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:50.470Z"
fetched_at: "2026-10-07T22:58:30Z"
sha256: "469862e419c65eba09fed58fd5c56095cea9e5ae1c308963196157ecdfbe6f34"
body_chars: 7036
extracted_with: "main"
status: "live"
---

# Get CDN Bandwidth

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/analytics/get-cdn-bandwidth/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Query Parameters](#query-parameters)
    - [Response](#response)

---

Get CDN Bandwidth

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth",
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

202

400

401

404

500

```
{
  "analytics": {
    "analytics_response": {
      "key": "cdn-bandwidth",
      "data": [
        {
          "name": "cdn-bandwidth",
          "total": 1000,
          "dataset": [
            {
              "key": "2025-10-28T00:00:00.000Z",
              "value": "1000"
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

cdn-bandwidth

Try it

Get CDN Bandwidth

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth",
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/analytics/cdn-bandwidth")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

202

400

401

404

500

```
{
  "analytics": {
    "analytics_response": {
      "key": "cdn-bandwidth",
      "data": [
        {
          "name": "cdn-bandwidth",
          "total": 1000,
          "dataset": [
            {
              "key": "2025-10-28T00:00:00.000Z",
              "value": "1000"
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

202

application/json

Getting CDN Bandwidth analytics

[​](#response-analytics)

analytics

object

required

Show child attributes
