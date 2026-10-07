---
url: "https://api-docs.kinsta.com/api-reference/wordpress-site-environments/update-redirect-rules/"
title: "Update redirect rules"
tier: "api"
product: "api"
product_label: "Kinsta API Reference"
subsection: "wordpress-site-environments"
section: []
kinsta_last_updated:
sitemap_lastmod: "2026-09-18T09:42:49.711Z"
fetched_at: "2026-10-07T22:41:27Z"
sha256: "e0c3b876d4e351385ca3662fc2ff23e11e75eb35d8451c02f6efee680c945ec9"
body_chars: 14657
extracted_with: "main"
status: "live"
---

# Update redirect rules

**Product:** Kinsta API Reference
**Source:** https://api-docs.kinsta.com/api-reference/wordpress-site-environments/update-redirect-rules/

## On this page

    - [Authorizations](#authorizations)
    - [Path Parameters](#path-parameters)
    - [Body](#body)
    - [Response](#response)

---

Update redirect rules

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "limit": 10,
  "offset": 3,
  "key": "domain",
  "order": "ascend",
  "search_query": "Search...",
  "regex_search": "true",
  "rules_to_update": [
    {
      "domain": "kinsta.com",
      "from": "/redirect/from",
      "to": "/redirect/to",
      "traffic_from_city": "Nashville",
      "traffic_from_country": "US",
      "traffic_from_country_name": "United States",
      "displayed_location": "Nashvile, United States"
    }
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules"

payload = {
    "limit": 10,
    "offset": 3,
    "key": "domain",
    "order": "ascend",
    "search_query": "Search...",
    "regex_search": "true",
    "rules_to_update": [
        {
            "domain": "kinsta.com",
            "from": "/redirect/from",
            "to": "/redirect/to",
            "traffic_from_city": "Nashville",
            "traffic_from_country": "US",
            "traffic_from_country_name": "United States",
            "displayed_location": "Nashvile, United States"
        }
    ]
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
    limit: 10,
    offset: 3,
    key: 'domain',
    order: 'ascend',
    search_query: 'Search...',
    regex_search: 'true',
    rules_to_update: [
      {
        domain: 'kinsta.com',
        from: '/redirect/from',
        to: '/redirect/to',
        traffic_from_city: 'Nashville',
        traffic_from_country: 'US',
        traffic_from_country_name: 'United States',
        displayed_location: 'Nashvile, United States'
      }
    ]
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'limit' => 10,
    'offset' => 3,
    'key' => 'domain',
    'order' => 'ascend',
    'search_query' => 'Search...',
    'regex_search' => 'true',
    'rules_to_update' => [
        [
                'domain' => 'kinsta.com',
                'from' => '/redirect/from',
                'to' => '/redirect/to',
                'traffic_from_city' => 'Nashville',
                'traffic_from_country' => 'US',
                'traffic_from_country_name' => 'United States',
                'displayed_location' => 'Nashvile, United States'
        ]
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules"

	payload := strings.NewReader("{\n  \"limit\": 10,\n  \"offset\": 3,\n  \"key\": \"domain\",\n  \"order\": \"ascend\",\n  \"search_query\": \"Search...\",\n  \"regex_search\": \"true\",\n  \"rules_to_update\": [\n    {\n      \"domain\": \"kinsta.com\",\n      \"from\": \"/redirect/from\",\n      \"to\": \"/redirect/to\",\n      \"traffic_from_city\": \"Nashville\",\n      \"traffic_from_country\": \"US\",\n      \"traffic_from_country_name\": \"United States\",\n      \"displayed_location\": \"Nashvile, United States\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"limit\": 10,\n  \"offset\": 3,\n  \"key\": \"domain\",\n  \"order\": \"ascend\",\n  \"search_query\": \"Search...\",\n  \"regex_search\": \"true\",\n  \"rules_to_update\": [\n    {\n      \"domain\": \"kinsta.com\",\n      \"from\": \"/redirect/from\",\n      \"to\": \"/redirect/to\",\n      \"traffic_from_city\": \"Nashville\",\n      \"traffic_from_country\": \"US\",\n      \"traffic_from_country_name\": \"United States\",\n      \"displayed_location\": \"Nashvile, United States\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"limit\": 10,\n  \"offset\": 3,\n  \"key\": \"domain\",\n  \"order\": \"ascend\",\n  \"search_query\": \"Search...\",\n  \"regex_search\": \"true\",\n  \"rules_to_update\": [\n    {\n      \"domain\": \"kinsta.com\",\n      \"from\": \"/redirect/from\",\n      \"to\": \"/redirect/to\",\n      \"traffic_from_city\": \"Nashville\",\n      \"traffic_from_country\": \"US\",\n      \"traffic_from_country_name\": \"United States\",\n      \"displayed_location\": \"Nashvile, United States\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

400

401

404

500

```
{
  "result": null
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

redirect-rules

Try it

Update redirect rules

cURL

```
curl --request POST \
  --url https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "limit": 10,
  "offset": 3,
  "key": "domain",
  "order": "ascend",
  "search_query": "Search...",
  "regex_search": "true",
  "rules_to_update": [
    {
      "domain": "kinsta.com",
      "from": "/redirect/from",
      "to": "/redirect/to",
      "traffic_from_city": "Nashville",
      "traffic_from_country": "US",
      "traffic_from_country_name": "United States",
      "displayed_location": "Nashvile, United States"
    }
  ]
}
'
```

```
import requests

url = "https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules"

payload = {
    "limit": 10,
    "offset": 3,
    "key": "domain",
    "order": "ascend",
    "search_query": "Search...",
    "regex_search": "true",
    "rules_to_update": [
        {
            "domain": "kinsta.com",
            "from": "/redirect/from",
            "to": "/redirect/to",
            "traffic_from_city": "Nashville",
            "traffic_from_country": "US",
            "traffic_from_country_name": "United States",
            "displayed_location": "Nashvile, United States"
        }
    ]
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
    limit: 10,
    offset: 3,
    key: 'domain',
    order: 'ascend',
    search_query: 'Search...',
    regex_search: 'true',
    rules_to_update: [
      {
        domain: 'kinsta.com',
        from: '/redirect/from',
        to: '/redirect/to',
        traffic_from_city: 'Nashville',
        traffic_from_country: 'US',
        traffic_from_country_name: 'United States',
        displayed_location: 'Nashvile, United States'
      }
    ]
  })
};

fetch('https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => json_encode([
    'limit' => 10,
    'offset' => 3,
    'key' => 'domain',
    'order' => 'ascend',
    'search_query' => 'Search...',
    'regex_search' => 'true',
    'rules_to_update' => [
        [
                'domain' => 'kinsta.com',
                'from' => '/redirect/from',
                'to' => '/redirect/to',
                'traffic_from_city' => 'Nashville',
                'traffic_from_country' => 'US',
                'traffic_from_country_name' => 'United States',
                'displayed_location' => 'Nashvile, United States'
        ]
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

	url := "https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules"

	payload := strings.NewReader("{\n  \"limit\": 10,\n  \"offset\": 3,\n  \"key\": \"domain\",\n  \"order\": \"ascend\",\n  \"search_query\": \"Search...\",\n  \"regex_search\": \"true\",\n  \"rules_to_update\": [\n    {\n      \"domain\": \"kinsta.com\",\n      \"from\": \"/redirect/from\",\n      \"to\": \"/redirect/to\",\n      \"traffic_from_city\": \"Nashville\",\n      \"traffic_from_country\": \"US\",\n      \"traffic_from_country_name\": \"United States\",\n      \"displayed_location\": \"Nashvile, United States\"\n    }\n  ]\n}")

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
HttpResponse<String> response = Unirest.post("https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules")
  .header("Authorization", "Bearer <token>")
  .header("Content-Type", "application/json")
  .body("{\n  \"limit\": 10,\n  \"offset\": 3,\n  \"key\": \"domain\",\n  \"order\": \"ascend\",\n  \"search_query\": \"Search...\",\n  \"regex_search\": \"true\",\n  \"rules_to_update\": [\n    {\n      \"domain\": \"kinsta.com\",\n      \"from\": \"/redirect/from\",\n      \"to\": \"/redirect/to\",\n      \"traffic_from_city\": \"Nashville\",\n      \"traffic_from_country\": \"US\",\n      \"traffic_from_country_name\": \"United States\",\n      \"displayed_location\": \"Nashvile, United States\"\n    }\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.kinsta.com/v2/sites/environments/{env_id}/redirect-rules")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"limit\": 10,\n  \"offset\": 3,\n  \"key\": \"domain\",\n  \"order\": \"ascend\",\n  \"search_query\": \"Search...\",\n  \"regex_search\": \"true\",\n  \"rules_to_update\": [\n    {\n      \"domain\": \"kinsta.com\",\n      \"from\": \"/redirect/from\",\n      \"to\": \"/redirect/to\",\n      \"traffic_from_city\": \"Nashville\",\n      \"traffic_from_country\": \"US\",\n      \"traffic_from_country_name\": \"United States\",\n      \"displayed_location\": \"Nashvile, United States\"\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

200

400

401

404

500

```
{
  "result": null
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

[​](#body-action-type)

action_type

enum<string>

required

Available options:

`DELETE`,

`DELETE_ALL`,

`NEW`,

`UPDATE`

[​](#body-limit)

limit

number

default:10

Example:

`10`

[​](#body-offset)

offset

number

default:0

Example:

`3`

[​](#body-key)

key

enum<string>

default:domain

Available options:

`domain`,

`from`,

`to`,

`type`

Example:

`"domain"`

[​](#body-order)

order

enum<string>

default:ascend

Available options:

`ascend`,

`descend`

Example:

`"ascend"`

[​](#body-search-query)

search_query

string

default:""

Example:

`"Search..."`

[​](#body-regex-search)

regex_search

enum<string>

default:false

Available options:

`true`,

`false`

Example:

`"true"`

[​](#body-rules-to-update)

rules_to_update

object[]

Show child attributes

[​](#body-new-value)

new_value

object

Show child attributes

#### Response

200

application/json

Successfully updated redirect rules

[​](#response-result)

result

null

required
