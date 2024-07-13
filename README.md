# Olympics Data Analysis App

This project is a Streamlit web application for analyzing Olympic data. It provides various functionalities to explore and visualize the Olympic dataset, which includes athlete information and medal counts from different countries and seasons.

## Features

- **Season-wise Analysis**: Analyze data for both Summer and Winter Olympics separately.
- **Medal Tally**: View the medal tally for all countries, sorted by Gold, Silver, and Bronze medals.
- **Country-wise Search**: Search for a specific country and view its medal tally.
- **Year-wise Analysis**: Explore the medal distribution for a selected year and country.
- **Year-wise Progress**: Analyze the progress of a country over the years in terms of medals won.

## Dataset

The data used in this application includes two CSV files:
1. `athlete_events.csv`: Contains information about athletes and their performance in different Olympic events.
2. `noc_regions.csv`: Contains information about National Olympic Committees (NOCs) and their corresponding regions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/Olympics-Data-Analysis.git
    cd Olympics-Data-Analysis
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Select the season (Summer or Winter) from the sidebar menu.
2. Choose an analysis option:
    - **Medal Tally**: View the medal tally for all countries.
    - **Country-wise**: Search for a specific country's medal tally.
    - **Year-wise**: View medal distribution for a selected year and country.
    - **Year-wise Progress**: Analyze a country's progress over the years.

3. Interact with the visualizations and explore the data.

## Project Structure

.
├── data
│ ├── athlete_events.csv
│ └── noc_regions.csv
├── helpers.py
├── app.py
├── README.md
└── requirements.txt


- `data/`: Directory containing the dataset.
- `helpers.py`: Contains helper functions for data preprocessing and visualization.
- `app.py`: Main Streamlit application script.
- `README.md`: Project description and instructions.
- `requirements.txt`: List of required Python packages.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
