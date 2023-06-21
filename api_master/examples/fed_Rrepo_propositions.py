import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import pandas as pd
import requests
session = requests.session()








def repo_propositions():
        """Check all repo & reverse repo operations out of the FED."""
        propositions = session.get("https://markets.newyorkfed.org/api/rp/reverserepo/propositions/search.json").json()

        repo = propositions['repo']
        operations = repo['operations']
        data = []
        for operation in operations:
            operation_id = operation['operationId']
            operation_date = operation['operationDate']
            operation_type = operation['operationType']
            note = operation['note']
            total_amt_accepted = operation['totalAmtAccepted']
            
            data.append({
                'Operation ID': operation_id,
                'Operation Date': operation_date,
                'Operation Type': operation_type,
                'Note': note,
                'Total Amount Accepted': total_amt_accepted
            })

        df = pd.DataFrame(data)
        return df



propositions = repo_propositions()
# Define the directory path
directory = 'files/fed_reserve/reverse_repo/'
# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)



# Define the file path
filename = f'{directory}all_propositions.csv'

propositions.to_csv(filename)