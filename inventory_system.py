"""
Inventory Management System

Provides utilities to add, remove, save, load, and report stock levels.
Ensures proper validation, error handling, and PEP8 compliance.
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    filename="inventory.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Global stock data
stock_data: Dict[str, float] = {}


def add_item(item: str, qty: float, logs: Optional[List[str]] = None) -> None:
    """
    Add a quantity of an item to the inventory.

    Args:
        item: The item name (string).
        qty: Quantity to add (non-negative number).
        logs: Optional list to record log entries.

    Raises:
        ValueError: If item name or quantity is invalid.
    """
    if not isinstance(item, str) or not item.strip():
        raise ValueError("Item must be a non-empty string.")
    if not isinstance(qty, (int, float)) or qty < 0:
        raise ValueError("Quantity must be a non-negative number.")

    stock_data[item] = stock_data.get(item, 0.0) + float(qty)
    timestamp = datetime.now().isoformat()
    logging.info("Added %.2f of %s", qty, item)

    if logs is not None:
        logs.append(f"{timestamp}: Added {qty} of {item}")


def remove_item(item: str, qty: float) -> None:
    """
    Remove a quantity of an item from the inventory.

    Args:
        item: The item name.
        qty: Quantity to remove (positive number).

    Raises:
        ValueError: If item or quantity is invalid, or insufficient stock.
        KeyError: If the item is not found.
    """
    if not isinstance(item, str) or not item.strip():
        raise ValueError("Item must be a non-empty string.")
    if not isinstance(qty, (int, float)) or qty <= 0:
        raise ValueError("Quantity must be a positive number.")
    if item not in stock_data:
        raise KeyError(f"Item '{item}' not found in inventory.")

    new_qty = stock_data[item] - float(qty)
    if new_qty < 0:
        raise ValueError(
            f"Insufficient stock for '{item}'. "
            f"Available: {stock_data[item]}, Tried to remove: {qty}"
        )

    if new_qty == 0:
        del stock_data[item]
        logging.info("Removed %.2f of %s (deleted at zero).", qty, item)
    else:
        stock_data[item] = new_qty
        logging.info("Removed %.2f of %s (new qty: %.2f).", qty, item, new_qty)


def get_qty(item: str) -> float:
    """
    Get the current quantity of an item.

    Args:
        item: The item name.

    Returns:
        The quantity of the item.

    Raises:
        KeyError: If the item does not exist.
    """
    return float(stock_data[item])


def save_data(file_path: str = "inventory.json") -> None:
    """
    Save the current stock data to a JSON file.

    Args:
        file_path: The path to save the file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(stock_data, file, indent=2, ensure_ascii=False)
    logging.info("Saved %d items to %s", len(stock_data), file_path)


def load_data(file_path: str = "inventory.json") -> None:
    """
    Load stock data from a JSON file.

    Args:
        file_path: The path to the inventory file.

    Raises:
        ValueError: If the file contains invalid data.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("Inventory file must contain a JSON object.")

    stock_data.clear()
    for key, value in data.items():
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            raise ValueError("Inventory must map strings to numeric values.")
        stock_data[key] = float(value)

    logging.info("Loaded %d items from %s", len(stock_data), file_path)


def print_data() -> None:
    """Print all items and their quantities."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold: float = 5) -> List[str]:
    """
    Return items whose quantity is below a given threshold.

    Args:
        threshold: The numeric threshold.

    Returns:
        List of items below the threshold.

    Raises:
        ValueError: If threshold is invalid.
    """
    if not isinstance(threshold, (int, float)) or threshold < 0:
        raise ValueError("Threshold must be a non-negative number.")

    return [item for item, qty in stock_data.items() if qty < threshold]


def main() -> None:
    """Demonstrate inventory system functionality."""
    logs: List[str] = []

    add_item("apple", 10, logs)
    add_item("banana", 3, logs)
    remove_item("apple", 2)

    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())

    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
