import redis
import json
# step 2: define our connection information for Redis
# Replaces with your configuration information
redis_host = '10.128.0.3'
redis_port = '6379'
redis_password = ""
def write_to_redis():
    input_data=[
    {
        "id" : "1",
        "Name": "Name1"
    },
    {
        "id" : "2",
        "Name": "Name2"
    },
    {
        "id" : "3",
        "Name": "Name3"
    },
    {
        "id" : "4",
        "Name": "Name4"
    },
    ]
    # Create the Redis Connection object
    try:
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        print('connection')
        r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True) 
    except Exception as e:
        print("Error in connecting to redis")
        print(e)
    for elem in input_data:
        id = elem['id']
        name = elem['Name']
        #json_data=json.loads(elem)
        # Set the message in Redis
        r.set(id, name)
        print("Entered " + str(input_data.index(line)) + "rows")
if __name__ == '__main__':
    write_to_redis()