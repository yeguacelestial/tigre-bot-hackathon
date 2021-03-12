# tigre-bot-api

## Flowchart

<center>
    <img src="./assets/diagrama.jpeg" alt="flowchart" width=500 center>
</center>

___

## Consuming the API

### Base endpoint
The base endpoint must be the following URL:

`https://tigre-bot-api.herokuapp.com/api/v1`

### Sending a question

**Definition**

`POST /question`

**Arguments**

- `"content": string`, indicates the question text. This text is processed by a DialogFlow model.

**Response**

```javascript
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 3,
    "content": "this is the third question test"
}
```

### Getting all the questions with associated answers

**Definition**

`GET /question`

**Response**

```javascript
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "question": "this is a test",
        "answer": "this is the first answer"
    },
    {
        "id": 2,
        "question": "this is another test",
        "answer": "this is the second answer"
    },
    {
        "id": 3,
        "question": "this is the third question test",
        "answer": "this is the third answer"
    }
]
```