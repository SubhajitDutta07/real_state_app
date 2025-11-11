import streamlit as st
import pickle
import pandas as pd
import re

st.set_page_config(page_title="Recommend Appartments")

location_df = pickle.load(open('/Users/sencer07/Desktop/DataScience/Projects/real-estate-app/pages/location_distance_.pkl', 'rb'))

st.title("Select Location and radius")

cosine_sim1 = pickle.load(open('/Users/sencer07/Desktop/DataScience/Projects/real-estate-app/pages/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('/Users/sencer07/Desktop/DataScience/Projects/real-estate-app/pages/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('/Users/sencer07/Desktop/DataScience/Projects/real-estate-app/pages/cosine_sim3.pkl', 'rb'))


def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()
    return pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })


selected_location = st.selectbox('Location', sorted(location_df.columns.to_list()))
radius = st.number_input('Radius in Kms')

if st.button('Search'):
    apartment=[]
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()
    for key, value in result_ser.items():
        apartment.append(f"{key} ---> {round(value / 1000)} kms")
    st.session_state['apartment_list'] = apartment  # store in session state

# Only show apartment selectbox if we already have results
if 'apartment_list' in st.session_state:
    st.subheader('Recommend Appartments')
    selected_apt = st.selectbox(
        'Select anyone for recommendations based on your search on distance',
        st.session_state['apartment_list']
    )

    # Extract the property name
    selected_property = selected_apt.split('--->')[0].strip()

    if st.button('Recommend'):
        recommendation_df = recommend_properties_with_scores(selected_property)
        st.dataframe(recommendation_df)
