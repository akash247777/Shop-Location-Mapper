# 🗺️ Shop Location Mapper

A streamlined web application that helps you map shop locations using coordinates from an Excel file. Find shops instantly and view their locations on Google Maps!https://github.com/user-attachments/assets/6a851d37-47be-4f97-af15-c255295080b3



https://github.com/user-attachments/assets/864522d6-31e2-4195-aba6-5e001d12922e



Demo Video Link - https://drive.google.com/file/d/1ObdJt1H0PJxwMBep6wRlbwIvlnCITTfh/view?usp=drive_link
## ✨ Features

- 📊 Excel file validation and data processing
- 🔍 Quick shop location search by ID
- 🌎 Seamless Google Maps integration
- 🖥️ Clean, interactive web interface using Streamlit
- ⚡ Robust error handling and data validation

## 🚀 Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## ⚙️ Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/shop-location-mapper.git
cd shop-location-mapper
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

### Required Packages 📦
- streamlit
- pandas
- openpyxl

## 📝 Data Format

The application expects an Excel file named "lat & long.xlsx" with these columns:
| Column | Description |
|--------|-------------|
| SHOPID | Unique identifier for each shop |
| SHOPNAME | Name of the shop |
| LATITUDE | Geographical latitude |
| LONGITUDE | Geographical longitude |

## 🎯 Usage

1. Place your Excel file named "lat & long.xlsx" in the same directory as the script.

2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. The application will open in your default web browser.

4. Enter a shop ID in the search box and click "Show Location" to view the shop's details and location on Google Maps.

## 🛡️ Error Handling

The application handles various scenarios gracefully:
- 📁 Missing or invalid Excel files
- ❌ Missing required columns
- 🌐 Invalid coordinate data
- 🔎 Non-existent shop IDs

## 👥 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests


## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io) 🎈
- Powered by [pandas](https://pandas.pydata.org) 🐼
- Integrates with [Google Maps](https://maps.google.com) 🗺️

---

<div align="center">
    
⭐ Star this repository if you find it helpful! ⭐

</div>
