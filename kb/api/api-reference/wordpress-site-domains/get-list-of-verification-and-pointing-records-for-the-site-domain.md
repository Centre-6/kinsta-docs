---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-domains/get-list-of-verification-and-pointing-records-for-the-site-domain/"
title: "Get list of verification and pointing records for the site domain"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-domains"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.266Z"
fetched_at: "2026-10-07T22:41:12Z"
sha256: "bc873e57637630ae9da2d1a678fb18175a8f21f024227240ad5bd92f8e70ea81"
body_chars: 7022
extracted_with: "main"
status: "live"
---

# Get list of verification and pointing records for the site domain

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-domains/get-list-of-verification-and-pointing-records-for-the-site-domain/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Get list of verification and pointing records for the site domain

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records",
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

	url := "https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records")

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
  "site_domain": {
    "verification_records": [
      {
        "name": "_acme-challenge.staging.example-site.io",
        "value": "staging.example-site.io.kinstavalidation.app",
        "type": "CNAME"
      }
    ],
    "pointing_records": [
      {
        "name": "staging.example-site.io",
        "value": "192.0.2.10",
        "type": "A"
      },
      {
        "name": "www",
        "value": "staging.example-site.io",
        "type": "CNAME"
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

environments

/

domains

/

{site_domain_id}

/

verification-records

Try it

Get list of verification and pointing records for the site domain

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records",
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

	url := "https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/domains/{site_domain_id}/verification-records")

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
  "site_domain": {
    "verification_records": [
      {
        "name": "_acme-challenge.staging.example-site.io",
        "value": "staging.example-site.io.kinstavalidation.app",
        "type": "CNAME"
      }
    ],
    "pointing_records": [
      {
        "name": "staging.example-site.io",
        "value": "192.0.2.10",
        "type": "A"
      },
      {
        "name": "www",
        "value": "staging.example-site.io",
        "type": "CNAME"
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

[​](#parameter-site-domain-id)

site_domain_id

string<uuid>

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

200

application/json

Response object of verification and pointing records requests

[​](#response-site-domain)

site_domain

object

required

Show child attributes
