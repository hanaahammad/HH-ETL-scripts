import numpy as np
import pandas as pd
import streamlit as st
import random

from faker import Faker

st.header("Dataframe interactive")
@st.cache_data

def get_profile_dataset(number_of_items: int = 20, seed: int = 0) -> pd.DataFrame:
    new_data = []

    fake = Faker()
    random.seed(seed)
    Faker.seed(seed)

    for i in range(number_of_items):
        profile = fake.profile()
        new_data.append(
            {
                "name": profile["name"],
                "daily_activity": np.random.rand(25),
                "activity": np.random.randint(2, 90, size=12),
            }
        )

    profile_df = pd.DataFrame(new_data)
    return profile_df


st.dataframe(get_profile_dataset())

st.header('Display your data with multi-row selections enabled')

column_configuration = {
    "name": st.column_config.TextColumn(
        "Name", help="The name of the user", max_chars=100, width="medium"
    ),
    "activity": st.column_config.LineChartColumn(
        "Activity (1 year)",
        help="The user's activity over the last 1 year",
        width="large",
        y_min=0,
        y_max=100,
    ),
    "daily_activity": st.column_config.BarChartColumn(
        "Activity (daily)",
        help="The user's activity in the last 25 days",
        width="medium",
        y_min=0,
        y_max=1,
    ),
}
st.header("All members")
df = get_profile_dataset()

event = st.dataframe(
    df,
    column_config=column_configuration,
    use_container_width=True,
    hide_index=True,
    on_select="rerun",
    selection_mode="multi-row",
)


st.header("Selected members")
people = event.selection.rows
filtered_df = df.iloc[people]
st.dataframe(
        filtered_df,
        column_config=column_configuration,
        use_container_width=True,
    )

activity_df = {}
for person in people:
    activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]

activity_df = pd.DataFrame(activity_df)
daily_activity_df = {}
for person in people:
    daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
daily_activity_df = pd.DataFrame(daily_activity_df)

st.dataframe(activity_df)
st.dataframe(daily_activity_df)


if len(people) > 0:
    st.header("Daily activity comparison")
    st.bar_chart(daily_activity_df)
    st.header("Yearly activity comparison")
    st.line_chart(activity_df)
else:
    st.markdown("No members selected.")