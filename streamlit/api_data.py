import requests
import pandas as pd
import streamlit as st

# --- Page Config ---
st.set_page_config(layout="wide", page_title="Data Visualizer")
st.title("Streamlit — Paginated Dataset Viewer")

# --- Configuration & State ---
if 'api_data' not in st.session_state:
    st.session_state.api_data = None

api_region = st.selectbox('Select region', ('poland', "opole", "dolnoslaskie"))
base_url = "http://127.0.0.1:8000/api/map/" if api_region == 'poland' else f"http://127.0.0.1:8000/api/box/?region_name={api_region}"


# --- Data Collector ---
def collect_all_data(url):
    all_records = []
    next_url = url

    # UI Progress components
    container = st.container()
    progress_bar = container.progress(0)
    status_text = container.empty()

    try:
        while next_url:
            resp = requests.get(next_url)
            if resp.status_code != 200:
                st.error(f"API Error: {resp.status_code}")
                break

            data = resp.json()
            results = data.get("results", [])
            all_records.extend(results)

            next_url = data.get("next")
            total_count = data.get("count", len(all_records))

            status_text.text(f"Fetched {len(all_records)} / {total_count} records...")
            if isinstance(total_count, int) and total_count > 0:
                progress_bar.progress(min(len(all_records) / total_count, 1.0))

    except Exception as e:
        st.error(f"Connection Error: {e}")

    container.empty()
    return all_records


# --- Load Button ---
if st.button("Fetch Data from API"):
    with st.spinner("Downloading..."):
        data = collect_all_data(base_url)
        if data:
            st.session_state.api_data = pd.DataFrame(data)
            st.success(f"Loaded {len(st.session_state.api_data)} records successfully!")
        else:
            st.warning("No data returned from API.")

# --- Display Logic ---
if st.session_state.api_data is not None:
    df = st.session_state.api_data

    st.divider()

    # 1. Controls: Search and Page Size
    col_search, col_size = st.columns([3, 1])
    search_query = col_search.text_input("Search in all columns", "")
    page_size = col_size.selectbox("Rows per page", [10, 25, 50, 100], index=1)

    # 2. Filter data if search query exists
    if search_query:
        # Simple string matching across all columns
        mask = df.astype(str).apply(lambda x: x.str.contains(search_query, case=False)).any(axis=1)
        display_df = df[mask]
    else:
        display_df = df

    # 3. Pagination Math
    total_rows = len(display_df)
    if total_rows > 0:
        total_pages = (total_rows // page_size) + (1 if total_rows % page_size > 0 else 0)

        # UI for Page Selection
        col_prev, col_page, col_next = st.columns([1, 2, 1])
        current_page = col_page.number_input(f"Page 1 of {total_pages}", min_value=1, max_value=total_pages, step=1)

        # Slice Data
        start_idx = (current_page - 1) * page_size
        end_idx = start_idx + page_size

        # 4. Final Table Display
        st.dataframe(display_df.iloc[start_idx:end_idx], use_container_width=True)

        st.info(f"Showing rows {start_idx + 1} to {min(end_idx, total_rows)} of {total_rows}")

        # Download Option
        csv = display_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download current view as CSV", csv, "data_export.csv", "text/csv")
    else:
        st.info("No records match your search.")