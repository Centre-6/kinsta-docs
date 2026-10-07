---
url: "https://api-docs.kinsta.com/api-reference/additional-sftp-users/add-additional-sftp-account/"
title: "Add additional SFTP account"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "additional-sftp-users"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:50.372Z"
fetched_at: "2026-10-07T22:58:29Z"
sha256: "76cbea86384254d48d6f69d364df6208f584c1159cd37baa2f3f99ec4ec1ad2c"
body_chars: 9348
extracted_with: "main"
status: "live"
---

# Add additional SFTP account

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/additional-sftp-users/add-additional-sftp-account/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Add additional SFTP account

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "username": "test-user",
  "password": "R8zXwT@#bV!kJq9^",
  "root_directory": "/dir_1",
  "permission": "write"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts"

payload = {
    "username": "test-user",
    "password": "R8zXwT@#bV!kJq9^",
    "root_directory": "/dir_1",
    "permission": "write"
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
    username: 'test-user',
    password: 'R8zXwT@#bV!kJq9^',
    root_directory: '/dir_1',
    permission: 'write'
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'username' => 'test-user',
    'password' => 'R8zXwT@#bV!kJq9^',
    'root_directory' => '/dir_1',
    'permission' => 'write'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts"

	payload := strings.NewReader("{\n  \"username\": \"test-user\",\n  \"password\": \"R8zXwT@#bV!kJq9^\",\n  \"root_directory\": \"/dir_1\",\n  \"permission\": \"write\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"username\": \"test-user\",\n  \"password\": \"R8zXwT@#bV!kJq9^\",\n  \"root_directory\": \"/dir_1\",\n  \"permission\": \"write\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"username\": \"test-user\",\n  \"password\": \"R8zXwT@#bV!kJq9^\",\n  \"root_directory\": \"/dir_1\",\n  \"permission\": \"write\"\n}"

response = http.request(request)
puts response.read_body
```

200

401

500

```
{
  "operation_id": "sftp-accounts:add-additional-sftp-account-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Adding Additional SFTP Account in progress",
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

POST

/

sites

/

environments

/

{env_id}

/

additional-sftp-accounts

Try it

Add additional SFTP account

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "username": "test-user",
  "password": "R8zXwT@#bV!kJq9^",
  "root_directory": "/dir_1",
  "permission": "write"
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts"

payload = {
    "username": "test-user",
    "password": "R8zXwT@#bV!kJq9^",
    "root_directory": "/dir_1",
    "permission": "write"
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
    username: 'test-user',
    password: 'R8zXwT@#bV!kJq9^',
    root_directory: '/dir_1',
    permission: 'write'
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'username' => 'test-user',
    'password' => 'R8zXwT@#bV!kJq9^',
    'root_directory' => '/dir_1',
    'permission' => 'write'
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts"

	payload := strings.NewReader("{\n  \"username\": \"test-user\",\n  \"password\": \"R8zXwT@#bV!kJq9^\",\n  \"root_directory\": \"/dir_1\",\n  \"permission\": \"write\"\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"username\": \"test-user\",\n  \"password\": \"R8zXwT@#bV!kJq9^\",\n  \"root_directory\": \"/dir_1\",\n  \"permission\": \"write\"\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/additional-sftp-accounts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"username\": \"test-user\",\n  \"password\": \"R8zXwT@#bV!kJq9^\",\n  \"root_directory\": \"/dir_1\",\n  \"permission\": \"write\"\n}"

response = http.request(request)
puts response.read_body
```

200

401

500

```
{
  "operation_id": "sftp-accounts:add-additional-sftp-account-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Adding Additional SFTP Account in progress",
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

[​](#body-username)

username

string

required

Example:

`"test-user"`

[​](#body-password)

password

string

required

Minimum string length: `16`

Example:

`"R8zXwT@#bV!kJq9^"`

[​](#body-root-directory)

root_directory

string

default:/

Example:

`"/dir_1"`

[​](#body-permission)

permission

enum<string>

default:read

Available options:

`read`,

`write`

Example:

`"write"`

#### Response

200

application/json

Adding additional SFTP account successful

[​](#response-operation-id)

operation_id

string

required

Example:

`"sftp-accounts:add-additional-sftp-account-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Adding Additional SFTP Account in progress"`

[​](#response-status)

status

number

required

Example:

`202`
