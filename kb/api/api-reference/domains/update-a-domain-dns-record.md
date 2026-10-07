---
url: "https://api-docs.kinsta.com/api-reference/domains/update-a-domain-dns-record/"
title: "Update a domain DNS record"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "domains"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.384Z"
fetched_at: "2026-10-07T22:41:06Z"
sha256: "8f22149993cd005f131c6a039226953d1a2ea278c2f207f49b0d14ea65538220"
body_chars: 10440
extracted_with: "main"
status: "live"
---

# Update a domain DNS record

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/domains/update-a-domain-dns-record/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Update a domain DNS record

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/domains/{domain_id}/dns-records \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "type": "A",
  "name": "abc.mydomain.com",
  "ttl": 3600,
  "new_resource_records": [
    {
      "value": "1.1.1.1"
    }
  ],
  "removed_resource_records": [
    {
      "value": "2.2.2.2"
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
    "new_resource_records": [{ "value": "1.1.1.1" }],
    "removed_resource_records": [{ "value": "2.2.2.2" }]
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
    type: 'A',
    name: 'abc.mydomain.com',
    ttl: 3600,
    new_resource_records: [{value: '1.1.1.1'}],
    removed_resource_records: [{value: '2.2.2.2'}]
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
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'A',
    'name' => 'abc.mydomain.com',
    'ttl' => 3600,
    'new_resource_records' => [
        [
                'value' => '1.1.1.1'
        ]
    ],
    'removed_resource_records' => [
        [
                'value' => '2.2.2.2'
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

	payload := strings.NewReader("{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"new_resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ],\n  \"removed_resource_records\": [\n    {\n      \"value\": \"2.2.2.2\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"new_resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ],\n  \"removed_resource_records\": [\n    {\n      \"value\": \"2.2.2.2\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"new_resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ],\n  \"removed_resource_records\": [\n    {\n      \"value\": \"2.2.2.2\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Updating a domain DNS record in progress",
  "status": 202,
  "operation_id": "domains:update-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

PUT

/

domains

/

{domain_id}

/

dns-records

Try it

Update a domain DNS record

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/domains/{domain_id}/dns-records \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "type": "A",
  "name": "abc.mydomain.com",
  "ttl": 3600,
  "new_resource_records": [
    {
      "value": "1.1.1.1"
    }
  ],
  "removed_resource_records": [
    {
      "value": "2.2.2.2"
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
    "new_resource_records": [{ "value": "1.1.1.1" }],
    "removed_resource_records": [{ "value": "2.2.2.2" }]
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
    type: 'A',
    name: 'abc.mydomain.com',
    ttl: 3600,
    new_resource_records: [{value: '1.1.1.1'}],
    removed_resource_records: [{value: '2.2.2.2'}]
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
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'A',
    'name' => 'abc.mydomain.com',
    'ttl' => 3600,
    'new_resource_records' => [
        [
                'value' => '1.1.1.1'
        ]
    ],
    'removed_resource_records' => [
        [
                'value' => '2.2.2.2'
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

	payload := strings.NewReader("{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"new_resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ],\n  \"removed_resource_records\": [\n    {\n      \"value\": \"2.2.2.2\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"new_resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ],\n  \"removed_resource_records\": [\n    {\n      \"value\": \"2.2.2.2\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"A\",\n  \"name\": \"abc.mydomain.com\",\n  \"ttl\": 3600,\n  \"new_resource_records\": [\n    {\n      \"value\": \"1.1.1.1\"\n    }\n  ],\n  \"removed_resource_records\": [\n    {\n      \"value\": \"2.2.2.2\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Updating a domain DNS record in progress",
  "status": 202,
  "operation_id": "domains:update-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

TTL in seconds

Required range: `x >= 300`

Example:

`3600`

[​](#body-new-resource-records)

new_resource_records

object[]

Show child attributes

[​](#body-removed-resource-records)

removed_resource_records

object[]

Show child attributes

#### Response

202

application/json

DNS record update action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Updating a domain DNS record in progress"`

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

`"domains:update-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
