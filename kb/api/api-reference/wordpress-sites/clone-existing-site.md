---
url: "https://api-docs.kinsta.com/api-reference/wordpress-sites/clone-existing-site/"
title: "Clone existing site"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-sites"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.145Z"
fetched_at: "2026-11-11T13:04:52Z"
sha256: "282d1f6e1dc03b05dfce2c2c4f00da15cb1722021d07c0e4bef4ead727e9fe1c"
body_chars: 9208
extracted_with: "main"
status: "live"
---

# Clone existing site

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-sites/clone-existing-site/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Clone existing site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/clone \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "display_name": "Copy of First WP Site",
  "source_env_id": "0010cdaf-0b94-472e-86bd-7edf6fceaa1c"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/clone"

payload = {
    "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "display_name": "Copy of First WP Site",
    "source_env_id": "0010cdaf-0b94-472e-86bd-7edf6fceaa1c"
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
    display_name: 'Copy of First WP Site',
    source_env_id: '0010cdaf-0b94-472e-86bd-7edf6fceaa1c'
  })
};

fetch('https://api.kinsta.com/v2/sites/clone', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/clone",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'company' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'display_name' => 'Copy of First WP Site',
    'source_env_id' => '0010cdaf-0b94-472e-86bd-7edf6fceaa1c'
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

	url := "https://api.kinsta.com/v2/sites/clone"

	payload := strings.NewReader("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"Copy of First WP Site\",\n  \"source_env_id\": \"0010cdaf-0b94-472e-86bd-7edf6fceaa1c\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/clone")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"Copy of First WP Site\",\n  \"source_env_id\": \"0010cdaf-0b94-472e-86bd-7edf6fceaa1c\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/clone")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"Copy of First WP Site\",\n  \"source_env_id\": \"0010cdaf-0b94-472e-86bd-7edf6fceaa1c\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Cloning site in progress",
  "status": 202,
  "operation_id": "site:clone-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "support_reference_id": 123456
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

clone

Try it

Clone existing site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/clone \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "display_name": "Copy of First WP Site",
  "source_env_id": "0010cdaf-0b94-472e-86bd-7edf6fceaa1c"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/clone"

payload = {
    "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "display_name": "Copy of First WP Site",
    "source_env_id": "0010cdaf-0b94-472e-86bd-7edf6fceaa1c"
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
    display_name: 'Copy of First WP Site',
    source_env_id: '0010cdaf-0b94-472e-86bd-7edf6fceaa1c'
  })
};

fetch('https://api.kinsta.com/v2/sites/clone', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/clone",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'company' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'display_name' => 'Copy of First WP Site',
    'source_env_id' => '0010cdaf-0b94-472e-86bd-7edf6fceaa1c'
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

	url := "https://api.kinsta.com/v2/sites/clone"

	payload := strings.NewReader("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"Copy of First WP Site\",\n  \"source_env_id\": \"0010cdaf-0b94-472e-86bd-7edf6fceaa1c\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/clone")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"Copy of First WP Site\",\n  \"source_env_id\": \"0010cdaf-0b94-472e-86bd-7edf6fceaa1c\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/clone")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"Copy of First WP Site\",\n  \"source_env_id\": \"0010cdaf-0b94-472e-86bd-7edf6fceaa1c\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Cloning site in progress",
  "status": 202,
  "operation_id": "site:clone-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "support_reference_id": 123456
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

`"Copy of First WP Site"`

[​](#body-source-env-id)

source_env_id

string

required

Example:

`"0010cdaf-0b94-472e-86bd-7edf6fceaa1c"`

#### Response

202

application/json

Cloning Wordpress site action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Cloning site in progress"`

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

`"site:clone-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-support-reference-id)

support_reference_id

number

Example:

`123456`
