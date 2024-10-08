
# Firebase Populator

A Python package to populate Firebase Firestore with generated data. This package helps you easily insert multiple entries into a specified Firestore collection based on a provided data template.

## Installation

To install the package, use pip:

```bash
pip install firebase-populator
```

## Requirements

Make sure to have the `firebase-admin` library installed, which is automatically included as a dependency.

## Usage

### Initialization

You need to initialize the `FirebasePopulator` with your Firebase service account credentials. Obtain these credentials from your Firebase project settings.

### Example

Here’s how to use the `FirebasePopulator` class:

```python
from firebase_populator import FirebasePopulator

# Define the path to your Firebase credentials JSON file
credential_file_path = 'path/to/your/firebase/credentials.json'

# Define the Firestore collection name
collection_name = 'your_collection'

# Define a data template for the entries to be added
data_template = {
    'field1': lambda i: f'value_{i}',  # Generates unique values based on the index
    'field2': 'static_value',           # Static value for all entries
    'field3': lambda i: i * 2           # Generates values that are twice the index
}

# Initialize and populate Firestore
populator = FirebasePopulator(credential_file=credential_file_path)
populator.initialize_firebase()  # Initialize Firebase
populator.populate_firestore(collection_name, data_template, num_entries=5)  # Populate Firestore
```

### Parameters

- **`credential_file`**: Path to the Firebase service account key (JSON).
- **`database_url`** (optional): Specify if using Realtime Database.
- **`collection_name`**: Name of the Firestore collection to populate.
- **`data_template`**: A dictionary template representing the data, where values can be static or generated using a function.
- **`num_entries`**: Number of entries to insert into the database.

### Logging

The package uses Python's logging module to log the initialization status and data insertion process. You can configure logging settings as needed.

## License

This package is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

### Key Sections Explained:
- **Installation**: How to install your package using pip.
- **Usage**: Detailed example showing how to set up and use the `FirebasePopulator` class, including parameter explanations.
- **Logging**: Mentions that logging is used, providing insight into how users can monitor the process.
- **License and Contributing**: Standard sections for open-source projects.

Feel free to modify any parts to better match your style or additional features you may want to highlight! Let me know if you need further assistance!