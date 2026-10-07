---
url: "https://api-docs.kinsta.com/api-reference/backups/restore-a-scheduled-or-manual-or-system-generated-backup-to-an-environment/"
title: "Restore a scheduled or manual or system generated backup to an environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "backups"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:50.768Z"
fetched_at: "2026-10-07T22:58:41Z"
sha256: "635b3ed7a3d1dba81e18bc88853598b3d654a07423a41c2a1c8ca294df629e49"
body_chars: 8860
extracted_with: "main"
status: "live"
---

# Restore a scheduled or manual or system generated backup to an environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/backups/restore-a-scheduled-or-manual-or-system-generated-backup-to-an-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Restore a scheduled or manual or system generated backup to an environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "backup_id": 123456789,
  "notified_user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore"

payload = {
    "backup_id": 123456789,
    "notified_user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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
  body: JSON.stringify({backup_id: 123456789, notified_user_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'backup_id' => 123456789,
    'notified_user_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1'
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

	url := "https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore"

	payload := strings.NewReader("{\n  \"backup_id\": 123456789,\n  \"notified_user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"backup_id\": 123456789,\n  \"notified_user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"backup_id\": 123456789,\n  \"notified_user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Restoring a backup to environment in progress",
  "status": 202,
  "operation_id": "backups:restore-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

{target_env_id}

/

backups

/

restore

Try it

Restore a scheduled or manual or system generated backup to an environment

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "backup_id": 123456789,
  "notified_user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore"

payload = {
    "backup_id": 123456789,
    "notified_user_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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
  body: JSON.stringify({backup_id: 123456789, notified_user_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1'})
};

fetch('https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'backup_id' => 123456789,
    'notified_user_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1'
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

	url := "https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore"

	payload := strings.NewReader("{\n  \"backup_id\": 123456789,\n  \"notified_user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"backup_id\": 123456789,\n  \"notified_user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{target_env_id}/backups/restore")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"backup_id\": 123456789,\n  \"notified_user_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\"\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Restoring a backup to environment in progress",
  "status": 202,
  "operation_id": "backups:restore-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#parameter-target-env-id)

target_env_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Body

application/json

[​](#body-backup-id)

backup_id

number

required

Example:

`123456789`

[​](#body-notified-user-id)

notified_user_id

string<uuid>

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

202

application/json

Restore backup to environment action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Restoring a backup to environment in progress"`

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

`"backups:restore-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
