class Song(object): 
	def __init__(self, lyrics): 
		self.lyrics = lyrics

	def sing_me_a_song(self): 
		for line in self.lyrics: 
			print line

happy_bday = Song(["WTF WTF WTF", 
					"how ABOUT NOW", 
					"HIHHIHHIHI"])
bulls_on_paradise = Song(["GO GO GO GO"])

happy_bday.sing_me_a_song()

bulls_on_paradise.sing_me_a_song()