import streamlit as st
import pickle
from datetime import datetime
startTime = datetime.now()


filename = "gamesModel2.sv"
model = pickle.load(open(filename,'rb'))

firstBlood_d = {1:"Your team gets first blood", 2:"Enemy team gets first blood"}
firstTower_d = {1:"Your team gets first tower", 2:"Enemy team gets first tower"}
firstInhibitor_d = {1:"Your team get first inhibitor", 2:"Enemy team gets first inhibitor"}
firstBaron_d = {0:"Noone gets first baron", 1:"Your team gets first baron", 2:"Enemy team gets first baron"}
firstDragon_d = {0:"Noone gets first dragon", 1:"Your team gets first dragon", 2:"Enemy team gets first dragon"}
firstRiftHerald_d = {0:"Noone gets first herald", 1:"Your team gets first herald", 2:"Enemy team gets first herald"}


def main():

	st.set_page_config(page_title="LoL Games Calculator")
	st.image("PUM Project Logo.jpg")
	overview = st.container()
	left, right = st.columns(2)
	prediction = st.container()

	with overview:
		st.title("League of Legends Win Calculator")

	with left:
		firstBaron_radio = st.radio("First baron", list(firstBaron_d.keys()),format_func=lambda x : firstBaron_d[x])
		firstDragon_radio = st.radio("First dragon", list(firstDragon_d.keys()),format_func=lambda x : firstDragon_d[x])
		firstRiftHerald_radio = st.radio("First rift herald", list(firstRiftHerald_d.keys()),format_func=lambda x : firstRiftHerald_d[x])
        
        
	with right:
		firstBlood_radio = st.radio("First blood", list(firstBlood_d.keys()),format_func=lambda x : firstBlood_d[x])
		firstTower_radio = st.radio("First tower", list(firstTower_d.keys()),format_func=lambda x : firstTower_d[x])
		firstInhibitor_radio = st.radio("First inhibitor", list(firstInhibitor_d.keys()),format_func=lambda x : firstInhibitor_d[x])

	data = [[firstBlood_radio, firstTower_radio, firstInhibitor_radio, firstBaron_radio, firstDragon_radio, firstRiftHerald_radio]]
	winner = model.predict(data)
	s_confidence = model.predict_proba(data)

	with prediction:
		st.header("Will you win the game?")
		st.header(("Yes" if winner[0] == 1 else "No"))
		try:
			st.write("Percent certainty {0:.2f} %".format(s_confidence[0][winner][0] * 100))
		except:
			st.write("Unable to determine certainty")

if __name__ == "__main__":
    main()