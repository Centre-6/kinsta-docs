---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/update-sftpssh-ip-allowlist/"
title: "Update SFTP/SSH IP allowlist"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:49.828Z"
fetched_at: "2026-10-07T22:59:00Z"
sha256: "4ea1f99d24627e9de7c8a6957d4d072df904a17187224b19e82af04020ac47e3"
body_chars: 7345
extracted_with: "main"
status: "live"
---

# Update SFTP/SSH IP allowlist

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/update-sftpssh-ip-allowlist/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Update SFTP/SSH IP allowlist

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "ip_allowlist": [
    "127.0.0.1"
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips"

payload = { "ip_allowlist": ["127.0.0.1"] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({ip_allowlist: ['127.0.0.1']})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'ip_allowlist' => [
        '127.0.0.1'
    ]
  ]),
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <token>",
    "Content-Type: application/json"
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips"

	payload := strings.NewReader("{\n  \"ip_allowlist\": [\n    \"127.0.0.1\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"ip_allowlist\": [\n    \"127.0.0.1\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"ip_allowlist\": [\n    \"127.0.0.1\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

400

401

500

```
{
  "result": null
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

ssh

/

set-allowed-ips

Try it

Update SFTP/SSH IP allowlist

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "ip_allowlist": [
    "127.0.0.1"
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips"

payload = { "ip_allowlist": ["127.0.0.1"] }
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({ip_allowlist: ['127.0.0.1']})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'ip_allowlist' => [
        '127.0.0.1'
    ]
  ]),
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <token>",
    "Content-Type: application/json"
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips"

	payload := strings.NewReader("{\n  \"ip_allowlist\": [\n    \"127.0.0.1\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"ip_allowlist\": [\n    \"127.0.0.1\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/ssh/set-allowed-ips")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"ip_allowlist\": [\n    \"127.0.0.1\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

400

401

500

```
{
  "result": null
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

#### Body

application/json

[​](#body-ip-allowlist)

ip_allowlist

string[]

required

Example:

```
["127.0.0.1"]
```

#### Response

200

application/json

Update SFTP/SSH IP allowlist

[​](#response-result)

result

null

required
