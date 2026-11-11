---
url: "https://api-docs.kinsta.com/api-reference/wordpress-sites/get-site-by-id/"
title: "Get site by ID"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-sites"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.195Z"
fetched_at: "2026-11-11T13:04:57Z"
sha256: "ef7d77fc1d402cb17b6e6ecd17ffb535b8d3bee7d2532059454a470ac9a05cf1"
body_chars: 6923
extracted_with: "main"
status: "live"
---

# Get site by ID

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-sites/get-site-by-id/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Get site by ID

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/{site_id} \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/{site_id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}",
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

	url := "https://api.kinsta.com/v2/sites/{site_id}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/{site_id}")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}")

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
  "site": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "name": "first-site",
    "display_name": "Site Name",
    "company_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "status": "live",
    "environments": [
      {
        "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
        "name": "first-site",
        "display_name": "First site",
        "is_premium": false,
        "is_blocked": false,
        "domains": [
          {
            "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "name": "mydomain.com",
            "type": "live",
            "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
          }
        ],
        "primaryDomain": {
          "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "name": "mydomain.com",
          "type": "live",
          "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
        }
      }
    ]
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

{site_id}

Try it

Get site by ID

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/{site_id} \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/{site_id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}",
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

	url := "https://api.kinsta.com/v2/sites/{site_id}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/{site_id}")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}")

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
  "site": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "name": "first-site",
    "display_name": "Site Name",
    "company_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "status": "live",
    "environments": [
      {
        "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
        "name": "first-site",
        "display_name": "First site",
        "is_premium": false,
        "is_blocked": false,
        "domains": [
          {
            "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "name": "mydomain.com",
            "type": "live",
            "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
          }
        ],
        "primaryDomain": {
          "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "name": "mydomain.com",
          "type": "live",
          "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
        }
      }
    ]
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

[​](#parameter-site-id)

site_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

200

application/json

Successfully found site by ID

[​](#response-site)

site

object

required

Show child attributes
