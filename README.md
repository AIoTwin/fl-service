# Hands on Part I.
# Hierarchical FL with Flower Framework

## Task 1. - Standard Federated Learning setup with Flower
**Setup**:
```
Flower Server:                              (hfl-n1, "10.19.4.113:8080")

Flower Clients     (hfl-n4) (hfl-n5) (hfl-n6) (hfl-n7) (hfl-n8) (hfl-n9) (hfl-n10) (hfl-n11) (hfl-n12) (hfl-n13)
```
**Task structure**:  
```
├── task1 
│   └── client.py  
│   └── task.py
```

&nbsp;  
**Steps**:
1. Move into the task1 directory
```
cd aiotwin-tutorial/task1
```
2. In client.py set the server address and number of training epochs

3. Start Flower client:
```
python3 client.py
```
&nbsp;&nbsp;&nbsp; Expected output:
```
INFO flwr 2025-06-15 17:22:45,642 | grpc.py:52 | Opened insecure gRPC connection (no certificates were passed)
2025-06-15 17:22:45 | INFO | Opened insecure gRPC connection (no certificates were passed)
DEBUG flwr 2025-06-15 17:22:45,669 | connection.py:55 | ChannelConnectivity.IDLE
2025-06-15 17:22:45 | DEBUG | ChannelConnectivity.IDLE
DEBUG flwr 2025-06-15 17:22:45,670 | connection.py:55 | ChannelConnectivity.CONNECTING
2025-06-15 17:22:45 | DEBUG | ChannelConnectivity.CONNECTING
DEBUG flwr 2025-06-15 17:22:45,674 | connection.py:55 | ChannelConnectivity.READY
2025-06-15 17:22:45 | DEBUG | ChannelConnectivity.READY
```

&nbsp;  
&nbsp;  

## Task 2. - Hierarhical Federated Learning setup with Flower
**Setup**:
```
Flower Global Server:                                        (hfl-n1, "10.19.4.113:8080")

Flower Local Server            (hfl-n2, "10.19.4.119:8080")                                   (hfl-n3, "10.19.4.201:8080")

Flower Clients      (hfl-n4) (hfl-n5) (hfl-n6) (hfl-n7) (hfl-n8)                   (hfl-n9) (hfl-n10) (hfl-n11) (hfl-n12) (hfl-n13)
```
**Task structure**: 
```
├── task2  
│   └── client.py  
│   └── client_config.yaml  
│   └── task.py
```
  
&nbsp;  
**Steps**:
1. Move into the task2 directory
```
cd aiotwin-tutorial/task2
```
2. In client_config.yaml set the local server address and number of training epochs

3. Start Flower client:
```
python3 client.py
```
&nbsp;&nbsp;&nbsp; Expected output:
```
INFO flwr 2025-06-15 17:28:18,934 | grpc.py:52 | Opened insecure gRPC connection (no certificates were passed)
2025-06-15 17:28:18 | INFO | Opened insecure gRPC connection (no certificates were passed)
DEBUG flwr 2025-06-15 17:28:18,936 | connection.py:55 | ChannelConnectivity.IDLE
2025-06-15 17:28:18 | DEBUG | ChannelConnectivity.IDLE
DEBUG flwr 2025-06-15 17:28:18,940 | connection.py:55 | ChannelConnectivity.CONNECTING
2025-06-15 17:28:18 | DEBUG | ChannelConnectivity.CONNECTING
DEBUG flwr 2025-06-15 17:28:18,941 | connection.py:55 | ChannelConnectivity.READY
2025-06-15 17:28:18 | DEBUG | ChannelConnectivity.READY
```

