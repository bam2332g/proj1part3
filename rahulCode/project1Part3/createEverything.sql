CREATE TABLE SportsLeague (leagueID integer,
							name char(3) NOT NULL,
							avgYrsOfExp real,
							numOfPlyrOnTeam integer,
							avgAgeOfPlyr real,
							avgAgeOfTeam real,
							avgWinPct real,
							PRIMARY KEY(leagueID),
							CHECK (avgYrsOfExp>=0 and
									numOfPlyrOnTeam>=0 and
									avgAgeOfPlyr>=0 and
									avgAgeOfTeam>=0 and
									avgWinPct>=0 and
									avgWinPct<=1 and
									(name= 'NBA' or name= 'NFL')));

CREATE TABLE Team(teamID integer,
				  	name varchar(100) NOT NULL,
				  	leagueID integer NOT NULL,
				  	ties integer NOT NULL,
				  	wins integer NOT NULL,
				  	losses integer NOT NULL,
				  	numberOfChampionships integer NOT NULL,
				  	probOfWinningChmp real,
				  	PRIMARY KEY (teamID,leagueID),
				  	FOREIGN KEY (leagueID) REFERENCES SportsLeague ON DELETE NO ACTION,
				  	CHECK (wins>=0 and
				  			losses>=0 and
				  			ties>=0 and
				  			probOfWinningChmp>=0 and
				  			probOfWinningChmp<=1 and
				  			numberOfChampionships>=0));

CREATE TABLE Player(playerID integer,
					leagueID integer NOT NULL,
					teamID integer NOT NULL,
					name varchar(100) NOT NULL,
					dateOfBirth date NOT NULL,
					expInLeague real NOT NULL,
					position varchar(2) NOT NULL,
					numberOfChampionships integer NOT NULL,
					PRIMARY KEY (playerID),
					FOREIGN KEY (teamID, leagueID) REFERENCES Team ON DELETE NO ACTION,
					CHECK (expInLeague>=0 and
							expInLeague<=1 and
							((leagueID=0 and (position='QB' or position='WR' or position='RB')) or
							(leagueID=1 and (position= 'G' or position= 'C' or position= 'F'))
							)));

CREATE TABLE NFLPlayerStats(playerID integer,
						year integer,
						games integer NOT NULL,
						qbYards integer NOT NULL,
						qbInter integer NOT NULL,
						qbSacks integer NOT NULL,
						qbCompl integer NOT NULL,
						qbAtt integer NOT NULL,
						qbRating real NOT NULL,
						rushingAtt integer NOT NULL,
						rushingYds integer NOT NULL,
						receptions integer NOT NULL,
						receivingYds integer NOT NULL,
						td integer NOT NULL,
						probowl boolean NOT NULL,
						mvp boolean NOT NULL,
						PRIMARY KEY(playerID, year),
						FOREIGN KEY(playerID) REFERENCES Player ON DELETE CASCADE,
						CHECK(qbYards>=0 and
								qbInter>=0 and
								qbSacks>=0 and
								qbCompl>=0 and
								qbAtt>=qbCompl and
								qbRating>=0 and
								rushingAtt>=0 and
								rushingYds>=0 and
								receptions>=0 and
								receivingYds>=0 and
								td>=0 and
								year>=2005));

CREATE TABLE NBAPlayerStats(playerID integer,
						year integer,
						games integer NOT NULL,
						turnovers integer NOT NULL,
						steals integer NOT NULL,
						blks integer NOT NULL,
						pts integer NOT NULL,
						fgm integer NOT NULL,
						fga integer NOT NULL,
						tpm integer NOT NULL,
						tpa integer NOT NULL,
						ftm integer NOT NULL,
						fta integer NOT NULL,
						rebs integer NOT NULL,
						assists integer NOT NULL,
						allStar boolean NOT NULL,
						mvp boolean NOT NULL,
						PRIMARY KEY(playerID,year),
						FOREIGN KEY(playerID) REFERENCES Player ON DELETE CASCADE,
						CHECK (year>=2005 and
								turnovers>=0 and
								steals>=0 and
								blks>=0 and
								pts>=0 and
								fgm>=0 and
								fga>=fgm and
								tpm>=0 and
								tpa>=tpm and
								ftm>=0 and
								fta>=ftm and
								rebs>=0 and
								assists>=0));

CREATE TABLE TopPlayer(topPlayerID integer,
						leagueID integer NOT NULL,
						name varchar(100) NOT NULL,
						numOfChamps integer NOT NULL,
						position varchar(2) NOT NULL,
						numOfAllStar integer NOT NULL,
						numOfMvp integer NOT NULL,
						PRIMARY KEY (topplayerID),
						FOREIGN KEY (leagueID) REFERENCES SportsLeague ON DELETE NO ACTION,
						CHECK (numOfChamps>=0 and
								numOfAllStar>=0 and
								numOfMvp>=0 and
								((leagueID=0 and (position='QB' or position='WR' or position='RB')) or
								(leagueID=1 and (position= 'G' or position= 'C' or position= 'F'))
								)));

CREATE TABLE TopNFLPlayerStats(topPlayerID integer,
								qbYards real NOT NULL,
								qbInter real NOT NULL,
								qbSacks real NOT NULL,
								qbCompl real NOT NULL,
								qbAtt real NOT NULL,
								qbRating real NOT NULL,
								rushingAtt real NOT NULL,
								rushingYds real NOT NULL,
								receptions real NOT NULL,
								receivingYds real NOT NULL,
								td real NOT NULL,
								PRIMARY KEY(topPlayerID),
								FOREIGN KEY(topPlayerID) REFERENCES TopPlayer ON DELETE CASCADE,
								CHECK (qbYards>=0 and
										qbInter>=0 and
										qbSacks>=0 and
										qbCompl>=0 and
										qbAtt>=qbCompl and
										qbRating>=0 and
										rushingAtt>=0 and
										rushingYds>=0 and
										receptions>=0 and
										receivingYds>=0 and
										td>=0));

CREATE TABLE TopNBAPlayerStats(topPlayerID integer,
							stlpg real NOT NULL,
							blkpg real NOT NULL,
							ppg real NOT NULL,
							fgpg real NOT NULL,
							tppg real NOT NULL,
							ftpg real NOT NULL,
							rbspg real NOT NULL,
							astpg real NOT NULL,
							PRIMARY KEY(topPlayerID),
							FOREIGN KEY(topPlayerID) REFERENCES TopPlayer ON DElETE CASCADE,
							CHECK (stlpg>=0 and
									blkpg>=0 and
									ppg>=0 and
									fgpg>=0 and
									fgpg<=1 and
									tppg>=0 and
									tppg<=1 and
									ftpg>=0 and
									ftpg<=1 and
									rbspg>=0 and
									astpg>=0));

CREATE TABLE Predictions(playerID integer,
							topPlayerID integer NOT NULL,
							similarityScore real NOT NULL,
							probOfAllStar real NOT NULL,
							probOfMvp real NOT NULL,
							PRIMARY KEY (playerID),
							FOREIGN KEY(playerID) REFERENCES Player ON DELETE CASCADE,
							FOREIGN KEY(topPlayerID) REFERENCES TopPlayer ON DELETE NO ACTION,
							CHECK (probOfAllStar>=0 and
									probOfAllStar<=1 and
									probOfMvp>=0 and
									probOfMvp<=1 and
									similarityScore>=0));




