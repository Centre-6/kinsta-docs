---
url: "https://api-docs.kinsta.com/api-reference/analytics/get-cdn-bandwidth-usage/"
title: "Get CDN Bandwidth usage"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "analytics"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.455Z"
fetched_at: "2026-10-07T22:39:29Z"
sha256: "85ca54bd847c78afab2ed7bcaf1ab375cb69f2eff23f1c4f4a8072000d11b62f"
body_chars: 6091
extracted_with: "main"
status: "live"
---

# Get CDN Bandwidth usage

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/analytics/get-cdn-bandwidth-usage/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Get CDN Bandwidth usage

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month",
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month")

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
  "site": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "this_month_cdn_usage": {
      "bandwidth": 100
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

{site_id}

/

usage

/

cdn-bandwidth

/

this-month

Try it

Get CDN Bandwidth usage

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month",
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/usage/cdn-bandwidth/this-month")

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
  "site": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "this_month_cdn_usage": {
      "bandwidth": 100
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

[​](#parameter-site-id)

site_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

200

application/json

Successfully found CDN bandwidth

[​](#response-site)

site

object

required

Show child attributes
