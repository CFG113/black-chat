# BlackChat API

## Overview

BlackChat API is a simple chat application built with Python Flask. The API allows users to create and manage chat sessions, generate unique invitation links for sessions, join sessions using those links, and delete sessions and links.

## Features

- **Create Session**: Create a new chat session.
- **Generate Link**: Generate a unique link for a session.
- **Get Session by Link**: Retrieve the session ID associated with a given link.
- **Join Session**: Mark a link as used and join the session.
- **Delete Link**: Delete a link.
- **End Session**: Delete a session.

## Endpoints

### Create a New Session

- **URL**: `/sessions/create`
- **Method**: `POST`
- **Response**:
  - `201 Created`: `{ "session_id": "session_id" }`
  - `500 Internal Server Error`: Error message

### Get a Session by ID

- **URL**: `/sessions/<session_id>`
- **Method**: `GET`
- **Response**:
  - `200 OK`: `{ "session_id": "session_id" }`
  - `404 Not Found`: Error message

### End a Session

- **URL**: `/sessions/end-session`
- **Method**: `DELETE`
- **Request Body**:
  - `{ "session_id": "session_id" }`
- **Response**:
  - `204 No Content`
  - `400 Bad Request`: Error message
  - `404 Not Found`: Error message

### Generate a New Link

- **URL**: `/links/generate`
- **Method**: `POST`
- **Request Body**:
  - `{ "session_id": "session_id" }`
- **Response**:
  - `201 Created`: `{ "link": "link_id" }`
  - `500 Internal Server Error`: Error message

### Get Session ID by Link

- **URL**: `/links/session/<link_id>`
- **Method**: `GET`
- **Response**:
  - `200 OK`: `{ "session_id": "session_id" }`
  - `404 Not Found`: Error message

### Join a Session Using a Link

- **URL**: `/links/join/<link>`
- **Method**: `PUT`
- **Response**:
  - `200 OK`: `{ "success": true }`
  - `404 Not Found`: Error message
  - `410 Gone`: Error message

### Delete a Link

- **URL**: `/links/<link>`
- **Method**: `DELETE`
- **Response**:
  - `204 No Content`
  - `404 Not Found`: Error message

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CFG113/black-chat.git
   cd black-chat
New line Tue Aug 27 11:42:08 AEST 2024
