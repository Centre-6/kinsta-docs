---
url: "https://api-docs.kinsta.com/api-reference/additional-sftp-users/remove-additional-sftp-account/"
title: "Remove additional SFTP account"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "additional-sftp-users"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:59.918Z"
fetched_at: "2026-11-11T13:03:06Z"
sha256: "7d2362a7d29348f2805a44eca6730c4210561d631dd0c0c3921f3ca3f4dac344"
body_chars: 6300
extracted_with: "main"
status: "live"
---

# Remove additional SFTP account

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/additional-sftp-users/remove-additional-sftp-account/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Remove additional SFTP account

cURL

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id} \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.text)
```

```
const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <token>"
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "sftp-accounts:remove-additional-sftp-account-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Removing Additional SFTP Account in progress",
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

DELETE

/

sites

/

environments

/

additional-sftp-accounts

/

{sftp_account_id}

Try it

Remove additional SFTP account

cURL

```
curl --request DELETE \
  --url https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id} \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}"

headers = {"Authorization": "Bearer <token>"}

response = requests.delete(url, headers=headers)

print(response.text)
```

```
const options = {method: 'DELETE', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer <token>"
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
	"net/http"
	"io"
)

func main() {

	url := "https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/additional-sftp-accounts/{sftp_account_id}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

202

401

500

```
{
  "operation_id": "sftp-accounts:remove-additional-sftp-account-54fb80af-576c-4fdc-ba4f-b596c83f15a1",
  "message": "Removing Additional SFTP Account in progress",
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

[​](#parameter-sftp-account-id)

sftp_account_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

202

application/json

Removing additional SFTP account in progress

[​](#response-operation-id)

operation_id

string

required

Example:

`"sftp-accounts:remove-additional-sftp-account-54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#response-message)

message

string

required

Example:

`"Removing Additional SFTP Account in progress"`

[​](#response-status)

status

number

required

Example:

`202`
