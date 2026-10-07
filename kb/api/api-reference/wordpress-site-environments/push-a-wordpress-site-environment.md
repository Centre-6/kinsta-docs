---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/push-a-wordpress-site-environment/"
title: "Push a WordPress site environment"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.558Z"
fetched_at: "2026-10-07T22:41:26Z"
sha256: "fffd19885014d621df5041c27e9f3c243b56f9efdc137d020b5147bc1ae782c2"
body_chars: 12584
extracted_with: "main"
status: "live"
---

# Push a WordPress site environment

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/push-a-wordpress-site-environment/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Push a WordPress site environment

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "source_env_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "target_env_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "push_db": true,
  "push_files": true,
  "run_search_and_replace": true,
  "push_files_option": "SPECIFIC_FILES",
  "file_list": [
    "wp-content/plugins",
    "wp-content/themes",
    "wp-content/uploads"
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments"

payload = {
    "source_env_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "target_env_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "push_db": True,
    "push_files": True,
    "run_search_and_replace": True,
    "push_files_option": "SPECIFIC_FILES",
    "file_list": ["wp-content/plugins", "wp-content/themes", "wp-content/uploads"]
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
    source_env_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    target_env_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    push_db: true,
    push_files: true,
    run_search_and_replace: true,
    push_files_option: 'SPECIFIC_FILES',
    file_list: ['wp-content/plugins', 'wp-content/themes', 'wp-content/uploads']
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
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'source_env_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'target_env_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'push_db' => true,
    'push_files' => true,
    'run_search_and_replace' => true,
    'push_files_option' => 'SPECIFIC_FILES',
    'file_list' => [
        'wp-content/plugins',
        'wp-content/themes',
        'wp-content/uploads'
    ]
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

	payload := strings.NewReader("{\n  \"source_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"target_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"push_db\": true,\n  \"push_files\": true,\n  \"run_search_and_replace\": true,\n  \"push_files_option\": \"SPECIFIC_FILES\",\n  \"file_list\": [\n    \"wp-content/plugins\",\n    \"wp-content/themes\",\n    \"wp-content/uploads\"\n  ]\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/{site_id}/environments")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"source_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"target_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"push_db\": true,\n  \"push_files\": true,\n  \"run_search_and_replace\": true,\n  \"push_files_option\": \"SPECIFIC_FILES\",\n  \"file_list\": [\n    \"wp-content/plugins\",\n    \"wp-content/themes\",\n    \"wp-content/uploads\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"source_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"target_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"push_db\": true,\n  \"push_files\": true,\n  \"run_search_and_replace\": true,\n  \"push_files_option\": \"SPECIFIC_FILES\",\n  \"file_list\": [\n    \"wp-content/plugins\",\n    \"wp-content/themes\",\n    \"wp-content/uploads\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Pushing environment in progress",
  "status": 202,
  "operation_id": "environments:push-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

{site_id}

/

environments

Try it

Push a WordPress site environment

cURL

```
curl --request PUT \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "source_env_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "target_env_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "push_db": true,
  "push_files": true,
  "run_search_and_replace": true,
  "push_files_option": "SPECIFIC_FILES",
  "file_list": [
    "wp-content/plugins",
    "wp-content/themes",
    "wp-content/uploads"
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments"

payload = {
    "source_env_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "target_env_id": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
    "push_db": True,
    "push_files": True,
    "run_search_and_replace": True,
    "push_files_option": "SPECIFIC_FILES",
    "file_list": ["wp-content/plugins", "wp-content/themes", "wp-content/uploads"]
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
    source_env_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    target_env_id: '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    push_db: true,
    push_files: true,
    run_search_and_replace: true,
    push_files_option: 'SPECIFIC_FILES',
    file_list: ['wp-content/plugins', 'wp-content/themes', 'wp-content/uploads']
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
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => json_encode([
    'source_env_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'target_env_id' => '54fb80af-576c-4fdc-ba4f-b596c83f15a1',
    'push_db' => true,
    'push_files' => true,
    'run_search_and_replace' => true,
    'push_files_option' => 'SPECIFIC_FILES',
    'file_list' => [
        'wp-content/plugins',
        'wp-content/themes',
        'wp-content/uploads'
    ]
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

	payload := strings.NewReader("{\n  \"source_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"target_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"push_db\": true,\n  \"push_files\": true,\n  \"run_search_and_replace\": true,\n  \"push_files_option\": \"SPECIFIC_FILES\",\n  \"file_list\": [\n    \"wp-content/plugins\",\n    \"wp-content/themes\",\n    \"wp-content/uploads\"\n  ]\n}")

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
HttpResponse<String> response = Unirest.put("https://api.kinsta.com/v2/sites/{site_id}/environments")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"source_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"target_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"push_db\": true,\n  \"push_files\": true,\n  \"run_search_and_replace\": true,\n  \"push_files_option\": \"SPECIFIC_FILES\",\n  \"file_list\": [\n    \"wp-content/plugins\",\n    \"wp-content/themes\",\n    \"wp-content/uploads\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"source_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"target_env_id\": \"54fb80af-576c-4fdc-ba4f-b596c83f15a1\",\n  \"push_db\": true,\n  \"push_files\": true,\n  \"run_search_and_replace\": true,\n  \"push_files_option\": \"SPECIFIC_FILES\",\n  \"file_list\": [\n    \"wp-content/plugins\",\n    \"wp-content/themes\",\n    \"wp-content/uploads\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

202

400

401

500

```
{
  "message": "Pushing environment in progress",
  "status": 202,
  "operation_id": "environments:push-54fb80af-576c-4fdc-ba4f-b596c83f15a1"
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

[​](#body-source-env-id)

source_env_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#body-target-env-id)

target_env_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#body-push-db)

push_db

boolean

default:true

Example:

`true`

[​](#body-push-files)

push_files

boolean

default:true

Example:

`true`

[​](#body-run-search-and-replace)

run_search_and_replace

boolean

default:true

Example:

`true`

[​](#body-push-files-option)

push_files_option

enum<string>

default:ALL_FILES

Available options:

`ALL_FILES`,

`SPECIFIC_FILES`

Example:

`"SPECIFIC_FILES"`

[​](#body-file-list)

file_list

string[]

Example:

```
[  
  "wp-content/plugins",  
  "wp-content/themes",  
  "wp-content/uploads"  
]
```

#### Response

202

application/json

Pushing environment action started. Check MyKinsta for status

[​](#response-message)

message

string

required

Example:

`"Pushing environment in progress"`

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

`"environments:push-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`
