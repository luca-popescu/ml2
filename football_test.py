import streamlit as st
import numpy as np
import joblib

# Load the pre-trained model
model = joblib.load("football.pkl")

# Title and introduction
st.title("Football Player Market Value Predictor")
st.write("Predict the market value of football players using detailed performance metrics.")

# Slider input fields
age = st.slider('Age', 10, 39, step=1)
matches_played = st.slider('Matches Played', 0, int(69 * 1.5), step=1)
minutes_played = st.slider('Minutes Played', 549, int(6580 * 1.5), step=1)
goals = st.slider('Goals', 0, int(52 * 1.5), step=1)
xG = st.slider('xG (Expected Goals)', 0.0, float(48.19 * 1.5), step=0.01)
assists = st.slider('Assists', 0, int(24 * 1.5), step=1)
xA = st.slider('xA (Expected Assists)', 0.0, float(24.13 * 1.5), step=0.01)
duels_per_90 = st.slider('Duels per 90', 0.15, float(34.84 * 1.5), step=0.01)
duels_won_percent = st.slider('Duels won, %', 0, 100, step=1)
height = st.slider('Height', 120, 201, step=1)
successful_defensive_actions_per_90 = st.slider('Successful defensive actions per 90', 1.0, float(13.09 * 1.5), step=0.01)
defensive_duels_per_90 = st.slider('Defensive duels per 90', 0.0, float(10.34 * 1.5), step=0.01)
defensive_duels_won_percent = st.slider('Defensive duels won, %', 0, 100, step=1)
aerial_duels_per_90 = st.slider('Aerial duels per 90', 0.0, float(13.17 * 1.5), step=0.01)
aerial_duels_won_percent = st.slider('Aerial duels won, %', 0, 100, step=1)
sliding_tackles_per_90 = st.slider('Sliding tackles per 90', 0.0, float(1.45 * 1.5), step=0.01)
shots_blocked_per_90 = st.slider('Shots blocked per 90', 0.0, float(1.35 * 1.5), step=0.01)
interceptions_per_90 = st.slider('Interceptions per 90', 0.69, float(7.89 * 1.5), step=0.01)
successful_attacking_actions_per_90 = st.slider('Successful attacking actions per 90', 0.0, float(11.51 * 1.5), step=0.01)
goals_per_90 = st.slider('Goals per 90', 0.0, float(0.92 * 1.5), step=0.01)
non_penalty_goals_per_90 = st.slider('Non-penalty goals per 90', 0.0, float(0.72 * 1.5), step=0.01)
shots = st.slider('Shots', 0, int(181 * 1.5), step=1)
goal_conversion_percent = st.slider('Goal conversion, %', 0, 100, step=1)
assists_per_90 = st.slider('Assists per 90', 0.0, float(0.49 * 1.5), step=0.01)
xA_per_90 = st.slider('xA per 90', 0.0, float(0.39 * 1.5), step=0.01)
crosses_per_90 = st.slider('Crosses per 90', 0.0, float(6.77 * 1.5), step=0.01)
accurate_crosses_percent = st.slider('Accurate crosses, %', 0, 100, step=1)
accurate_crosses_left_flank_percent = st.slider('Accurate crosses from left flank, %', 0, 100, step=1)
crosses_right_flank_per_90 = st.slider('Crosses from right flank per 90', 0.0, float(5.07 * 1.5), step=0.01)
accurate_crosses_right_flank_percent = st.slider('Accurate crosses from right flank, %', 0, 100, step=1)
successful_dribbles_percent = st.slider('Successful dribbles, %', 0, 100, step=1)
offensive_duels_per_90 = st.slider('Offensive duels per 90', 0.0, float(24.07 * 1.5), step=0.01)
offensive_duels_won_percent = st.slider('Offensive duels won, %', 0, 100, step=1)
progressive_runs_per_90 = st.slider('Progressive runs per 90', 0.0, float(6.66 * 1.5), step=0.01)
accurate_passes_percent = st.slider('Accurate passes, %', 0, 100, step=1)
accurate_forward_passes_percent = st.slider('Accurate forward passes, %', 0, 100, step=1)
accurate_back_passes_percent = st.slider('Accurate back passes, %', 0, 100, step=1)
accurate_lateral_passes_percent = st.slider('Accurate lateral passes, %', 0, 100, step=1)
accurate_short_medium_passes_percent = st.slider('Accurate short / medium passes, %', 0, 100, step=1)
accurate_long_passes_percent = st.slider('Accurate long passes, %', 0, 100, step=1)
third_assists_per_90 = st.slider('Third assists per 90', 0.0, float(0.29 * 1.5), step=0.01)
accurate_smart_passes_percent = st.slider('Accurate smart passes, %', 0, 100, step=1)
key_passes_per_90 = st.slider('Key passes per 90', 0.0, float(1.38 * 1.5), step=0.01)
accurate_passes_final_third_percent = st.slider('Accurate passes to final third, %', 0, 100, step=1)
accurate_passes_penalty_area_percent = st.slider('Accurate passes to penalty area, %', 0, 100, step=1)
accurate_through_passes_percent = st.slider('Accurate through passes, %', 0, 100, step=1)
progressive_passes_per_90 = st.slider('Progressive passes per 90', 0.58, float(13.06 * 1.5), step=0.01)
accurate_progressive_passes_percent = st.slider('Accurate progressive passes, %', 0, 100, step=1)
save_rate_percent = st.slider('Save rate, %', 0, 100, step=1)
xG_against = st.slider('xG against', 0.0, float(66.84 * 1.5), step=0.01)
direct_free_kicks_on_target_percent = st.slider('Direct free kicks on target, %', 0, 100, step=1)
penalty_conversion_percent = st.slider('Penalty conversion, %', 0, 100, step=1)

# Select box input fields
england = st.selectbox('English Player?', ['Yes', 'No'])
goalie = st.selectbox('Goalie?', ['Yes', 'No'])
defender = st.selectbox('Defender?', ['Yes', 'No'])
midfielder = st.selectbox('Midfielder?', ['Yes', 'No'])
attacker = st.selectbox('Attacker?', ['Yes', 'No'])

# Convert Yes/No to 1/0
england = 1 if england == 'Yes' else 0
goalie = 1 if goalie == 'Yes' else 0
defender = 1 if defender == 'Yes' else 0
midfielder = 1 if midfielder == 'Yes' else 0
attacker = 1 if attacker == 'Yes' else 0

# Predict button
if st.button('Predict Market Value'):
    # Prepare the input data
    input_data = np.array([[age, matches_played, minutes_played, goals, xG, assists, xA, duels_per_90, duels_won_percent, height,
                            successful_defensive_actions_per_90, defensive_duels_per_90, defensive_duels_won_percent, aerial_duels_per_90,
                            aerial_duels_won_percent, sliding_tackles_per_90, shots_blocked_per_90, interceptions_per_90, 
                            successful_attacking_actions_per_90, goals_per_90, non_penalty_goals_per_90, shots, goal_conversion_percent, 
                            assists_per_90, xA_per_90, crosses_per_90, accurate_crosses_percent, accurate_crosses_left_flank_percent, 
                            crosses_right_flank_per_90, accurate_crosses_right_flank_percent, successful_dribbles_percent, offensive_duels_per_90, 
                            offensive_duels_won_percent, progressive_runs_per_90, accurate_passes_percent, accurate_forward_passes_percent, 
                            accurate_back_passes_percent, accurate_lateral_passes_percent, accurate_short_medium_passes_percent, 
                            accurate_long_passes_percent, third_assists_per_90, accurate_smart_passes_percent, key_passes_per_90, 
                            accurate_passes_final_third_percent, accurate_passes_penalty_area_percent, accurate_through_passes_percent, 
                            progressive_passes_per_90, accurate_progressive_passes_percent, save_rate_percent, xG_against, 
                            direct_free_kicks_on_target_percent, penalty_conversion_percent, england, goalie, defender, midfielder, attacker]])

    # Predict market value
    prediction = model.predict(input_data)

    st.write(f"The predicted market value of the player is: ${prediction[0]:,.2f}")

# Note: This code assumes that the model and the input features are correctly aligned.


