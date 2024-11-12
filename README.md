# Restaurant Management System

This Python-based **Restaurant Management System** allows users to view, add menus, place new orders, and view all orders. It uses basic file handling for storing and retrieving menu items and orders.

## Features

- **View Menu**: Display all available menu items from `Menu.txt`.
- **Add Menu**: Add new meals to the menu with meal name and cost.
- **New Order**: Place orders by selecting meal IDs and specifying quantities. Orders are saved in `Orders.txt`.
- **View Orders**: Display all past orders with customer names and total payments.
- **Exit**: Close the system gracefully.

## How It Works

### Menu Management
- The menu is stored in `Menu.txt`.
- Each menu item has an ID, name, and cost.
- Users can view and add new menu items.

### Order Management
- Orders are stored in `Orders.txt`.
- Users can place orders by providing their name and selecting meal IDs.
- The system calculates the total cost of the order.
- Users can place multiple orders or view all past orders.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd restaurant-management-system
   ```
3. - Ensure `Menu.txt` and `Orders.txt` exist:
   - Create `Menu.txt` and `Orders.txt` files in the project directory if they do not exist.

## Usage

1. **Run the Program**:
   ```bash
   python restaurant_management.py
   ```
2. **Follow the On-Screen Prompts**:
   - Choose options from the menu to view, add, or order items.

## File Structure

- `restaurant_management.py`: Main script.
- `Menu.txt`: Stores menu items.
- `Orders.txt`: Stores customer orders.

## Example

**Menu.txt**:
```
001: 'Pizza' -> '8$'
002: 'Sushi' -> '12$'
```

**Orders.txt**:
```
Customer name: 'John Doe'  Total_Pay: '20$'
```

## Dependencies

- **Python 3.x**
- No external libraries required.

## Future Enhancements

- Add a GUI for better user experience.
- Integrate a database for improved data handling.
- Include error handling and validation improvements.

## License

This project is licensed under the MIT License.
