import os

choices = {}
choices['1']="POST /images                        Create a new image"
choices['2']="POST /containers                    Create a new container"
choices['3']="GET /containers                     List all containers"
choices['4']="GET /containers?state=running       List running containers"
choices['5']="GET /containers/<id>                Find specific container"
choices['6']="GET /containers/<id>/logs           Dump specific container logs" 
choices['7']="GET /images                         List all images"
choices['8']="PATCH /containers/<id>              Change a container's state" 
choices['9']="PATCH /images/<id>                  Change a specific image's attributes"
choices['10']="DELETE /containers/<id>             Delete a specific container"
choices['11']="DELETE /containers                  Delete all containers (including running)"
choices['12']="DELETE /images/<id>                 Delete a specific image"
choices['13']="DELETE /images                      Delete all images"
choices['14']="Exit"

while True: 
  options=choices.keys()
  options.sort()
  
  print "Available API endpoints:"
  for entry in options: 
    print entry, choices[entry]
  selection=raw_input("Please Select:") 
  if selection =='1': 
    os.system("curl -s -X GET -H 'Accept: application/json' http://146.148.26.129:8080/containers | python -mjson.tool")
  elif selection == '2': 
    os.system("curl -s -X GET -H 'Accept: application/json' http://146.148.26.129:8080/containers?state=running | python -mjson.tool")
  elif selection == '3':
    id=raw_input("Please Enter Container ID:") 
    os.system("curl -s -X GET -H 'Accept: application/json' http://146.148.26.129:8080/containers/%s" % id)
  elif selection == '4': 
    id=raw_input("Enter Container ID:") 
    os.system("curl -s -X GET -H 'Accept: application/json' http://146.148.26.129:8080/containers/%s/logs" % id)
  elif selection == '5':
    os.system("curl -s -X GET -H 'Accept: application/json' http://146.148.26.129:8080/images | python -mjson.tool")
  elif selection == '6': 
    os.system("curl -H 'Accept: application/json' -F file=@Dockerfile http://146.148.26.129:8080/images")
  elif selection == '7':
    id=raw_input("Enter Image ID:")
    os.system("curl -X POST -H 'Content-Type: application/json' http://146.148.26.129:8080/containers -d '{\"image\": \"%s\"}'" % id)
  elif selection == '8': 
	id=raw_input("Enter Container ID:") 
	os.system("curl -X PATCH -H 'Content-Type: application/json' http://146.148.26.129:8080/containers/%s" % id
  elif selection == '9':
    id=raw_input("Please Enter Image ID:")
    os.system("curl -s -X PATCH -H 'Content-Type: application/json' http://146.148.26.129:8080/images/%s -d '{\"tag\": \"test:1.0\"}'" % id)
  elif selection == '10': 
    id=raw_input("Please Enter Image ID:")
    os.system("curl -s -X DELETE -H 'Accept: application/json' http://146.148.26.129:8080/images/%s" % id)
  elif selection == '11':
    os.system("curl -s -X DELETE -H 'Accept: application/json' http://146.148.26.129:8080/containers")
  elif selection == '12': 
    id=raw_input("Please Enter Image ID:")
    os.system("curl -s -X DELETE -H 'Accept: application/json' http://146.148.26.129:8080/images/%s" % id)
  elif selection == '13':
    os.system("curl -s -X DELETE -H 'Accept: application/json' http://146.148.26.129:8080/images")
  elif selection == '14': 
    break
  else: 
    print "Unknown Option Selected!" 