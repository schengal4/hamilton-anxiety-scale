import streamlit as st

st.title('Hamilton Anxiety Scale Assessment')
st.write('This assessment measures the severity of a person’s anxiety based on the Hamilton Anxiety Scale.')

options = ["Not present", "Mild", "Moderate", "Severe", "Very Severe"]

response_mapping = {
    "Not present": 0,
    "Mild": 1,
    "Moderate": 2,
    "Severe": 3,
    "Very Severe": 4
}

# Questions
anxious_mood_text = 'Anxious mood: Worries, anticipation of the worst, fearful anticipation, irritability'
anxious_mood = st.selectbox('Anxious mood', options, help=anxious_mood_text)

tension_text = 'Tension: Feelings of tension, fatigability, startle response, etc.'
tension = st.selectbox('Tension', options, help=tension_text)

fears_text = 'Fears: Of dark, of strangers, of being left alone, etc.'
fears = st.selectbox('Fears', options, help=fears_text)

insomnia_text = 'Insomnia: Difficulty in falling asleep, broken sleep, etc.'
insomnia = st.selectbox('Insomnia', options, help=insomnia_text)

intellectual_text = 'Intellectual: Difficulty in concentration, poor memory.'
intellectual = st.selectbox('Intellectual', options, help=intellectual_text)

depressed_mood_text = 'Depressed mood: Loss of interest, lack of pleasure in hobbies, etc.'
depressed_mood = st.selectbox('Depressed mood', options, help=depressed_mood_text)

somatic_anxiety_text = 'Somatic (muscular): Pains and aches, twitching, stiffness, etc.'
somatic_anxiety = st.selectbox('Somatic (muscular)', options, help=somatic_anxiety_text)

somatic_sensory_text = 'Somatic(sensory): Tinnitus, blurring of vision, hot and cold flushes, etc.'
somatic_sensory = st.selectbox('Somatic (sensory)', options, help=somatic_sensory_text)

cardiovascular_symptoms_text = "Tachycardia, palpitations, pain in chest, etc."
cardiovascular_symptoms = st.selectbox("Cardiovascular symptoms", options, help=cardiovascular_symptoms_text)

respiratory_symptoms_text = "Pressure or constriction in chest, choking feelings, sighing, dyspnea."
respiratory_symptoms = st.selectbox("Respiratory symptoms", options, help=respiratory_symptoms_text)

gastrointestinal_symptoms_text = "Difficulty in swallowing, wind abdominal pain, burning sensations, etc."
gastrointestinal_symptoms = st.selectbox("Gastrointestinal symptoms", options, help=gastrointestinal_symptoms_text)

genitourinary_symptoms_text = "Frequency of micturition, urgency of micturition, amenorrhoea, etc."
genitourinary_symptoms = st.selectbox("Genitourinary symptoms", options, help=genitourinary_symptoms_text)

autonomic_symptoms_text = "Dry mouth, flushing, pallor, tendency to sweat, etc."
autonomic_symptoms = st.selectbox("Autonomic Symptoms", options, help=autonomic_symptoms_text)

behavior_at_interview_text = "Fidgeting, restlessness, pacing, tremor of hands, furrowed brow, strained face, etc."
behavior_at_interview = st.selectbox("Behavior at interview", options, help=behavior_at_interview_text)
# Calculate the total score

anxious_mood_value = response_mapping[anxious_mood]
tension_value = response_mapping[tension]
fears_value = response_mapping[fears]
insomnia_value = response_mapping[insomnia]
intellectual_value = response_mapping[intellectual]
depressed_mood_value = response_mapping[depressed_mood]
somatic_anxiety_value = response_mapping[somatic_anxiety]
somatic_sensory_value = response_mapping[somatic_sensory]
cardiovascular_symptoms_value = response_mapping[cardiovascular_symptoms]
respiratory_symptoms_value = response_mapping[respiratory_symptoms]
gastrointestinal_symptoms_value = response_mapping[gastrointestinal_symptoms]
genitourinary_symptoms_value = response_mapping[genitourinary_symptoms]
autonomic_symptoms_value = response_mapping[autonomic_symptoms]
behavior_at_interview_value = response_mapping[behavior_at_interview]

total_score = (anxious_mood_value + tension_value + fears_value + insomnia_value + intellectual_value +
               depressed_mood_value + somatic_anxiety_value + somatic_sensory_value + cardiovascular_symptoms_value +
               respiratory_symptoms_value + gastrointestinal_symptoms_value + genitourinary_symptoms_value +
               autonomic_symptoms_value + behavior_at_interview_value)


# Display the score and interpretation
st.write('Your Total Score is: ', total_score)

if total_score <= 17:
    st.write('Indicates mild anxiety severity.')
elif 18 <= total_score <= 24:
    st.write('Indicates mild to moderate anxiety severity.')
elif 25 <= total_score <= 30:
    st.write('Indicates moderate to severe anxiety severity.')
else:
    st.write('Indicates severe anxiety severity.')
