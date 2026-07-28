import requests

respuesta = requests.get("https://jsonplaceholder.typicode.com/users")
respuesta2 = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
respuesta3 = requests.get("https://jsonplaceholder.typicode.com/posts")

usuarios = respuesta.json()
usuarios2 = respuesta2.json()
usuarios3 = respuesta3.json()

#for usuario in usuarios:
   # print(f"{(usuario["name"])} | {(usuario["email"])}")

#print("--------------------------------------------------------")
#for comments in usuarios2:
   # print(f"{(comments["name"])} | {(comments["email"])}")

print("--------------------------------------------------------")
for post in usuarios3:
    if post["userId"] == 1:
        print(f"{(post["title"])}")