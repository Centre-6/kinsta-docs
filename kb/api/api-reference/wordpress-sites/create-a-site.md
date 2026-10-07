---
url: "https://api-docs.kinsta.com/api-reference/wordpress-sites/create-a-site/"
title: "Create a site"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-sites"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:49.447Z"
fetched_at: "2026-10-07T22:59:07Z"
sha256: "cf010dc132084a5e9f1f4694b4c3df4a7193f5f461405d8df95de7f35eccf15d"
body_chars: 13651
extracted_with: "main"
status: "live"
---

# Create a site

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-sites/create-a-site/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Create a site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "display_name": "First site",
  "region": "us-central1",
  "install_mode": "new",
  "admin_email": "[email protected]",
  "admin_password": "vJnFnN-~v)PxF[6k",
  "admin_user": "admin",
  "site_title": "My First Site",
  "wp_language": "en_US",
  "is_subdomain_multisite": false,
  "is_multisite": false,
  "woocommerce": false,
  "wordpressseo": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites"

payload = {
    "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "display_name": "First site",
    "region": "us-central1",
    "install_mode": "new",
    "admin_email": "[email protected]",
    "admin_password": "vJnFnN-~v)PxF[6k",
    "admin_user": "admin",
    "site_title": "My First Site",
    "wp_language": "en_US",
    "is_subdomain_multisite": False,
    "is_multisite": False,
    "woocommerce": False,
    "wordpressseo": False
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
    display_name: 'First site',
    region: 'us-central1',
    install_mode: 'new',
    admin_email: '[email protected]',
    admin_password: 'vJnFnN-~v)PxF[6k',
    admin_user: 'admin',
    site_title: 'My First Site',
    wp_language: 'en_US',
    is_subdomain_multisite: false,
    is_multisite: false,
    woocommerce: false,
    wordpressseo: false
  })
};

fetch('https://api.kinsta.com/v2/sites', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'company' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'display_name' => 'First site',
    'region' => 'us-central1',
    'install_mode' => 'new',
    'admin_email' => '[email protected]',
    'admin_password' => 'vJnFnN-~v)PxF[6k',
    'admin_user' => 'admin',
    'site_title' => 'My First Site',
    'wp_language' => 'en_US',
    'is_subdomain_multisite' => false,
    'is_multisite' => false,
    'woocommerce' => false,
    'wordpressseo' => false
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

	url := "https://api.kinsta.com/v2/sites"

	payload := strings.NewReader("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First site\",\n  \"region\": \"us-central1\",\n  \"install_mode\": \"new\",\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"site_title\": \"My First Site\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpressseo\": false\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First site\",\n  \"region\": \"us-central1\",\n  \"install_mode\": \"new\",\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"site_title\": \"My First Site\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpressseo\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First site\",\n  \"region\": \"us-central1\",\n  \"install_mode\": \"new\",\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"site_title\": \"My First Site\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpressseo\": false\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding site in progress",
  "status": 202,
  "operation_id": "sites:add-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

Try it

Create a site

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "display_name": "First site",
  "region": "us-central1",
  "install_mode": "new",
  "admin_email": "[email protected]",
  "admin_password": "vJnFnN-~v)PxF[6k",
  "admin_user": "admin",
  "site_title": "My First Site",
  "wp_language": "en_US",
  "is_subdomain_multisite": false,
  "is_multisite": false,
  "woocommerce": false,
  "wordpressseo": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites"

payload = {
    "company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "display_name": "First site",
    "region": "us-central1",
    "install_mode": "new",
    "admin_email": "[email protected]",
    "admin_password": "vJnFnN-~v)PxF[6k",
    "admin_user": "admin",
    "site_title": "My First Site",
    "wp_language": "en_US",
    "is_subdomain_multisite": False,
    "is_multisite": False,
    "woocommerce": False,
    "wordpressseo": False
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
    display_name: 'First site',
    region: 'us-central1',
    install_mode: 'new',
    admin_email: '[email protected]',
    admin_password: 'vJnFnN-~v)PxF[6k',
    admin_user: 'admin',
    site_title: 'My First Site',
    wp_language: 'en_US',
    is_subdomain_multisite: false,
    is_multisite: false,
    woocommerce: false,
    wordpressseo: false
  })
};

fetch('https://api.kinsta.com/v2/sites', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'company' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'display_name' => 'First site',
    'region' => 'us-central1',
    'install_mode' => 'new',
    'admin_email' => '[email protected]',
    'admin_password' => 'vJnFnN-~v)PxF[6k',
    'admin_user' => 'admin',
    'site_title' => 'My First Site',
    'wp_language' => 'en_US',
    'is_subdomain_multisite' => false,
    'is_multisite' => false,
    'woocommerce' => false,
    'wordpressseo' => false
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

	url := "https://api.kinsta.com/v2/sites"

	payload := strings.NewReader("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First site\",\n  \"region\": \"us-central1\",\n  \"install_mode\": \"new\",\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"site_title\": \"My First Site\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpressseo\": false\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First site\",\n  \"region\": \"us-central1\",\n  \"install_mode\": \"new\",\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"site_title\": \"My First Site\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpressseo\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"company\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"display_name\": \"First site\",\n  \"region\": \"us-central1\",\n  \"install_mode\": \"new\",\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"site_title\": \"My First Site\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpressseo\": false\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding site in progress",
  "status": 202,
  "operation_id": "sites:add-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

`"First site"`

[​](#body-region)

region

string

required

Example:

`"us-central1"`

[​](#body-install-mode)

install_mode

enum<string>

default:plain

required

deprecated

Available options:

`new`,

`plain`,

`clone`

Example:

`"new"`

[​](#body-admin-email)

admin_email

string

required

Example:

`"[email protected]"`

[​](#body-admin-password)

admin_password

string

required

Example:

`"vJnFnN-~v)PxF[6k"`

[​](#body-admin-user)

admin_user

string

required

Example:

`"admin"`

[​](#body-site-title)

site_title

string

required

Example:

`"My First Site"`

[​](#body-wp-language)

wp_language

string

required

Example:

`"en_US"`

[​](#body-is-subdomain-multisite)

is_subdomain_multisite

boolean

Example:

`false`

[​](#body-is-multisite)

is_multisite

boolean

Example:

`false`

[​](#body-woocommerce)

woocommerce

boolean

Example:

`false`

[​](#body-wordpressseo)

wordpressseo

boolean

Example:

`false`

#### Response

202

application/json

Site creation action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Adding site in progress"`

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

`"sites:add-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
