import csv
import os
from clients.models import Client

class ClientService:

    def __init__(self,table_name):
        self.table_name = table_name
    
    def create_client(self,client):
        with open(self.table_name, mode = 'a') as f:
            writer = csv.DictWriter(f, fieldnames = Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode = 'r') as f:
            reader = csv.DictReader(f,fieldnames= Client.schema())
            return list(reader)

    def update_client(self,updated_client):
        clients = self.list_clients()
        
        update_clients = []
        for client in clients:
            if client['uid'] == updated_client.uid:
                update_clients.append(updated_client.to_dict())
            else:
                update_clients.append(client)

        self.save_to_disk(update_clients)
        
    def delete_client(self,deleted_client):
        clients = self.list_clients()
        saved_client = []
        for client in clients:
            if client['uid'] != deleted_client.uid:
                saved_client.append(client)

        self.save_to_disk(saved_client)

    def save_to_disk(self,clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name,'a') as f:
            writer = csv.DictWriter(f, fieldnames = Client.schema())
            print(clients)
            writer.writerows(clients)
        os.remove(self.table_name)
        os.rename(tmp_table_name,self.table_name)

    
    