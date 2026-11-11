---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-wp-admin-user/"
title: "Create WP admin user"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.517Z"
fetched_at: "2026-11-11T13:04:18Z"
sha256: "1b795c2b34ca1faff945fb65aba7df5f61cc1d285d99b2b893d5399ac45f58a1"
body_chars: 8084
extracted_with: "main"
status: "live"
---

# Create WP admin user

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-wp-admin-user/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Create WP admin user

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "email": "[email protected]",
  "first_name": "John",
  "last_name": "Doe"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user"

payload = {
    "email": "[email protected]",
    "first_name": "John",
    "last_name": "Doe"
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
  body: JSON.stringify({email: '[email protected]', first_name: 'John', last_name: 'Doe'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'email' => '[email protected]',
    'first_name' => 'John',
    'last_name' => 'Doe'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user"

	payload := strings.NewReader("{\n  \"email\": \"[email protected]\",\n  \"first_name\": \"John\",\n  \"last_name\": \"Doe\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"[email protected]\",\n  \"first_name\": \"John\",\n  \"last_name\": \"Doe\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"[email protected]\",\n  \"first_name\": \"John\",\n  \"last_name\": \"Doe\"\n}"

response = http.request(request)
puts response.read_body
```

200

400

401

500

```
{
  "create_wp_admin_user": true
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

wpa-create-user

Try it

Create WP admin user

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "email": "[email protected]",
  "first_name": "John",
  "last_name": "Doe"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user"

payload = {
    "email": "[email protected]",
    "first_name": "John",
    "last_name": "Doe"
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
  body: JSON.stringify({email: '[email protected]', first_name: 'John', last_name: 'Doe'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'email' => '[email protected]',
    'first_name' => 'John',
    'last_name' => 'Doe'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user"

	payload := strings.NewReader("{\n  \"email\": \"[email protected]\",\n  \"first_name\": \"John\",\n  \"last_name\": \"Doe\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"[email protected]\",\n  \"first_name\": \"John\",\n  \"last_name\": \"Doe\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-create-user")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"[email protected]\",\n  \"first_name\": \"John\",\n  \"last_name\": \"Doe\"\n}"

response = http.request(request)
puts response.read_body
```

200

400

401

500

```
{
  "create_wp_admin_user": true
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

[​](#body-email)

email

string<email>

required

Example:

`"[email protected]"`

[​](#body-first-name)

first_name

string

required

Example:

`"John"`

[​](#body-last-name)

last_name

string

required

Example:

`"Doe"`

#### Response

200

application/json

WP admin user created successfully

[​](#response-create-wp-admin-user)

create_wp_admin_user

boolean

required

Example:

`true`
