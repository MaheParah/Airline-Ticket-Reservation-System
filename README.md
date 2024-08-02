# Airline-Ticket-Reservation-System

## Project Overview
This project is an Airline Ticket Reservation System created using Tkinter in Python. The application allows users to input passenger details, travel details, and food preferences, and generates a ticket with the entered information. It also includes functionality to verify travel details, calculate distances, and display ticket prices.

## Features
- Input passenger details (name, contact number, date).
- Select source and destination from predefined countries.
- Input number of tickets and food preferences (vegetarian, non-vegetarian, vegan, gluten-free, diabetic, baby meal).
- Verify travel details and calculate distances.
- Generate and display a ticket with all the entered details.
- Save the ticket as a text file.
- Clear the input fields and reset the form.
- Exit the application.

## Requirements
- Python 3.x
- Tkinter library (usually included with Python)
- SQLite3 (for database operations)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/airline-ticket-reservation-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd airline-ticket-reservation-system
   ```
3. Install the required dependencies:
   ```bash
   pip install tk
   ```

## How to Run
1. Ensure you have Python 3.x installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the Python script:
   ```bash
   python airline_ticket_reservation.py
   ```
5. The application window will open, allowing you to input passenger details, select travel details, and generate a ticket.

## How to Use
1. **Passenger Details:**
   - Enter the passenger's name and contact number.
   - Select the date of travel.
2. **Travel Details:**
   - Select the source and destination from the dropdown menus.
   - Enter the number of tickets required.
3. **Food Preferences:**
   - Enter the quantities for each type of meal (vegetarian, non-vegetarian, vegan, gluten-free, diabetic, baby meal).
4. **Actions:**
   - Click the **Check** button to verify the travel details and calculate the distance.
   - Click the **Submit** button to save the data into the database.
   - Click the **Generate Ticket** button to create and display the ticket.
   - Click the **Reset** button to clear the form.
   - Click the **Exit** button to close the application.

## Database
The project uses SQLite3 for database operations. A table named `prernaairlines` is created to store the following information:
- Name
- Contact
- Date
- Source
- Destination
- Number of Tickets
- Vegetarian Meal
- Non-Vegetarian Meal
- Vegan Meal
- Gluten-Free Meal
- Diabetic Meal
- Baby Meal

## Contribution
If you want to contribute to this project, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please contact [your-email@example.com](mailto:your-email@example.com).
