---
url: "https://api-docs.kinsta.com/api-reference/wordpress-sites/create-a-plain-site/"
title: "Create a plain site"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-sites"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.432Z"
fetched_at: "2026-10-07T22:40:20Z"
sha256: "98b1877b9debbe4214676d05f2f05da4f9927e888fa7603bab55740136683bef"
body_chars: 8518
extracted_with: "main"
status: "live"
---

# Create a plain site

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-sites/create-a-plain-site/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Create a plain site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/plain \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "display_name": "First plain site",
  "region": "us-central1"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/plain"

payload = {
    "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "display_name": "First plain site",
    "region": "us-central1"
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
    company: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    display_name: 'First plain site',
    region: 'us-central1'
  })
};

fetch('https://api.kinsta.com/v2/sites/plain', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/plain",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'company' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'display_name' => 'First plain site',
    'region' => 'us-central1'
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

	url := "https://api.kinsta.com/v2/sites/plain"

	payload := strings.NewReader("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First plain site\",\n  \"region\": \"us-central1\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/plain")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First plain site\",\n  \"region\": \"us-central1\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/plain")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First plain site\",\n  \"region\": \"us-central1\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding plain site in progress",
  "status": 202,
  "operation_id": "sites:add-plain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

plain

Try it

Create a plain site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/plain \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "display_name": "First plain site",
  "region": "us-central1"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/plain"

payload = {
    "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "display_name": "First plain site",
    "region": "us-central1"
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
    company: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    display_name: 'First plain site',
    region: 'us-central1'
  })
};

fetch('https://api.kinsta.com/v2/sites/plain', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/plain",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'company' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'display_name' => 'First plain site',
    'region' => 'us-central1'
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

	url := "https://api.kinsta.com/v2/sites/plain"

	payload := strings.NewReader("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First plain site\",\n  \"region\": \"us-central1\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/plain")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First plain site\",\n  \"region\": \"us-central1\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/plain")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First plain site\",\n  \"region\": \"us-central1\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding plain site in progress",
  "status": 202,
  "operation_id": "sites:add-plain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

#### Body

application/json

[​](#body-company)

company

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#body-display-name)

display_name

string

required

Example:

`"First plain site"`

[​](#body-region)

region

string

required

Example:

`"us-central1"`

#### Response

202

application/json

Plain site creation action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Adding plain site in progress"`

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

`"sites:add-plain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
