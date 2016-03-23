# TournamentPairer
Simple tournament pairing script written in Python. Implements the pairing method described in the Steamroller 2015 document from Privateer Press.

Steamroller tournament format: http://privateerpress.com/organized-play/steamroller-tournaments

The script is designed to work with the included spreadsheet.

============
Instructions
============

Before:
0:	Read all instructions before the tournament and practice using the program using the provided "2016 Ides of March After Round 4.ods" spreadsheet.

1:	Download Python 3.5 (or higher) from https://www.python.org

2:	Rename "Tournament sheet with SoS 7-Round v009.ods" to something more representative of your tournament.

3:	Open the spreadsheet, go to the "Scores" sheet and enter the "Family Name" and "Given Name"s of all your players into the fields.

	a:	The spreadsheet will automatically create a "Short Name" for each player.
		Each player must have a unique short name for the Strength of Schedule calculation to work.
		If not, manually change the name in the yellow boxes.
		The first box is orange to indicate it is the first row. There is no other special significance for that cell.

4:	Go to the "Pairing Data" tab and enter the clubs for each player. If a region has only one club, it is sufficient to enter the region's name.

	Copy all cells in columns A to I. Most of these cells will contain "#N/A" or be blank. This is normal.

	Open "PairingData.txt" with a text editor and replace its contents with the copied data from the spreadsheet.

	Run "drawRoundN.bat"

	Two files a created. "RefreshingRoundDrawXX.html". These are the round draws to be shown to players. If you are able to put them on a second screen that faces the players (projector), you should open it in a web browser, change the web browser to fullscreen mode, and zoom the web browser so the table occupies most of the screen. You can then ignore this for the remainder of the tournament.

	Replace "YourLogo.jpg" with a suitable image.

4a:	Alternatively, make the draw using the drop-down boxes on the "Round Draw" tab.

	Copy the draw to "aaRound 1 Draw.txt".

	Run "drawRound1.bat"

5:	Print the score sheets from "Score Sheets A5" or use the Privateer Press score / army list sheets.
	
During:

1:	In the "Scores" tab, enter the player's results.

2:	After entering all the results, go to the "Pairing Data" tab and copy all cells in columns A to I into "PairingData.txt"

	2016 Ides of March After Round 4.ods has been provided as an example of what it should look like during the tournament and for you to try this step before the tournament.

Prize Giving:

1:	Go to the "Final Standings" tab and select columns B to M

2:	Sort (Data > Sort) by the column "Sort Descending" and change the direction to "Descending"

	The player at the top of the spreadsheet is the winner and so on.

3:	Sort by CP and KP to get the relevant winners.

4:	Determine "Best Assassin" manually

5:	Determine Best Sport manually

6:	Determine Best Painted manually

After:

1: Sort Final Standings tab by "Sort Descending" again and take a screenshot / copy to a separate file / etc. and post on social media as desired.
