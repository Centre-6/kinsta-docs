---
url: "https://api-docs.kinsta.com/api-reference/company-users/get-list-of-company-users/"
title: "Get list of company users"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "company-users"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.242Z"
fetched_at: "2026-10-07T22:41:03Z"
sha256: "87e9177a46413f9775b8708c7e14a4c061c36636137f3fe5c2010636f4ff1f96"
body_chars: 6512
extracted_with: "main"
status: "live"
---

# Get list of company users

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/company-users/get-list-of-company-users/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Get list of company users

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/users \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/users"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/company/{id}/users', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/users",
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

	url := "https://api.kinsta.com/v2/company/{id}/users"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/company/{id}/users")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/users")

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
    "users": [
      {
        "user": {
          "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "email": "[email protected]",
          "image": "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
          "full_name": "John Doe",
          "type_2fa": "email"
        },
        "capabilities": [
          {
            "id": "9c1f7b2e-3d4a-4f5b-8c6d-1e2f3a4b5c6d",
            "type": "company",
            "role": "company-admin",
            "company_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
          }
        ]
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

company

/

{id}

/

users

Try it

Get list of company users

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/users \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/users"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/company/{id}/users', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/users",
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

	url := "https://api.kinsta.com/v2/company/{id}/users"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/company/{id}/users")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/users")

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
    "users": [
      {
        "user": {
          "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "email": "[email protected]",
          "image": "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
          "full_name": "John Doe",
          "type_2fa": "email"
        },
        "capabilities": [
          {
            "id": "9c1f7b2e-3d4a-4f5b-8c6d-1e2f3a4b5c6d",
            "type": "company",
            "role": "company-admin",
            "company_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "site_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
          }
        ]
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

[​](#parameter-id)

id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

200

application/json

List of company users

[​](#response-company)

company

object

required

Show child attributes
