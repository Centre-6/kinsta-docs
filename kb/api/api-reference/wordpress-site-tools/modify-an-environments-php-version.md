---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-tools/modify-an-environments-php-version/"
title: "Modify an Environment's PHP Version"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-tools"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.589Z"
fetched_at: "2026-11-11T13:04:47Z"
sha256: "7e1e98f122f4c7f7550ecebea69fd6428865244fdb8ad66027245dc8c00e35e0"
body_chars: 8883
extracted_with: "main"
status: "live"
---

# Modify an Environment's PHP Version

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-tools/modify-an-environments-php-version/

## On this page

    - [Authorizations](#authorizations)
    - [Body](#body)
    - [Response](#response)

---

Modify an Environment's PHP Version

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/tools/modify-php-version \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "php_version": "8.1",
  "is_opt_out_from_automatic_php_update": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/modify-php-version"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "php_version": "8.1",
    "is_opt_out_from_automatic_php_update": False
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
    environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    php_version: '8.1',
    is_opt_out_from_automatic_php_update: false
  })
};

fetch('https://api.kinsta.com/v2/sites/tools/modify-php-version', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/tools/modify-php-version",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'php_version' => '8.1',
    'is_opt_out_from_automatic_php_update' => false
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

	url := "https://api.kinsta.com/v2/sites/tools/modify-php-version"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"php_version\": \"8.1\",\n  \"is_opt_out_from_automatic_php_update\": false\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/tools/modify-php-version")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"php_version\": \"8.1\",\n  \"is_opt_out_from_automatic_php_update\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/modify-php-version")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"php_version\": \"8.1\",\n  \"is_opt_out_from_automatic_php_update\": false\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "php:modify-version-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Modifying PHP version in progress",
  "status": 202
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

tools

/

modify-php-version

Try it

Modify an Environment's PHP Version

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/tools/modify-php-version \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "php_version": "8.1",
  "is_opt_out_from_automatic_php_update": false
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/tools/modify-php-version"

payload = {
    "environment_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "php_version": "8.1",
    "is_opt_out_from_automatic_php_update": False
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
    environment_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    php_version: '8.1',
    is_opt_out_from_automatic_php_update: false
  })
};

fetch('https://api.kinsta.com/v2/sites/tools/modify-php-version', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/tools/modify-php-version",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'environment_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'php_version' => '8.1',
    'is_opt_out_from_automatic_php_update' => false
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

	url := "https://api.kinsta.com/v2/sites/tools/modify-php-version"

	payload := strings.NewReader("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"php_version\": \"8.1\",\n  \"is_opt_out_from_automatic_php_update\": false\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/tools/modify-php-version")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"php_version\": \"8.1\",\n  \"is_opt_out_from_automatic_php_update\": false\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/tools/modify-php-version")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"environment_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"php_version\": \"8.1\",\n  \"is_opt_out_from_automatic_php_update\": false\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "php:modify-version-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Modifying PHP version in progress",
  "status": 202
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

[​](#body-environment-id)

environment_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#body-php-version)

php_version

string

required

Example:

`"8.1"`

[​](#body-is-opt-out-from-automatic-php-update)

is_opt_out_from_automatic_php_update

boolean

Example:

`false`

#### Response

202

application/json

Modifying PHP version in progress

[​](#response-operation-id)

operation_id

string

required

Example:

`"php:modify-version-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Modifying PHP version in progress"`

[​](#response-status)

status

number

required

Example:

`202`
