import sys

async def main(scope, receive, send):
    sys.dont_write_bytecode = True
    assert scope['type'] == 'http'
    body = f'Received {scope["method"]} request to {scope["path"]}'
    await send({
        'type':'http.response.start',
        'status':200,
        'headers':[
            [b'content-type',b'text/plain']
        ]
    })
    await send({
        'type':'http.response.body',
        'body':body.encode('utf-8')
    })
    
if __name__ == "__main__":
    main()