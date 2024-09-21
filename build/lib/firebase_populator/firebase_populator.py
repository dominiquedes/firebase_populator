# firebase_populator.py

import firebase_admin
from firebase_admin import credentials, firestore
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FirebasePopulator:
    def __init__(self, credential_file, database_url=None):
        """
        Initialize Firebase connection.
        
        :param credential_file: Path to the Firebase service account key (JSON).
        :param database_url: Optional; specify if using Realtime Database.
        """
        self.credential_file = credential_file
        self.database_url = database_url
        self.firebase_initialized = False
        self.db = None

    def initialize_firebase(self):
        """
        Initializes Firebase app with the provided credentials.
        """
        try:
            cred = credentials.Certificate(self.credential_file)
            if self.database_url:
                firebase_admin.initialize_app(cred, {"databaseURL": self.database_url})
            else:
                firebase_admin.initialize_app(cred)
            self.db = firestore.client()  # Firestore
            self.firebase_initialized = True
            logging.info("Firebase successfully initialized.")
        except Exception as e:
            logging.error(f"Error initializing Firebase: {e}")

    def populate_firestore(self, collection_name, data_template, num_entries):
        """
        Populates Firebase Firestore database with generated data.
        
        :param collection_name: Name of the Firestore collection to populate.
        :param data_template: A dictionary template representing the data.
        :param num_entries: Number of entries to insert into the database.
        """
        if not self.firebase_initialized:
            logging.error("Firebase is not initialized. Please call `initialize_firebase` first.")
            return

        try:
            collection_ref = self.db.collection(collection_name)
            for i in range(num_entries):
                # Generate data for each entry
                data = {k: v if not callable(v) else v(i) for k, v in data_template.items()}
                collection_ref.add(data)
                logging.info(f"Inserted entry {i+1}: {data}")
            logging.info(f"Successfully added {num_entries} entries to the collection '{collection_name}'.")
        except Exception as e:
            logging.error(f"Error populating Firestore: {e}")


# Example usage:
if __name__ == '__main__':
    credential_file_path = 'path/to/your/firebase/credentials.json'
    collection_name = 'your_collection'
    data_template = {
        'field1': lambda i: f'value_{i}',
        'field2': 'static_value',
        'field3': lambda i: i * 2
    }
    
    # Initialize and populate Firestore
    populator = FirebasePopulator(credential_file=credential_file_path)
    populator.initialize_firebase()
    populator.populate_firestore(collection_name, data_template, num_entries=5)