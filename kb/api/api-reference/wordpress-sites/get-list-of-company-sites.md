---
url: "https://api-docs.kinsta.com/api-reference/wordpress-sites/get-list-of-company-sites/"
title: "Get list of company sites"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-sites"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.462Z"
fetched_at: "2026-10-07T22:40:22Z"
sha256: "b0f36c5e658bd46d3ddfb30fa6f3334e4abf97f899c2612ec9a1e560595782fb"
body_chars: 8770
extracted_with: "main"
status: "live"
---

# Get list of company sites

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-sites/get-list-of-company-sites/

## On this page

    - [Authorizations](#authorizations)
    - [Query Parameters](#query-parameters)
    - [Response](#response)

---

Get list of company sites

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites",
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

	url := "https://api.kinsta.com/v2/sites"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites")

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
    "sites": [
      {
        "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
        "name": "firstsite",
        "display_name": "First site",
        "status": "live",
        "siteLabels": [
          {
            "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "name": "Do not remove"
          }
        ],
        "environments": [
          {
            "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "name": "live",
            "display_name": "Live",
            "is_blocked": false,
            "id_edge_cache": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "cdn_cache_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "is_opt_out_from_automatic_php_update": false,
            "web_root": "/release_v1",
            "image_optimization_type": "lossy",
            "is_additional_sftp_accounts_enabled": false,
            "is_premium": false,
            "wordpress_version": "6.3.1",
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
            },
            "ssh_connection": {
              "ssh_port": "808080",
              "ssh_ip": {
                "external_ip": "1xx.1xx.1xx.1xx"
              }
            },
            "container_info": {
              "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
              "php_engine_version": "php8.3"
            }
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

sites

Try it

Get list of company sites

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites",
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

	url := "https://api.kinsta.com/v2/sites"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites")

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
    "sites": [
      {
        "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
        "name": "firstsite",
        "display_name": "First site",
        "status": "live",
        "siteLabels": [
          {
            "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "name": "Do not remove"
          }
        ],
        "environments": [
          {
            "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "name": "live",
            "display_name": "Live",
            "is_blocked": false,
            "id_edge_cache": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "cdn_cache_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
            "is_opt_out_from_automatic_php_update": false,
            "web_root": "/release_v1",
            "image_optimization_type": "lossy",
            "is_additional_sftp_accounts_enabled": false,
            "is_premium": false,
            "wordpress_version": "6.3.1",
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
            },
            "ssh_connection": {
              "ssh_port": "808080",
              "ssh_ip": {
                "external_ip": "1xx.1xx.1xx.1xx"
              }
            },
            "container_info": {
              "id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
              "php_engine_version": "php8.3"
            }
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

#### Query Parameters

[​](#parameter-company)

company

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#parameter-one-of-0)

include_environments

boolean | null

default:false

Example:

`true`

#### Response

200

application/json

Successfully found sites

[​](#response-company)

company

object

required

Show child attributes
