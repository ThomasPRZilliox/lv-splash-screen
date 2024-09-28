import zmq
import json

def send_stop_message():
    # Create a new ZeroMQ context
    context = zmq.Context()

    # Create a REQ socket (Request)
    socket = context.socket(zmq.REQ)

    # Connect to the server socket (change address/port if needed)
    socket.connect("tcp://localhost:5555")

    # Create a JSON object with the message
    data = {"message": "stop"}
    json_data = json.dumps(data)

    # Send the JSON message
    print("Sending JSON message...")
    socket.send_string(json_data)

    # Wait for the reply (for REQ-REP, the client needs to wait for a reply)
    reply = socket.recv_string()
    print(f"Received reply: {reply}")

if __name__ == "__main__":
    send_stop_message()
