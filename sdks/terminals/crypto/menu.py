import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



import sqlite3
# Connect to the database
conn = sqlite3.connect('crypto.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()


def menu():
    # SQLite database connection
    conn = sqlite3.connect('terminals/crypto/crypto.db')

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()
    while True:
        # Display the menu options
        print('What do you want to do?')
        print('1. View all RSI values')
        print('2. View RSI value for a specific symbol')
        print('3. Exit')
        
        # Get user input
        choice = input('> ')
        
        # Execute the selected command
        if choice == '1':
            # View all RSI values
            cur.execute('SELECT * FROM rsi')
            rows = cur.fetchall()
            print(f'Symbol\tRSI Value')
            for row in rows:
                print(f'{row[0]}\t{row[1]}')
        elif choice == '2':
            # View RSI value for a specific symbol
            symbol = input('Enter the symbol: ').upper()
            cur.execute('SELECT rsi_value FROM rsi WHERE symbol = ?', (symbol,))
            row = cur.fetchone()
            if row is None:
                print('Symbol not found')
            else:
                print(f'RSI value for {symbol}: {row[0]}')
        elif choice == '3':
            # Exit the program
            break
        else:
            # Invalid input
            print('Invalid choice')
    
    # Close the database connection
    conn.close()

# Call the menu function to start the program
menu()
