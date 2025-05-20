import yaml
import sys
import torch
import flwr as fl

from task import Net, get_weights, load_data, set_weights, test, train

class FlowerClient(fl.client.NumPyClient):
    def __init__(self, trainloader, valloader, local_epochs, learning_rate):
        self.net = Net()
        self.trainloader = trainloader
        self.valloader = valloader
        self.local_epochs = local_epochs
        self.lr = learning_rate
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def fit(self, parameters, config):
            """Train the model with data of this client."""
            set_weights(self.net, parameters)
            results = train(
                self.net,
                self.trainloader,
                self.valloader,
                self.local_epochs,
                self.lr,
                self.device,
            )
            return get_weights(self.net), len(self.trainloader.dataset), results
    
    def evaluate(self, parameters, config):
        """Evaluate the model on the data this client has."""
        set_weights(self.net, parameters)
        loss, accuracy = test(self.net, self.valloader, self.device)
        return loss, len(self.valloader.dataset), {"accuracy": accuracy,"loss":loss}
# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    
    with open("client_config.yaml", 'r') as file:
        config = yaml.safe_load(file)
   
    partition_id = config["node_config"]["partition-id"]
    num_partitions = config["node_config"]["num-partitions"]

    batch_size = config["run_config"]["batch-size"]
    local_epochs = config["run_config"]["local-epochs"]
    learning_rate = config["run_config"]["learning-rate"]

    server_address = config["server"]["address"]
    trainloader, valloader = load_data(partition_id, num_partitions, batch_size)


    client = FlowerClient(trainloader, valloader, local_epochs, learning_rate).to_client()

    fl.client.start_numpy_client(server_address=server_address, client=client)
