---
url: "https://api-docs.kinsta.com/api-reference/additional-sftp-users/enable-or-disable-additional-sftp-accounts/"
title: "Enable or disable additional SFTP accounts"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "additional-sftp-users"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:50.357Z"
fetched_at: "2026-10-07T22:58:29Z"
sha256: "cef8dff27b2b5ee4734c7a0c3cbb9205622560e419da962af521ac4a34494fc0"
body_chars: 7736
extracted_with: "main"
status: "live"
---

# Enable or disable additional SFTP accounts

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/additional-sftp-users/enable-or-disable-additional-sftp-accounts/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Enable or disable additional SFTP accounts

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "enabled": true
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status"

payload = { "enabled": True }
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
  body: JSON.stringify({enabled: true})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'enabled' => true
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status"

	payload := strings.NewReader("{\n  \"enabled\": true\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"enabled\": true\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"enabled\": true\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "sftp-accounts:toggle-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Updating Additional SFTP Accounts Status in progress",
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

environments

/

{env_id}

/

additional-sftp-accounts

/

toggle-status

Try it

Enable or disable additional SFTP accounts

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "enabled": true
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status"

payload = { "enabled": True }
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
  body: JSON.stringify({enabled: true})
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'enabled' => true
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status"

	payload := strings.NewReader("{\n  \"enabled\": true\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"enabled\": true\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts/toggle-status")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"enabled\": true\n}"

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "sftp-accounts:toggle-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Updating Additional SFTP Accounts Status in progress",
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

#### Path Parameters

[​](#parameter-env-id)

env_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-enabled)

enabled

boolean

required

Example:

`true`

#### Response

202

application/json

Toggling status for additional SFTP accounts in progress

[​](#response-operation-id)

operation_id

string

required

Example:

`"sftp-accounts:toggle-status-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Updating Additional SFTP Accounts Status in progress"`

[​](#response-status)

status

number

required

Example:

`202`
