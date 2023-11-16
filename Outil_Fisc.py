import streamlit as st

Bleu = '#0D2A59'
Rouge = '#E61434'

col1, col2, col3 = st.columns(3)
with col2 :
    st.subheader("Outil de calcul")


st.subheader("")
revenu_brut = st.number_input("Revenu annuel brut en € : ")
revenu = revenu_brut-revenu_brut*0.15

result = 0

if revenu > 177106 :
    ip = (28797-11294)*0.11 + (82341-28797)*0.3 + (177106-82341)*0.41 + (revenu-177106)*0.45

elif revenu < 177106 and revenu > 82341:
    ip = (28797-11294)*0.11 + (82341-28797)*0.3 + (revenu-82341)*0.41

elif revenu < 82341 and revenu > 28797:
    ip = (28797-11294)*0.11 + (revenu-28797)*0.3

elif revenu < 28797 and revenu > 11294:
    ip = (revenu-11294)*0.11

else:
    ip = 0

result = ip


st.subheader("")
st.subheader("")
col1, col2  = st.columns(2)
with col1:
    st.metric(label="Revenu net annuel avant IR", value=round(revenu,2), delta="en €")
with col2:
    st.metric(label="Impot sur le revenu", value=round(result,2), delta="en €")

col1, col2  = st.columns(2)
with col1:
    st.metric(label="Revenu net sur 12 mois après IR", value=round((revenu/12)-(result/12),2), delta="en €")
with col2:
    st.metric(label="Revenu net sur 13 mois après IR", value=round((revenu/13)-(result/12),2), delta="en €")