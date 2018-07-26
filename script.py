from recastai import Request, Connect

request = Request('d6a613da8e0ef6ab1088ec4331229a0c')
request.analyse_text('Hi')

connect = Connect('d6a613da8e0ef6ab1088ec4331229a0c')
messages = [
  {
    'type': 'text',
    'content': 'Roger that',
  }
]

connect.broadcast_message(messages)