---
url: "https://api-docs.kinsta.com/api-reference/domains/create-a-domain-dns-record/"
title: "Create a domain DNS record"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "domains"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.368Z"
fetched_at: "2026-10-07T22:39:45Z"
sha256: "aef814be8bf61bd636dcc5f4382975b03762894bc80d8b1cb8f6b52b19bd953c"
body_chars: 9237
extracted_with: "main"
status: "live"
---

# Create a domain DNS record

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/domains/create-a-domain-dns-record/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Create a domain DNS record

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/domains/{domain_id}/dns-records \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
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
'
```

```
import requests

url = "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

payload = {
    "type": "A",
    "name": "abc.mydomain.com",
    "ttl": 3600,
    "resource_records": [{ "value": "1.1.1.1" }]
}
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
  body: JSON.stringify({
    type: 'A',
    name: 'abc.mydomain.com',
    ttl: 3600,
    resource_records: [{value: '1.1.1.1'}]
  })
};

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
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'A',
    'name' => 'abc.mydomain.com',
    'ttl' => 3600,
    'resource_records' => [
        [
                'value' => '1.1.1.1'
        ]
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

	url := "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

	payload := strings.NewReader("{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Creating a domain DNS record in progress",
  "status": 202,
  "operation_id": "domains:create-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

domains

/

{domain_id}

/

dns-records

Try it

Create a domain DNS record

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/domains/{domain_id}/dns-records \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
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
'
```

```
import requests

url = "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

payload = {
    "type": "A",
    "name": "abc.mydomain.com",
    "ttl": 3600,
    "resource_records": [{ "value": "1.1.1.1" }]
}
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
  body: JSON.stringify({
    type: 'A',
    name: 'abc.mydomain.com',
    ttl: 3600,
    resource_records: [{value: '1.1.1.1'}]
  })
};

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
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'A',
    'name' => 'abc.mydomain.com',
    'ttl' => 3600,
    'resource_records' => [
        [
                'value' => '1.1.1.1'
        ]
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

	url := "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

	payload := strings.NewReader("{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Creating a domain DNS record in progress",
  "status": 202,
  "operation_id": "domains:create-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#parameter-domain-id)

domain_id

string<uuid>

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-type)

type

string

required

Example:

`"A"`

[​](#body-name)

name

string

required

Example:

`"abc.mydomain.com"`

[​](#body-ttl)

ttl

number

required

TTL in seconds

Required range: `x >= 300`

Example:

`3600`

[​](#body-resource-records)

resource_records

object[]

required

Show child attributes

#### Response

202

application/json

DNS record create action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Creating a domain DNS record in progress"`

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

`"domains:create-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
