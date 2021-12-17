import requests as r
import os

ROOT_URL = os.getenv("ROOTURL", "http://127.0.0.1:5000")

def get_topics():
  res = r.get(ROOT_URL + "/forum/topics")
  return res.json()

def create_topic(name, user_id, token):
  res = r.post(
    ROOT_URL + "/forum/topics",
    json={
      "topic": name,
      "id": user_id
    },
    headers={
      "Authorization": "Bearer " + token
    }
  )
  if res.text != "Success!":
    raise Exception("Error creating a topic!")
  
def get_messages_topic(topicid):
  res = r.get(ROOT_URL + f"/forum/topics/{topicid}/message")
  return res.json()

def add_message_topic(topicid, userid, msg, token):
  res = r.post(
    ROOT_URL + f"/forum/topics/{topicid}/message",
    json={
      "msg": msg,
      "userId": userid
    },
    headers={
      "Authorization": "Bearer " + token
    }
  )

  if res.text != "Success!":
    raise Exception("Error sending a message!")