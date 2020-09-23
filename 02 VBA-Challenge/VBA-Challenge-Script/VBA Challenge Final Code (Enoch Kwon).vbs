Sub VBAChallenge():

	Dim ws as Worksheet
	' LOOP THROUGH ALL SHEETS
	For Each ws in Worksheets


		' Define Variables
		Dim Ticker As String
		Dim Volume As Double
		Volume = 0
	


		Dim YearlyChange As Double
		Dim PercentChange As Double

 		' Define table row

		Dim tablerow As Integer
		tablerow = 2

		' Set Headers

		ws.Cells(1, 9).Value = "Ticker"
		ws.Cells(1, 10).Value = "Yearly Change"
		ws.Cells(1, 11).Value = "Percent Change"
		ws.Cells(1, 12).Value = "Total Stock Volume"
		ws.Cells(1, 16).Value = "Ticker"
		ws.Cells(1, 17).Value = "Value"


		' define last row

		Lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row

				YearOpen = ws.Cells(2, 3).Value


			For i = 2 To Lastrow


				If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then

	
			' Find/Define Values


				Ticker = ws.Cells(i,1).Value

				Volume = Volume + ws.Cells(i,7).Value

				YearClose = ws.Cells(i, 6).Value

				YearlyChange = (YearClose - YearOpen)

						If YearOpen <> 0 Then
                    		PercentChange = (YearlyChange / YearOpen) * 100

						End If



					If (YearlyChange > 0) Then

						ws.Cells(tablerow, 10).Interior.ColorIndex = 4

					ElseIf (YearlyChange <= 0) Then

						ws.Cells(tablerow, 10).Interior.ColorIndex = 3

					End If

					' Insert Values

				ws.Cells(tablerow, 9).Value = Ticker
				ws.Cells(tablerow,10).Value = YearlyChange
				ws.Cells(tablerow,11).Value = PercentChange
				ws.Cells(tablerow,12).Value = Volume



				' Attempting Challenge Section

					If (PercentChange > Greatest_Percent_Increase) Then
						Greatest_Percent_Increase = PercentChange
						GreatestTicker = Ticker

					End If


					If (PercentChange < 0) and (PercentChange < Greatest_Percent_Decrease) Then
						Greatest_Percent_Decrease = PercentChange
						GreatestDecreaseTicker = Ticker

					End If


					If (Volume > Greatest_Total_Volume) Then
						Greatest_Total_Volume = Volume
						Greatest_Total_Volume_Ticker = Ticker

					End If

					PercentChange = 0

					Ticker = 0



	

				' Challenge Headers Inserts etc

				ws.Cells(2, 15).Value = "Greatest % Increase"
				ws.Cells(3, 15).Value = "Greatest % Decrease"
				ws.Cells(4, 15).Value = "Greatest Total Volume"

				' Challenge Ticker Inserts

				ws.Cells(2, 16).Value = GreatestTicker
				ws.Cells(3, 16).Value = GreatestDecreaseTicker
				ws.Cells(4, 16).Value = Greatest_Total_Volume_Ticker

				' Challenge Values Insert

				ws.Cells(2, 17).Value = Greatest_Percent_Increase
				ws.Cells(3, 17).Value = Greatest_Percent_Decrease
				ws.Cells(4, 17).Value = Greatest_Total_Volume



				tablerow = tablerow + 1

				YearlyChange = 0

				YearClose = 0

				YearOpen = ws.Cells(i + 1, 3).Value

				Volume = 0


			Else

				Volume = Volume + ws.Cells(i, 7).Value

			End If

	 	Next i

	 	Greatest_Percent_Increase = 0
	 	Greatest_Percent_Decrease = 0
	 	Greatest_Total_Volume = 0


	Next ws


End Sub