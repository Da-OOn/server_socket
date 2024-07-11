# Socket Communication

This repository contains two Python scripts for demonstrating socket communication between a client and a server. The client executes a Python script (`main_cache.py`) and sends the results to the server. This repository is for team Jaegal-DulDul!

## Files

- `client.py`: The client script that executes `main_cache.py` and sends its output to the server.
- `server.py`: The server script that receives data from the client and prints it.

## Usage

### Conda Virtual Environment

You can use an existing conda virtual environment to manage dependencies. Follow the steps below to activate your conda environment:

1. Activate the environment:

    ```bash
    conda activate your_existing_env
    ```

    Replace `your_existing_env` with the name of your conda environment.

### Server

1. Run the server script on the machine that will receive the data:

    ```bash
    python server.py
    ```

    The server will start listening for incoming connections on `0.0.0.0` and port `12345`.

### Client

1. Before running the client script, make sure to update the `host` variable in `client.py` to the IP address of the machine where the server script is running:

    ```python
    host = '192.168.0.3'  # Replace with the server's IP address
    ```

2. Run the client script:

    ```bash
    python client.py
    ```

    The client will execute `main_cache.py` and send the output to the server.

### Note

- Make sure both the client and server are on the same network or that the server is accessible from the client's network.
- Ensure that the port `12345` is open and not blocked by any firewall or security group settings.

## Example

### Server Output

```bash
Server is listening...
Connected by ('192.168.0.2', 54321)
Received result: <output from main_cache.py>
