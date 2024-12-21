import pandas as pd
import webbrowser
import urllib.parse

try:
    import streamlit as st
except ModuleNotFoundError:
    raise ImportError("The 'streamlit' package is required but not installed. Install it using 'pip install streamlit'.")

# Function to load and validate the Excel file
def load_excel_file(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Validate required columns
        required_columns = ['SHOPID', 'SHOPNAME', 'LATITUDE', 'LONGITUDE']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        # Convert LATITUDE and LONGITUDE to numeric, coercing errors to NaN
        df['LATITUDE'] = pd.to_numeric(df['LATITUDE'], errors='coerce')
        df['LONGITUDE'] = pd.to_numeric(df['LONGITUDE'], errors='coerce')

        # Remove rows with NaN values in latitude or longitude
        df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

        # Convert SHOPID to string to ensure compatibility
        df['SHOPID'] = df['SHOPID'].astype(str)

        if df.empty:
            raise ValueError("No valid coordinates found in the file")

        return df
    except Exception as e:
        raise RuntimeError(f"Error loading file: {e}")

# Function to open Google Maps with specific coordinates
def open_google_maps(latitude, longitude):
    query_params = urllib.parse.urlencode({
        'q': f'{latitude},{longitude}',
        'z': '15'  # Zoom level
    })
    google_maps_url = f'https://www.google.com/maps/search/?{query_params}'
    webbrowser.open(google_maps_url)

# Main Streamlit App
def main():
    st.title("Shop Location Mapper")

    # Hardcoded file path for the Excel file
    file_path = "lat & long.xlsx"

    try:
        # Load Excel data
        df = load_excel_file(file_path)
        st.success("File loaded successfully!")

        # Search for a specific shop
        st.subheader("Find a Shop by ID")
        shop_id = st.text_input("Enter Shop ID")
        if st.button("Show Location"):
            shop = df[df['SHOPID'] == shop_id]

            if not shop.empty:
                shop_row = shop.iloc[0]
                latitude = shop_row['LATITUDE']
                longitude = shop_row['LONGITUDE']
                shop_name = shop_row['SHOPNAME']

                st.write(f"**Shop ID**: {shop_id}, **Name**: {shop_name}")
                map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
                st.write(f"[Open in Google Maps]({map_url})")
            else:
                st.error("Shop ID not found")
    except RuntimeError as e:
        st.error(str(e))

if __name__ == "__main__":
    main()
