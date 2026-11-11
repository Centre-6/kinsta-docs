---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-tools/update-denied-ip-list/"
title: "Update denied IP list"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-tools"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.617Z"
fetched_at: "2026-11-11T13:04:51Z"
sha256: "1847f091187d45ef19a400af1a4e35ba0822bf8acc2d0341b92a0b09aa108d92"
body_chars: 8591
extracted_with: "main"
status: "live"
---

# Update denied IP list

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-tools/update-denied-ip-list/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Update denied IP list

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/tools/denied-ips \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "ip_list": [
    "127.0.0.1",
    "128.0.0.1/32",
    "2001:0db8:0a0b:12f0:0000:0000:0000:0001"
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/denied-ips"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "ip_list": ["127.0.0.1", "128.0.0.1/32", "2001:0db8:0a0b:12f0:0000:0000:0000:0001"]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'PUT',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({
    environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    ip_list: ['127.0.0.1', '128.0.0.1/32', '2001:0db8:0a0b:12f0:0000:0000:0000:0001']
  })
};

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
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'ip_list' => [
        '127.0.0.1',
        '128.0.0.1/32',
        '2001:0db8:0a0b:12f0:0000:0000:0000:0001'
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

	url := "https://api.kinsta.com/v2/sites/tools/denied-ips"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"ip_list\": [\n    \"127.0.0.1\",\n    \"128.0.0.1/32\",\n    \"2001:0db8:0a0b:12f0:0000:0000:0000:0001\"\n  ]\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/tools/denied-ips")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"ip_list\": [\n    \"127.0.0.1\",\n    \"128.0.0.1/32\",\n    \"2001:0db8:0a0b:12f0:0000:0000:0000:0001\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/denied-ips")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"ip_list\": [\n    \"127.0.0.1\",\n    \"128.0.0.1/32\",\n    \"2001:0db8:0a0b:12f0:0000:0000:0000:0001\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

401

500

```
{
  "result": null
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

PUT

/

sites

/

tools

/

denied-ips

Try it

Update denied IP list

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/tools/denied-ips \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "ip_list": [
    "127.0.0.1",
    "128.0.0.1/32",
    "2001:0db8:0a0b:12f0:0000:0000:0000:0001"
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/denied-ips"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "ip_list": ["127.0.0.1", "128.0.0.1/32", "2001:0db8:0a0b:12f0:0000:0000:0000:0001"]
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'PUT',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({
    environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    ip_list: ['127.0.0.1', '128.0.0.1/32', '2001:0db8:0a0b:12f0:0000:0000:0000:0001']
  })
};

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
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'ip_list' => [
        '127.0.0.1',
        '128.0.0.1/32',
        '2001:0db8:0a0b:12f0:0000:0000:0000:0001'
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

	url := "https://api.kinsta.com/v2/sites/tools/denied-ips"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"ip_list\": [\n    \"127.0.0.1\",\n    \"128.0.0.1/32\",\n    \"2001:0db8:0a0b:12f0:0000:0000:0000:0001\"\n  ]\n}")

	req, _ := http.NewRequest("PUT", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/tools/denied-ips")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"ip_list\": [\n    \"127.0.0.1\",\n    \"128.0.0.1/32\",\n    \"2001:0db8:0a0b:12f0:0000:0000:0000:0001\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/denied-ips")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"ip_list\": [\n    \"127.0.0.1\",\n    \"128.0.0.1/32\",\n    \"2001:0db8:0a0b:12f0:0000:0000:0000:0001\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

401

500

```
{
  "result": null
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

#### Body

application/json

[​](#body-environment-id)

environment_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#body-ip-list)

ip_list

string[]

required

Example:

```
[
  "127.0.0.1",
  "128.0.0.1/32",
  "2001:0db8:0a0b:12f0:0000:0000:0000:0001"
]
```

#### Response

200

application/json

List of denied IPs was updated

[​](#response-result)

result

null

required
