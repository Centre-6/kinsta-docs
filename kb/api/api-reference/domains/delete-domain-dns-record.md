---
url: "https://api-docs.kinsta.com/api-reference/domains/delete-domain-dns-record/"
title: "Delete domain DNS record"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "domains"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.400Z"
fetched_at: "2026-10-07T22:39:45Z"
sha256: "da732c72850346d92983d36ab1ef90b91e54af4ab0bc423f3a3116aec8e64028"
body_chars: 7905
extracted_with: "main"
status: "live"
---

# Delete domain DNS record

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/domains/delete-domain-dns-record/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Delete domain DNS record

cURL

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/domains/{domain_id}/dns-records \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "type": "A",
  "name": "staging.mydomain.com"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

payload = {
    "type": "A",
    "name": "staging.mydomain.com"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'DELETE',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({type: 'A', name: 'staging.mydomain.com'})
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
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'A',
    'name' => 'staging.mydomain.com'
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

	payload := strings.NewReader("{\n  \"type\": \"A\",\n  \"name\": \"staging.mydomain.com\"\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"A\",\n  \"name\": \"staging.mydomain.com\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"A\",\n  \"name\": \"staging.mydomain.com\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Deleting domain DNS record in progress",
  "status": 202,
  "operation_id": "domains:delete-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

domains

/

{domain_id}

/

dns-records

Try it

Delete domain DNS record

cURL

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/domains/{domain_id}/dns-records \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "type": "A",
  "name": "staging.mydomain.com"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/domains/{domain_id}/dns-records"

payload = {
    "type": "A",
    "name": "staging.mydomain.com"
}
headers = {
    "Authorization": "Bearer <token>",
    "Content-Type": "application/json"
}

response = requests.delete(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'DELETE',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: JSON.stringify({type: 'A', name: 'staging.mydomain.com'})
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
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_POSTFIELDS => json_encode([
    'type' => 'A',
    'name' => 'staging.mydomain.com'
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

	payload := strings.NewReader("{\n  \"type\": \"A\",\n  \"name\": \"staging.mydomain.com\"\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Authorization", "Bearer <token>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"A\",\n  \"name\": \"staging.mydomain.com\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/domains/{domain_id}/dns-records")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"A\",\n  \"name\": \"staging.mydomain.com\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Deleting domain DNS record in progress",
  "status": 202,
  "operation_id": "domains:delete-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

`"staging.mydomain.com"`

#### Response

202

application/json

Domain DNS record deletion action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Deleting domain DNS record in progress"`

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

`"domains:delete-dns-record-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
