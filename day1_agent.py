def my_agent(sensor_input):
    print("Someone is coming")
    if sensor_input=="Movement":
        return "Action: Open the door"
    else:
        return "Action: Close the door"
# 1. We create the 'percept' (The data coming from the sensor)
# Use one '=' to assign the value
current_sensor_data = "Movement" 

# 2. We 'call' the agent and give it the data
# We store the agent's decision in a variable called 'result'
result = my_agent(current_sensor_data)

# 3. We print the result to the screen
print(result)
