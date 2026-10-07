---
url: "https://api-docs.kinsta.com/api-reference/domains/get-list-of-domain-dns-records-by-domain-id/"
title: "Get list of domain DNS records by domain ID"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "domains"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:49.353Z"
fetched_at: "2026-10-07T22:58:43Z"
sha256: "82ba9c270830a685041e6e3b3aaf827f921c01cf4e4b61b983d9f674d6deef13"
body_chars: 5668
extracted_with: "main"
status: "live"
---

# Get list of domain DNS records by domain ID

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/domains/get-list-of-domain-dns-records-by-domain-id/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Get list of domain DNS records by domain ID

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/domains/{domain_id}/dns-records \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/domains/{domain_id}/dns-records', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/domains/{domain_id}/dns-records",
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

	url := "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

401

500

```
{
  "domain": {
    "dns_records": [
      {
        "type": "A",
        "name": "abc.mydomain.com",
        "ttl": 3600,
        "resource_records": [
          {
            "value": "1.1.1.1"
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
  "message": "Error occurred while processing your request",
  "status": 500,
  "data": "<unknown>"
}
```

GET

/

domains

/

{domain_id}

/

dns-records

Try it

Get list of domain DNS records by domain ID

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/domains/{domain_id}/dns-records \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/domains/{domain_id}/dns-records', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/domains/{domain_id}/dns-records",
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

	url := "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

401

500

```
{
  "domain": {
    "dns_records": [
      {
        "type": "A",
        "name": "abc.mydomain.com",
        "ttl": 3600,
        "resource_records": [
          {
            "value": "1.1.1.1"
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

[​](#parameter-domain-id)

domain_id

string<uuid>

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

200

application/json

Response object of domain DNS records requests

[​](#response-domain)

domain

object

required

Show child attributes
