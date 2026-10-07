---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-tools/get-list-of-denied-ips/"
title: "Get list of denied IPs"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-tools"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.018Z"
fetched_at: "2026-10-07T22:40:16Z"
sha256: "8161af8e244d1ffa1c77ddfbddd37cbf5dd9e04e59d72e07d177fe6b5fe1b195"
body_chars: 5388
extracted_with: "main"
status: "live"
---

# Get list of denied IPs

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-tools/get-list-of-denied-ips/

## On this page

    - [Authorizations](#authorizations)
    - [Query Parameters](#query-parameters)
    - [Response](#response)

---

Get list of denied IPs

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/tools/denied-ips \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/denied-ips"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/tools/denied-ips', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/tools/denied-ips",
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

	url := "https://api.kinsta.com/v2/sites/tools/denied-ips"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/tools/denied-ips")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/denied-ips")

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
  "environment": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "ip_list": [
      "127.0.0.1",
      "128.0.0.1/32",
      "2001:0db8:0a0b:12f0:0000:0000:0000:0001"
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

sites

/

tools

/

denied-ips

Try it

Get list of denied IPs

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/tools/denied-ips \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/denied-ips"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/tools/denied-ips', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/tools/denied-ips",
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

	url := "https://api.kinsta.com/v2/sites/tools/denied-ips"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/tools/denied-ips")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/denied-ips")

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
  "environment": {
    "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "ip_list": [
      "127.0.0.1",
      "128.0.0.1/32",
      "2001:0db8:0a0b:12f0:0000:0000:0000:0001"
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

#### Query Parameters

[​](#parameter-environment-id)

environment_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

200

application/json

Returns list of denied IPs

[​](#response-environment)

environment

object

required

Show child attributes
