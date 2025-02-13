# NeoPortal

NeoPortal is a Python-based application designed to track and display detailed task information and system usage statistics for Windows systems. This tool helps you manage your computer's resources efficiently by providing insights into running processes and overall system performance.

## Features

- Displays a list of current processes with details such as PID, name, CPU usage, memory usage, and status.
- Provides real-time system usage statistics including CPU, memory, and disk usage percentages.
- Automatically updates every 5 seconds to ensure up-to-date information.

## Requirements

- Python 3.x
- `psutil` library
- `prettytable` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/neoportal.git
   ```

2. Navigate to the project directory:
   ```bash
   cd neoportal
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the `neoportal.py` script to start tracking tasks and system usage:

```bash
python neoportal.py
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [psutil](https://github.com/giampaolo/psutil) for process and system usage data.
- [PrettyTable](https://github.com/jazzband/prettytable) for tabular data representation.