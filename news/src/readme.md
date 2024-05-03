# Fars News Web Scraping

This Python script is designed for web scraping news articles from the [Fars News](https://www.farsnews.ir) website. It provides the ability to collect news articles from different categories, such as politics, sports, social, economy, culture, and arts-media. The extracted data, including article titles, text, publication dates, and labels, are stored in a CSV file for further analysis or usage.

## Prerequisites

Before running this code, ensure that you have the following prerequisites:

- Python 3.x installed on your system.
- Required Python libraries installed. You can install these libraries using `pip` if not already installed:
  - BeautifulSoup
  - requests
  - pandas

## Usage

1. Clone or download the code repository to your local machine.

2. Open a command prompt or terminal and navigate to the directory where the script is located.

3. Run the script using the following command:

   ```shell

   git clone https://github.com/parvvaresh/Iranian-news-dataset/tree/main/get_data
   pip install BeautifulSoup
   pip install requests
   pip install pandas
   python3 fars_news.py
   ```

4. The script will prompt you to enter the start and finish page numbers for data collection. These page numbers correspond to the page numbers on the Fars News website for the specified categories.

5. The script will initiate the web scraping process and display progress messages as it collects and processes the data.

6. Once the web scraping is complete, the script will save the extracted data to a CSV file named `farsnews.csv` in the same directory as the script.

7. After successful execution, you can access the collected data in the CSV file for analysis or any other purpose.

## Important Notes

- This script is for educational and informational purposes only. Web scraping may be subject to legal and ethical restrictions. Ensure that your usage complies with the website's terms of service and applicable laws.

- The provided script has some limitations and may require improvements for robust error handling and to address potential issues.

## Acknowledgments

- The script was created for educational purposes and is not affiliated with or endorsed by the Fars News website.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Author

[Alireza Parvaresh](https://www.linkedin.com/in/parvvaresh/)

## special thanks to : 
[Elham Ghassemi](https://www.linkedin.com/in/elham-ghasemi-5a258058/)

[Golshid Ranjbaran](https://www.linkedin.com/in/golshid-ranjbaran-544a2115a/)

[Faeezeh Gholamrezaee](https://github.com/faezeh-gholamrezaie)


## Contact

If you have any questions or feedback, please feel free to contact [parvvaresh@gmail.com].


