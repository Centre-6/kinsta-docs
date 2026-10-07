---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-wp-admin-login-link-by-email/"
title: "Get WP admin login link by email"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.920Z"
fetched_at: "2026-10-07T22:40:07Z"
sha256: "1be753132445eb857785ce7266766df686b809d42aca53e9702e9bf75fa13d35"
body_chars: 7380
extracted_with: "main"
status: "live"
---

# Get WP admin login link by email

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-wp-admin-login-link-by-email/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Get WP admin login link by email

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "email": "[email protected]"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url"

payload = { "email": "[email protected]" }
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
  body: JSON.stringify({email: '[email protected]'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'email' => '[email protected]'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url"

	payload := strings.NewReader("{\n  \"email\": \"[email protected]\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"[email protected]\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"[email protected]\"\n}"

response = http.request(request)
puts response.read_body
```

200

400

401

500

```
{
  "login_link": "https://mysite.kinsta.cloud?wp-login.php?kinsta-wp-autologin=<token>"
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

wpa-login-url

Try it

Get WP admin login link by email

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "email": "[email protected]"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url"

payload = { "email": "[email protected]" }
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
  body: JSON.stringify({email: '[email protected]'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'email' => '[email protected]'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url"

	payload := strings.NewReader("{\n  \"email\": \"[email protected]\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"email\": \"[email protected]\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/wpa-login-url")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"email\": \"[email protected]\"\n}"

response = http.request(request)
puts response.read_body
```

200

400

401

500

```
{
  "login_link": "https://mysite.kinsta.cloud?wp-login.php?kinsta-wp-autologin=<token>"
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

#### Response

200

application/json

WP admin login link generated successfully

[​](#response-login-link)

login_link

string

required

Example:

`"https://mysite.kinsta.cloud?wp-login.php?kinsta-wp-autologin=<token>"`
