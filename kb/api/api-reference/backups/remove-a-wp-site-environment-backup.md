---
url: "https://api-docs.kinsta.com/api-reference/backups/remove-a-wp-site-environment-backup/"
title: "Remove a WP site environment backup"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "backups"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:50.800Z"
fetched_at: "2026-10-07T22:39:43Z"
sha256: "514e69c72fdf46e09e416e3625202d5f962cd8459c9d398ad3c3f4c07e04a489"
body_chars: 6105
extracted_with: "main"
status: "live"
---

# Remove a WP site environment backup

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/backups/remove-a-wp-site-environment-backup/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Remove a WP site environment backup

cURL

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/sites/environments/backups/{backup_id} \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/backups/{backup_id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.text)
```

```
const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/backups/{backup_id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/backups/{backup_id}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
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

	url := "https://api.kinsta.com/v2/sites/environments/backups/{backup_id}"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.kinsta.com/v2/sites/environments/backups/{backup_id}")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/backups/{backup_id}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
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
  "message": "Removing a backup in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "backups:remove-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

DELETE

/

sites

/

environments

/

backups

/

{backup_id}

Try it

Remove a WP site environment backup

cURL

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/sites/environments/backups/{backup_id} \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/backups/{backup_id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.text)
```

```
const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/backups/{backup_id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/backups/{backup_id}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
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

	url := "https://api.kinsta.com/v2/sites/environments/backups/{backup_id}"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.kinsta.com/v2/sites/environments/backups/{backup_id}")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/backups/{backup_id}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
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
  "message": "Removing a backup in progress. Use the operation_id to check the status.",
  "status": 202,
  "operation_id": "backups:remove-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#parameter-backup-id)

backup_id

number

required

Example:

`165424355`

#### Response

202

application/json

Removing backup action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Removing a backup in progress. Use the operation_id to check the status."`

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

`"backups:remove-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
