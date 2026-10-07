---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-domains/change-primary-domain-of-an-environment/"
title: "Change primary domain of an environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-domains"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:50.282Z"
fetched_at: "2026-10-07T22:58:47Z"
sha256: "9f37de8b2ca4e2566323f4df39c685b0596e18dc7583a52d1ba64df982e548c9"
body_chars: 8812
extracted_with: "main"
status: "live"
---

# Change primary domain of an environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-domains/change-primary-domain-of-an-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Change primary domain of an environment

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "domain_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "run_search_and_replace": true
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain"

payload = {
    "domain_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "run_search_and_replace": True
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
    domain_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    run_search_and_replace: true
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'domain_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'run_search_and_replace' => true
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain"

	payload := strings.NewReader("{\n  \"domain_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"run_search_and_replace\": true\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"domain_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"run_search_and_replace\": true\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"domain_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"run_search_and_replace\": true\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Changing primary site domain in progress",
  "status": 202,
  "operation_id": "sites:change-primary-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

sites

/

environments

/

{env_id}

/

change-primary-domain

Try it

Change primary domain of an environment

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "domain_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "run_search_and_replace": true
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain"

payload = {
    "domain_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "run_search_and_replace": True
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
    domain_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    run_search_and_replace: true
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'domain_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'run_search_and_replace' => true
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain"

	payload := strings.NewReader("{\n  \"domain_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"run_search_and_replace\": true\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"domain_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"run_search_and_replace\": true\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/change-primary-domain")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"domain_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"run_search_and_replace\": true\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Changing primary site domain in progress",
  "status": 202,
  "operation_id": "sites:change-primary-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#body-domain-id)

domain_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#body-run-search-and-replace)

run_search_and_replace

boolean

default:false

required

Example:

`true`

#### Response

202

application/json

Changing primary domain action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Changing primary site domain in progress"`

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

`"sites:change-primary-domain-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
