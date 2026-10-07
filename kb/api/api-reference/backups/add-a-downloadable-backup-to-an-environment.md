---
url: "https://api-docs.kinsta.com/api-reference/backups/add-a-downloadable-backup-to-an-environment/"
title: "Add a downloadable backup to an environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "backups"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.726Z"
fetched_at: "2026-10-07T22:39:40Z"
sha256: "7646c2d36087a8a7401f547bd22eaec5de069e47e8201271a18b089456bf79e4"
body_chars: 6418
extracted_with: "main"
status: "live"
---

# Add a downloadable backup to an environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/backups/add-a-downloadable-backup-to-an-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Add a downloadable backup to an environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups"

headers = {"Authorization": "Bearer <token>"}

response = requests.post(url, headers=headers)

print(response.text)
```

```
const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups"

	req, _ := http.NewRequest("POST", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Starting downloadable backup generation. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "start-downloadable-backup-generation:update-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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
  "message": "Error occurred while processing your request",
  "status": 500,
  "data": "<unknown>"
}
```

POST

/

sites

/

environments

/

{env_id}

/

downloadable-backups

Try it

Add a downloadable backup to an environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups"

headers = {"Authorization": "Bearer <token>"}

response = requests.post(url, headers=headers)

print(response.text)
```

```
const options = {method: 'POST', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups"

	req, _ := http.NewRequest("POST", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/downloadable-backups")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Starting downloadable backup generation. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "start-downloadable-backup-generation:update-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

#### Response

202

application/json

Downloadable backup creation was successfully started for the environment

[​](#response-message)

message

string

required

Example:

`"Starting downloadable backup generation. Use the operation_id to check the status."`

[​](#response-status)

status

number

required

Example:

`202`

[​](#response-operation-id)

operation_id

string

Example:

`"start-downloadable-backup-generation:update-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
