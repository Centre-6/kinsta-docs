---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-a-wordpress-site-environment/"
title: "Create a WordPress site environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:49.542Z"
fetched_at: "2026-10-07T22:58:51Z"
sha256: "2a2e421992752921c18bbb6580061c58f504db7958903eff1f46646957a09401"
body_chars: 13522
extracted_with: "main"
status: "live"
---

# Create a WordPress site environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/create-a-wordpress-site-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Create a WordPress site environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "display_name": "development",
  "site_title": "My First Site - development",
  "is_premium": false,
  "admin_email": "[email protected]",
  "admin_password": "vJnFnN-~v)PxF[6k",
  "admin_user": "admin",
  "wp_language": "en_US",
  "is_subdomain_multisite": false,
  "is_multisite": false,
  "woocommerce": false,
  "wordpress_plugin_edd": false,
  "wordpressseo": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments"

payload = {
    "display_name": "development",
    "site_title": "My First Site - development",
    "is_premium": False,
    "admin_email": "[email protected]",
    "admin_password": "vJnFnN-~v)PxF[6k",
    "admin_user": "admin",
    "wp_language": "en_US",
    "is_subdomain_multisite": False,
    "is_multisite": False,
    "woocommerce": False,
    "wordpress_plugin_edd": False,
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
    display_name: 'development',
    site_title: 'My First Site - development',
    is_premium: false,
    admin_email: '[email protected]',
    admin_password: 'vJnFnN-~v)PxF[6k',
    admin_user: 'admin',
    wp_language: 'en_US',
    is_subdomain_multisite: false,
    is_multisite: false,
    woocommerce: false,
    wordpress_plugin_edd: false,
    wordpressseo: false
  })
};

fetch('https://api.kinsta.com/v2/sites/{site_id}/environments', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/environments",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'display_name' => 'development',
    'site_title' => 'My First Site - development',
    'is_premium' => false,
    'admin_email' => '[email protected]',
    'admin_password' => 'vJnFnN-~v)PxF[6k',
    'admin_user' => 'admin',
    'wp_language' => 'en_US',
    'is_subdomain_multisite' => false,
    'is_multisite' => false,
    'woocommerce' => false,
    'wordpress_plugin_edd' => false,
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/environments"

	payload := strings.NewReader("{\n  \"display_name\": \"development\",\n  \"site_title\": \"My First Site - development\",\n  \"is_premium\": false,\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpress_plugin_edd\": false,\n  \"wordpressseo\": false\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/{site_id}/environments")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"display_name\": \"development\",\n  \"site_title\": \"My First Site - development\",\n  \"is_premium\": false,\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpress_plugin_edd\": false,\n  \"wordpressseo\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"display_name\": \"development\",\n  \"site_title\": \"My First Site - development\",\n  \"is_premium\": false,\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpress_plugin_edd\": false,\n  \"wordpressseo\": false\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding environment in progress",
  "status": 202,
  "operation_id": "environment:add-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

{site_id}

/

environments

Try it

Create a WordPress site environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "display_name": "development",
  "site_title": "My First Site - development",
  "is_premium": false,
  "admin_email": "[email protected]",
  "admin_password": "vJnFnN-~v)PxF[6k",
  "admin_user": "admin",
  "wp_language": "en_US",
  "is_subdomain_multisite": false,
  "is_multisite": false,
  "woocommerce": false,
  "wordpress_plugin_edd": false,
  "wordpressseo": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments"

payload = {
    "display_name": "development",
    "site_title": "My First Site - development",
    "is_premium": False,
    "admin_email": "[email protected]",
    "admin_password": "vJnFnN-~v)PxF[6k",
    "admin_user": "admin",
    "wp_language": "en_US",
    "is_subdomain_multisite": False,
    "is_multisite": False,
    "woocommerce": False,
    "wordpress_plugin_edd": False,
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
    display_name: 'development',
    site_title: 'My First Site - development',
    is_premium: false,
    admin_email: '[email protected]',
    admin_password: 'vJnFnN-~v)PxF[6k',
    admin_user: 'admin',
    wp_language: 'en_US',
    is_subdomain_multisite: false,
    is_multisite: false,
    woocommerce: false,
    wordpress_plugin_edd: false,
    wordpressseo: false
  })
};

fetch('https://api.kinsta.com/v2/sites/{site_id}/environments', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/environments",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'display_name' => 'development',
    'site_title' => 'My First Site - development',
    'is_premium' => false,
    'admin_email' => '[email protected]',
    'admin_password' => 'vJnFnN-~v)PxF[6k',
    'admin_user' => 'admin',
    'wp_language' => 'en_US',
    'is_subdomain_multisite' => false,
    'is_multisite' => false,
    'woocommerce' => false,
    'wordpress_plugin_edd' => false,
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/environments"

	payload := strings.NewReader("{\n  \"display_name\": \"development\",\n  \"site_title\": \"My First Site - development\",\n  \"is_premium\": false,\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpress_plugin_edd\": false,\n  \"wordpressseo\": false\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/{site_id}/environments")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"display_name\": \"development\",\n  \"site_title\": \"My First Site - development\",\n  \"is_premium\": false,\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpress_plugin_edd\": false,\n  \"wordpressseo\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"display_name\": \"development\",\n  \"site_title\": \"My First Site - development\",\n  \"is_premium\": false,\n  \"admin_email\": \"[email protected]\",\n  \"admin_password\": \"vJnFnN-~v)PxF[6k\",\n  \"admin_user\": \"admin\",\n  \"wp_language\": \"en_US\",\n  \"is_subdomain_multisite\": false,\n  \"is_multisite\": false,\n  \"woocommerce\": false,\n  \"wordpress_plugin_edd\": false,\n  \"wordpressseo\": false\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Adding environment in progress",
  "status": 202,
  "operation_id": "environment:add-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#parameter-site-id)

site_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-display-name)

display_name

string

required

Example:

`"development"`

[​](#body-site-title)

site_title

string

required

Example:

`"My First Site - development"`

[​](#body-is-premium)

is_premium

boolean

required

Example:

`false`

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

[​](#body-wordpress-plugin-edd)

wordpress_plugin_edd

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

Environment creation action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Adding environment in progress"`

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

`"environment:add-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
