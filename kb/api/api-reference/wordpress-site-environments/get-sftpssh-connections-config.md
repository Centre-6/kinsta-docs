---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-sftpssh-connections-config/"
title: "Get SFTP/SSH connections config"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
change_signal: "2026-09-18T09:42:49.842Z"
fetched_at: "2026-10-07T22:58:56Z"
sha256: "996dd6785ea6bf60491dc38453d4bba8fe46e1ee7d553e72ab789dcd019f134c"
body_chars: 6940
extracted_with: "main"
status: "live"
---

# Get SFTP/SSH connections config

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/get-sftpssh-connections-config/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Response](#response)

---

Get SFTP/SSH connections config

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config",
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

400

401

404

```
{
  "site": {
    "id": "<string>",
    "name": "<string>",
    "displayName": "<string>",
    "usr": "<string>",
    "environment": {
      "id": "<string>",
      "activeContainer": {
        "id": "<string>",
        "lxdSshPort": "<string>",
        "loadBalancer": {
          "id": "<string>",
          "extIP": "<string>"
        }
      }
    }
  },
  "port": "<string>",
  "name": "<string>",
  "host": "<string>",
  "user": "<string>",
  "ssh_command": "<string>"
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
  "message": "Could not find data or the user does not have permissions to retrieve it",
  "status": 404,
  "data": "<unknown>"
}
```

GET

/

sites

/

{site_id}

/

environments

/

{env_id}

/

ssh

/

config

Try it

Get SFTP/SSH connections config

cURL

```
curl --request GET \
  --url https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config \
  --header 'Authorization: Bearer <token>'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config"

headers = {"Authorization": "Bearer <token>"}

response = requests.get(url, headers=headers)

print(response.text)
```

```
const options = {method: 'GET', headers: {Authorization: 'Bearer <token>'}};

fetch('https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config",
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

	url := "https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Authorization", "Bearer <token>")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.get("https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/{site_id}/environments/{env_id}/ssh/config")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

200

400

401

404

```
{
  "site": {
    "id": "<string>",
    "name": "<string>",
    "displayName": "<string>",
    "usr": "<string>",
    "environment": {
      "id": "<string>",
      "activeContainer": {
        "id": "<string>",
        "lxdSshPort": "<string>",
        "loadBalancer": {
          "id": "<string>",
          "extIP": "<string>"
        }
      }
    }
  },
  "port": "<string>",
  "name": "<string>",
  "host": "<string>",
  "user": "<string>",
  "ssh_command": "<string>"
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
  "message": "Could not find data or the user does not have permissions to retrieve it",
  "status": 404,
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

[​](#parameter-site-id)

site_id

string

required

Example:

`"54fb80af-576c-4fdc-ba4f-b596c83f15a1"`

#### Response

200

application/json

Successfully found SFTP config

[​](#response-site)

site

object

required

Show child attributes

[​](#response-port)

port

string

required

[​](#response-name)

name

string

required

[​](#response-host)

host

string

required

[​](#response-user)

user

string

required

[​](#response-ssh-command)

ssh_command

string

required
