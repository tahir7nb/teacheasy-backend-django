from google.oauth2 import id_token
from google.auth.transport import requests
import os
from dotenv import load_dotenv
import requests as req
load_dotenv()

def verify_token(token):
    try:
        CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
        # print(CLIENT_ID)
        idinfo = id_token.verify_oauth2_token(token, requests.Request())
        if 'email' in idinfo:
            return idinfo['email']
        else:
            return None
    except Exception as e:
        print('exception in verify_token')
        print(e)
        return None

# print(verify_token('eyJhbGciOiJSUzI1NiIsImtpZCI6ImVkODA2ZjE4NDJiNTg4MDU0YjE4YjY2OWRkMWEwOWE0ZjM2N2FmYzQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJhY2NvdW50cy5nb29nbGUuY29tIiwiYXpwIjoiMTA0NzA2NTEwMTE0Ni0xdWZ1c250Z2Zmc2sxbWdmcGt0cGhjbXQxZXA3bWY0Yi5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsImF1ZCI6IjEwNDcwNjUxMDExNDYtMXVmdXNudGdmZnNrMW1nZnBrdHBoY210MWVwN21mNGIuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDE5NjI0MTY1MDUzNDM0NDIwOTEiLCJlbWFpbCI6Im1vZWVuY2hpc2h0eTk2QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJhdF9oYXNoIjoiNllaYXlIaVc5OGQxd1pyamdlbTY3ZyIsImlhdCI6MTcwNzY2NTQ3MSwiZXhwIjoxNzA3NjY5MDcxfQ.dWTFLvxpVMOSWzLpEvI9aeh8cjh7QhOgku-NkOytJYmaSxIJ2Nl_ThET0QlyeV7IAN_uzB4cEwyAVg-k__TyXoy0ON03ee4s9zlM5pCbIB71MH-GxIdhKgw8Bpyf4PUidi0phe8usTMg-sDdihR3MaYmjEhvJlqPux5rYHWzWTxnXdCPq4ChpK2Ra4gWN5TrSxPArEhDxbYocJ1407mekcfo9iQv-rAXMuLJrbbu3rWF8GD4_42UnmG_ZRU-8tnP8sUppDEC35ILiCnGJx3KAqUkR9oD0XCYnAxk79XqlEjp0VDpKr547e4sASabwA1VtTEf7tmzQ_-TwGow2bQpsg'))