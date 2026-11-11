---
url: "https://api-docs.kinsta.com/api-reference/company-users/edit-user-capabilities-for-the-company/"
title: "Edit user capabilities for the company"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "company-users"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:58.956Z"
fetched_at: "2026-11-11T13:03:38Z"
sha256: "89a79dba1ac6ca3339cd6ec626bc7fc6acfeffb08a9daf4c95d30499a979fed1"
body_chars: 8822
extracted_with: "main"
status: "live"
---

# Edit user capabilities for the company

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/company-users/edit-user-capabilities-for-the-company/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Edit user capabilities for the company

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "role": "company-admin"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities"

payload = {
    "user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "role": "company-admin"
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
  body: JSON.stringify({user_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1', role: 'company-admin'})
};

fetch('https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'user_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'role' => 'company-admin'
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

	url := "https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities"

	payload := strings.NewReader("{\n  \"user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"role\": \"company-admin\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"role\": \"company-admin\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"role\": \"company-admin\"\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "message": "User capabilities updated for the company",
  "status": 202,
  "operation_id": "company:set-company-user-capabilities-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

POST

/

company

/

{company_id}

/

users

/

company-capabilities

Try it

Edit user capabilities for the company

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "role": "company-admin"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities"

payload = {
    "user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "role": "company-admin"
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
  body: JSON.stringify({user_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1', role: 'company-admin'})
};

fetch('https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'user_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'role' => 'company-admin'
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

	url := "https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities"

	payload := strings.NewReader("{\n  \"user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"role\": \"company-admin\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"role\": \"company-admin\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{company_id}/users/company-capabilities")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"role\": \"company-admin\"\n}"

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "message": "User capabilities updated for the company",
  "status": 202,
  "operation_id": "company:set-company-user-capabilities-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#parameter-company-id)

company_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-user-id)

user_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#body-role)

role

enum<string>

required

Available options:

`company-admin`,

`company-developer`,

`company-billing`

Example:

`"company-admin"`

#### Response

200

application/json

User capabilities updated for the company

[​](#response-message)

message

string

required

Example:

`"User capabilities updated for the company"`

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

`"company:set-company-user-capabilities-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
