---
url: "https://api-docs.kinsta.com/api-reference/company-users/get-a-company-user-by-id/"
title: "Get a company user by ID"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "company-users"
section: []
kinsta_last_updated:
change_signal: "2026-11-10T17:49:58.943Z"
fetched_at: "2026-11-11T13:03:40Z"
sha256: "637541222efd14001b80a98a9dc3549ff07baf27c92e73fe0c849ec60caaa96a"
body_chars: 6355
extracted_with: "main"
status: "live"
---

# Get a company user by ID

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/company-users/get-a-company-user-by-id/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Get a company user by ID

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/users/{id_user} \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/users/{id_user}"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/company/{id}/users/{id_user}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/users/{id_user}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
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

	url := "https://api.kinsta.com/v2/company/{id}/users/{id_user}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/company/{id}/users/{id_user}")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/users/{id_user}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "company": {
    "user_by_id": {
      "user": {
        "id": "9c1e4d2a-1b3c-4f5a-8d6e-7f8a9b0c1d2e",
        "email": "[email protected]",
        "full_name": "John Doe",
        "type_2fa": "email"
      },
      "capabilities": [
        {
          "role": "company-developer",
          "id_company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "id_site": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
        }
      ]
    }
  }
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
  "message": "Could not find data or the user does not have permissions to retrieve it",
  "status": 404,
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

GET

/

company

/

{id}

/

users

/

{id_user}

Try it

Get a company user by ID

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/company/{id}/users/{id_user} \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/company/{id}/users/{id_user}"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/company/{id}/users/{id_user}', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/company/{id}/users/{id_user}",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
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

	url := "https://api.kinsta.com/v2/company/{id}/users/{id_user}"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/company/{id}/users/{id_user}")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/company/{id}/users/{id_user}")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

401

404

500

```
{
  "company": {
    "user_by_id": {
      "user": {
        "id": "9c1e4d2a-1b3c-4f5a-8d6e-7f8a9b0c1d2e",
        "email": "[email protected]",
        "full_name": "John Doe",
        "type_2fa": "email"
      },
      "capabilities": [
        {
          "role": "company-developer",
          "id_company": "54fb80af-576c-4fdc-ba4f-b596c83f15a1",
          "id_site": "54fb80af-576c-4fdc-ba4f-b596c83f15a1"
        }
      ]
    }
  }
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
  "message": "Could not find data or the user does not have permissions to retrieve it",
  "status": 404,
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

[​](#parameter-id)

id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

[​](#parameter-id-user)

id_user

string

required

Example:

`"9c1e4d2a-1b3c-4f5a-8d6e-7f8a9b0c1d2e"`

#### Response

200

application/json

The requested company user

[​](#response-company)

company

object

required

Show child attributes
