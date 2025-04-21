import pickle

hangout = {
    "Barbara": set(),
    "Beidou": set(),
    "Bennett": set(),
    "Chongyun": set(),
    "Diona": set(),
    "Faruzan": set(),
    "Gorou": set(),
    "Heizou": set(),
    "Kaveh": set(),
    "Kaeya": set(),
    "Layla": set(),
    "Lynette": set(),
    "Ningguang": set(),
    "Noelle 1": set(),
    "Noelle 2": set(),
    "Sayu": set(),
    "Shinobu": set(),
    "Thoma": set(),
    "Yun Jin": set()
    }

sq = {
    "Albedo": set(),
    "Alhaitham": set(),
    "Amber": set(),
    "Arlecchino": set(),
    "Ayaka": set(),
    "Ayato": set(),
    "Baizhu": set(),
    "Childe": set(),
    "Chiori": set(),
    "Clorinde": set(),
    "Cyno 1": set(),
    "Cyno 2": set(),
    "Dehya": set(),
    "Diluc": set(),
    "Emilie": set(),
    "Eula": set(),
    "Furina": set(),
    "Ganyu": set(),
    "Hu Tao": set(),
    "Itto": set(),
    "Jean": set(),
    "Kaeya": set(),
    "Kazuha": set(),
    "Kinich": set(),
    "Klee": set(),
    "Kokomi": set(),
    "Lisa": set(),
    "Lyney": set(),
    "Mona": set(),
    "Mualani": set(),
    "Nahida 1": set(),
    "Nahida 2" : set(),
    "Navia": set(),
    "Neuvillette": set(),
    "Nilou": set(),
    "Raiden 1": set(),
    "Raiden 2": set(),
    "Razor": set(),
    "Sigewinne": set(),
    "Tighnari": set(),
    "Venti": set(),
    "Wriothesley": set(),
    "Xiangling": set(),
    "Xianyun": set(),
    "Xiao": set(),
    "Xingqiu": set(),
    "Yae Miko": set(),
    "Yelan": set(),
    "Yoimiya 1": set(),
    "Yoimiya 2": set(),
    "Zhongli 1": set(),
    "Zhongli 2": set()
    }

aq = set()

with open("story_quest.pkl", "wb") as f:
    pickle.dump(sq, f)

with open("hangout.pkl", "wb") as f:
    pickle.dump(hangout, f)

with open("archon_quest.pkl", "wb") as f:
    pickle.dump(aq, f)
