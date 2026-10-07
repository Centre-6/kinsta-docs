---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments/"
title: "Get site environments"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.526Z"
fetched_at: "2026-10-07T22:41:25Z"
sha256: "43c0b00ca60c71beff1740a98eefa30e3129df047e34930a812ab3dbde5b5e6e"
body_chars: 8023
extracted_with: "main"
status: "live"
---

# Get site environments

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-site-environments/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Get site environments

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/{site_id}/environments', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/environments",
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/environments"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/{site_id}/environments")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments")

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

environments

Try it

Get site environments

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/{site_id}/environments', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/environments",
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/environments"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/{site_id}/environments")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments")

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

Successfully found site environments

[​](#response-site)

site

object

required

Show child attributes
